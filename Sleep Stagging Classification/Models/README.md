# Indian Medicinal Plants Classification

## 🎯 Goal
The primary aim of this project is to classify sleep stages from polysomnographic data using various machine learning models and evaluate their performance.

## 🧵 Dataset

The link to the dataset is given below :-

**Link :-
https://www.kaggle.com/datasets/mahek6114/sleep-stagging/data

## 🧾 Description

This project involves the application of machine learning models to classify sleep stages from the given dataset. The focus will be on comparing the performance of models such as Random Forest, Support Vector Machine (SVM), Convolutional Neural Networks (CNN), and Recurrent Neural Networks (RNN). The project also includes data preprocessing, feature extraction, model training, evaluation, and visualization of results.
## 🧮 What I had done!

### 1. Data Loading and Preparation:
    Loaded the polysomnographic data into a pandas DataFrame for manipulation and analysis.
    Extracted relevant features from the raw data.

### 2. Exploratory Data Analysis (EDA):
    Visualized the distribution of sleep stages.
    Identified and addressed any class imbalances.

### 3. Data Analysis:
    Normalized the data.
    Split the data into training, validation, and test sets.

### 4. Image Preprocessing and Model Training:
    Loaded and preprocessed the test images, ensuring normalization of pixel values for consistency.
        Iterated through multiple models (VGG16, ResNet50 , Xception) saved in a directory and made predictions on the test dataset.
        Saved the predictions to CSV files for further analysis and comparison.

### 5. Model Prediction Visualization:
    Loaded models and visualized their predictions on a sample set of test images to qualitatively assess model performance.
        Adjusted image preprocessing for models requiring specific input sizes (e.g., 299x299 for Xception).

## 🚀 Models Implemented

The inference of sleep stages is done by training a deep neural network to learn the association between the multivariate time series of HR, RR, λ, and BMF and the sequence of sleep-staging labels scored by human experts. We used a biLSTM neural network to classify the sleep stages. The biLSTM architecture can learn sequence information in backward and forward directions20. We considered the biLSTM model suitable for predicting sleep staging because the transitions of sleep progression are known to have a temporal dependency. 
The model was composed of a sequential input layer, three biLSTM layers, and a fully connected layer. Each bi-LSTM layer consisted of 128 hidden cells. A dropout layer (rate of 0.2) was added after each bi-LSTM layer to reduce overfitting. The fully connected layer consisted of six neurons corresponding to the six class probabilities of light non-REM sleep (N1, N2), deep non-REM sleep (N3), REM sleep (REM), WK, and LV. The softmax function was used as the activation function in the output of the fully connected layer, which could be used to predict the multinomial probability distribution. Finally, the classification layer classified the epochs by the epoch sleep stage based on the probability distribution.
![image](https://github.com/user-attachments/assets/05b13983-a03a-4a30-a653-c573b9f9798a)

## Estimation of sleep parameters
We investigated the potential of the deep-learning-based sleep stage classification in calculating sleep parameters. The following six sleep parameters were chosen: total sleep time (TST), defined as the total time of non-wake stages; sleep latency (SL), defined as the duration of time from bedtime to the onset of sleep; wake after sleep onset (WASO), calculated as time in bed (TIB)-SL-TST; percent time of REM sleep in TST (REM%); percent time of NREM sleep in TST (NREM%); and sleep efficiency (SE), defined as TST/TIB. These parameters derived from deep learning were compared with those assessed by PSG measurements.

## Results
(A) ![image](https://github.com/user-attachments/assets/23017af8-41b2-4eaf-b44b-8503f953ed41)
(B) ![image](https://github.com/user-attachments/assets/49024c8e-8329-43bb-a5b2-6864d801158b)
Examples of an overnight sleep stage prediction by the model in the low- (A) and high-AHI (B) participants at the same age. In both A and B, (a) sleep stage scored by a human expert; (b) predicted sleep stage by the model; (c) and (d) pie charts whose segments represent the fractions of each of the sleep stages of TIB; (e) confusion matrix; (f) balanced accuracy, Cohen’s κ, and F1 score of each of the sleep stages derived from the confusion matrix; (g) percentage of time spent in each sleep stage to the TIB for the ground truth (True) and prediction (Predicted). (A) a 37-year-old man with an AHI of 3.2, (B) a 37-year-old man with an AHI of 80.2. SS: sleep stage, pSS: predicted sleep stage, WK: wake stage, REM: rapid eye movement sleep stage, N1: non-REM N1 sleep stage, N2: non-REM N2 sleep stage, N3: non-REM N3 sleep stage.

![image](https://github.com/user-attachments/assets/bc110db1-512d-4dbf-b071-1d59802d1039)
Box plot showing the distribution of overall performance in terms of balanced accuracy, Cohen's κ, and F1 score. The box plot displays the 25th percentile, median, and 75th percentile. Whiskers extend to the minimum and maximum values. Black and red open circles denote male and female participants, respectively.
![image](https://github.com/user-attachments/assets/6bf574a4-19f9-4465-9cdc-49a1e8915e0e)
Scatter plots of overall performance in terms of balanced accuracy, Cohen's κ, and F1 score against AHI (A, B, C), age (D, E, F), and SE (G, H, I) of participants. Black and red open circles denote male and female participants, respectively. Regression lines are displayed with solid lines. Linear regression equations with a correlation coefficient (r) for each relation are indicated. AHI: apnea hypopnea index; SE: sleep efficiency.




## 📚 Libraries Needed

1. **NumPy:** Fundamental package for numerical computing.
2. **pandas:** Data analysis and manipulation library.
3. **scikit-learn:** Machine learning library for classification, regression, and clustering.
4.  **Matplotlib:** Plotting library for creating visualizations.
5.  **Keras:** High-level neural networks API, typically used with TensorFlow backend.
6. **tqdm:** Progress bar utility for tracking iterations.
7. **seaborn:** Statistical data visualization library based on Matplotlib.

## 📢 Conclusion

the present study demonstrated that the biLSTM deep learning model performed well in a five-class sleep stage classification using only four physiological parameters derived from cardiorespiratory and body movement activities in a population with suspected sleep disorders. Currently, some issues remain to be addressed, particularly regarding the limitation of model performance for participants with a high AHI score. To achieve a more accurate prediction in high-AHI participants, we need to investigate whether other cardiorespiratory parameters could provide information about sleep fragmentation associated with repeated arousal during sleep. Analyzing the performance index of sleep stage classification in terms of arousal index and periodic limb movements is also a future task. Additionally, we should consider reducing the class imbalance by recruiting more participants with a higher percentage of N3 epochs and/or healthy control participants. Considering the relatively small sample size, future studies should include a larger sample size to increase the generalization ability of the deep learning model. We expect that the biLSTM model will have better performance in automated sleep staging with more balanced training data between the classes, as this model captures the temporal dynamics of the sleep-stage transition by attending to features of the parameters in forward and backward sequences

## ✒️ Your Signature

Full name:-Mahek Patel                   </br>
Github Id :- [https://github.com/kyra-09  ](https://github.com/mahek0620) </br>
Email ID :-mahekrpatel611@gmail.com  
LinkdIn :- www.linkedin.com/in/mahek-patel-19670625b
</br>
Participant Role :- Contributor / GSSOC (Girl Script Summer of Code ) - 2024
