#  Maternal Health Risk prediction using machine learning

The Maternal Risk Prediction project is a Streamlit web application designed to predict the risk level (low, medium, or high) for maternal health based on specific health metrics. The application utilizes a trained XGBoost model to make predictions. Users input their age, systolic blood pressure, diastolic blood pressure, blood sugar levels, body temperature, and heart rate. The model processes these inputs and provides a risk assessment. The interface is user-friendly, featuring a sleek design with a blurred background image for aesthetic appeal and clarity. This application aims to offer a quick and accessible tool for expecting mothers to assess their health risks, facilitating better-informed healthcare decisions.

## Data Set

The below csv dataset from kaggle is used as reference which contains nearly 1000+ rows (maternal Health risk data Set.csv) on which porcessing is performed to obtained a  processed data. 

The dataset link is are as follows :-
https://www.kaggle.com/datasets/csafrit2/maternal-health-risk-data

on this dataset, below processing are performed :
1) featue scaling and column reinitialization
2) errors and outliers removal
3) remove na,missing values , regularization etc
(all this works ar depicted in .ipynb file)

The model is trained on processed_data_car.csv file and all works associated with it are depicted in 
maternal_health_risk_prediction.ipynb file.

## Methodology

The project follows the below structured methodology ranging from data preprocessing pipeline to model training, evaluation and deployment :-

1. **Data Preprocessing and feature enginnering**: 
2. **Exploratory Data Analysis (EDA)**:
    after Data preprocessing the next step is Exploratory  data analysis using different plotting libraries like matplotlib,pandas,seaborn and plotly.following plots were plotted in this step:-
    1) Pie chart 
    2) violen plot 
    3) box plot of numerical features
    4) count plot 
    5) heatmap or confusion matrix for four different models of machine learning
    6) model comparison graphs
    7) line plots
    (refer images folder for this images and graph observation)


4. **Model Training and evaluation**: 
     The four machine learning model random forest ,xgboost ,KNN, gradient boosting machine are selected for model training over the inputed processed data:
     random forest accuracy : 85 %
     GBM accuracy : 77 %
     XGboost accuracy : 86 %
     KNN accuracy : 76 %

     The XGBoost machine model is then loaded into streamlit application after installing and using joblib library.

5. **Inference**: 
      Deployed the model with the help streamlit web application to predict the maternal health risk associated with a women.


## Libraries Used

1. **Joblib**: For downloading the random forest model
2. **Scikit learn**: For machine learning processing  and operations
3. **Matplotlib**: For plotting and visualizing the detection results.
4. **Pandas**: For image manipulation.
5. **NumPy**: For efficient numerical operations.
6. **Seaborn** : for advanced data visualizations
7. **plotly** : for 3D data visualizations .
8. **Streamlit** : for creating gui of the web application.


## How to Use

1. **Clone the Repository**: 
    ```sh
    git clone url_to_this_repository
    ```

2. **Install Dependencies**: 
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Model**: 
    ```python
    streamlit run app.py
    ```

4. **View Results**: The script will allow you to predict the maternal risk associated with the lady in pregnancy and therby taking care to avoid it.


## Demo :

