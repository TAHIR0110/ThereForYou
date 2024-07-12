import os
import re
from utils import *
import pandas as pd
import heartpy as hp
from ecgdetectors import Detectors
from QRSDetectorOffline import QRSDetectorOffline

def ecg_preprocessor(detector):
    """
    Detects the QRS complexes in the given ECG signal and extracts the HRV features for every patient
    Parameters: detector (str): The detector to use.
    Returns: None
    """    
    files = [i for i in os.listdir() if(re.search("VP*", i))]
    final_df_list = []
    for i in range(0,len(files)):    
        ecg_df = pd.read_csv(os.path.join(files[i], os.listdir(files[i])[1]), delimiter='\t', names=["ecg", "time", "raw"], header=None, index_col=False)
        ecg_df = ecg_df.drop(columns = "raw")
        ecg_df = ecg_df.sort_values(['time'])
        ecg_df = ecg_df[["time", "ecg"]]
        ecg_df.reset_index(drop=True, inplace = True)
        ecg_df.to_csv(path_or_buf = os.path.join(files[i], "ecg.csv"),index = False)

        sca_ecg = hp.scale_data(ecg_df["ecg"], lower = 0, upper = 3)

        exposure_period_df = pd.read_csv(os.path.join(files[i], os.listdir(files[i])[-1]), delimiter='\t', names=["event", "s_time", "e_time"], header=None, index_col=False)
        
        if (len(exposure_period_df.loc[(exposure_period_df["event"]=="BIOFEEDBACK-OXYGEN-TRAININGS") | (exposure_period_df["event"] == "BIOFEEDBACK-REST")]) == 2):
            exposure_period_df = exposure_period_df.loc[exposure_period_df["event"]!="BIOFEEDBACK-OXYGEN-TRAININGS"].copy()
            exposure_period_df = exposure_period_df.reset_index()

        if(detector == "pan-tompkins"):
            qrs_detector = QRSDetectorOffline(ecg_data_path=os.path.join(files[i],"ecg.csv"), verbose=True, log_data=True, plot_data=False, show_plot=False)
            peaks = extract_peaks()
        elif(detector == "hamilton"):
            detectors = Detectors(100)
            r_peaks = detectors.hamilton_detector(sca_ecg)
            peaks = ecg_df.iloc[r_peaks]

        peaks = peaks.rename(columns = {"ecg" : "ecg_measurement", "time" : "timestamp"})
        peaks.drop_duplicates(subset = ['timestamp'], keep = 'first', inplace = True)
        peaks = extract_hr(peaks)
        peaks = extract_NNI(peaks)
        final_df = adv_features(peaks, exposure_period_df)
        subject_no = files[i]
        final_df.insert(0, "subject", subject_no)
        final_df_list.append(final_df)

    ecg_df = pd.concat(final_df_list)
    ecg_df = ecg_df[(ecg_df["sdNN"].isnull() == False) & (ecg_df["RMSSD"].isnull() == False)]
    _ = ecg_df.groupby(['subject', 'event'])["mean_hr"].agg(['mean'])
    g = _.groupby(['event'])["mean"].agg(['mean'])

    high_clips = g.nlargest(7, 'mean').index[1:4].tolist()
    medium_clips = g.nlargest(7, 'mean').index[4:].tolist()
    high_df = ecg_df.loc[(ecg_df["event"].isin(high_clips))]
    medium_df = ecg_df.loc[(ecg_df["event"].isin(medium_clips))]
    high_df["anxiety"] = 3
    medium_df["anxiety"] = 2
    bio_df = ecg_df[(ecg_df["event"] == "BIOFEEDBACK-REST") | (ecg_df["event"] == "BIOFEEDBACK-OXYGEN-TRAININGS")]
    low_df = bio_df.groupby(['subject']).tail(18)
    low_df["anxiety"] = 1

    ecg_preprocessed = pd.concat([high_df, medium_df, low_df])
    ecg_preprocessed.to_csv(path_or_buf = "ecg_processed.csv", index=False)