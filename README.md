# Anxiety Level Detection 

## Description

This repository contains the code for Anxiety Level Detection in arachnophobic individuals using Supervised Machine Learning algorithms. The physiological signals used were **ECG (Electrocardiogram)**, **GSR (Galvanic Skin Response)** and **RESP (Respiratory signal)**. These signals were pre-processed and the necessary features were extracted. The dataset can be downloaded from [here](https://physionet.org/content/ecg-spider-clip/1.0.0/).

The anxiety level of the patients is classified into one of the three classes (*High*/*Medium*/*Low*). The following classification algorithms have been tested on the HRV (Heart Rate Variability) feature set obtained through feature selection:
- **Logistic Regression**
- **Decision Trees**
- **Random Forest**
- **Extra Trees**
- **XGBoost**
- **Bagging**


## File Description

- [gsr_analysis.ipynb](./gsr_analysis.ipynb) -> This notebook is used for extracting, visualizing and pre-processing the GSR signal.
- [resp.py](./resp.py) -> This script contains code for respiratory signal extraction and breathing rate calculations.
- [ecg.py](./ecg.py) -> Script to obtain R-peaks from ECG signals and extract time domain HRV features.
- [utils.py](./utils.py) -> Script contains helper functions for HRV feature extraction and pre-processing of physiological signals.
- [QRSDetectorOffline.py](./QRSDetectorOffline.py) -> Script for [Pan-Tompkins](https://github.com/c-labpl/qrs_detector) QRS complex detection algorithm.
- [main.py](./main.py) -> Script to run the ML classifiers for Anxiety level classification

## How to run the program


1. Clone the repo
   ```sh
   git clone https://github.com/sidesh27/Anxiety-Detection.git
   ```
   For accounts that are SSH configured
   ```sh
    git clone git@github.com:sidesh27/Anxiety-Detection.git
   ```
2. Install pip
   ```sh
   python -m pip install --upgrade pip
   ```
3. Create and Activate Virtual Environment (Linux)
   ```sh
   python3 -m venv [environment-name]
   source [environment-name]/bin/activate
   ```
4. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```
5. Run main
   ```sh
   python3 main.py --option value
   ```
   
6. The following are the list of trainable parameters that can be provided in the terminal

| Option               | Description                                                                    |
| :------------------- | :----------------------------------------------------------------------------- |
| `--detector or -d`     | R-peak Detection Algorithms [pan-tompkins, hamilton] -> string |
| `--classifier or -clf`  | Classification Algorithms [logreg, decisiontree, xgboost, randomforest, extratrees, bagging] -> string                           |


## References

[1] Michał Sznajder, & Marta Łukowska. (2017). Python Online and Offline ECG QRS Detector based on the Pan-Tomkins algorithm (v1.1.0). Zenodo. https://doi.org/10.5281/zenodo.826614 

[2] Ihmig, F. R., H, A. G., Neurohr-Parakenings, F., Schäfer, S. K., Lass-Hennemann, J., & Michael, T. (2020). On-line anxiety level detection from biosignals: Machine learning based on a randomized controlled trial with spider-fearful individuals. PloS one, 15(6), e0231517. https://doi.org/10.1371/journal.pone.0231517

[3] Ihmig, F. R., Gogeascoechea, A., Schäfer, S., Lass-Hennemann, J., & Michael, T. (2020). Electrocardiogram, skin conductance and respiration from spider-fearful individuals watching spider video clips (version 1.0.0). PhysioNet. https://doi.org/10.13026/sq6q-zg04.

[4] Goldberger, A., Amaral, L., Glass, L., Hausdorff, J., Ivanov, P. C., Mark, R., ... & Stanley, H. E. (2000). PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals. Circulation [Online]. 101 (23), pp. e215-e220.
