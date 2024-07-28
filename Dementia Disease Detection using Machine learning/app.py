import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the pre-trained Logistic Regression model
model_log = joblib.load('dementia_model.pkl')

# Define label encoders (fitted with training data categories)
label_encoders = {
    'Diabetic': LabelEncoder().fit([0, 1]),
    'Education_Level': LabelEncoder().fit([0, 1, 2, 3]),
    'Family_History': LabelEncoder().fit([0, 1]),
    'Smoking_Status': LabelEncoder().fit([0, 1, 2]),
    'APOE_ε4': LabelEncoder().fit([0, 1]),
    'Depression_Status': LabelEncoder().fit([0, 1]),
    'Physical_Activity': LabelEncoder().fit([0, 1, 2]),
    'Prescription': LabelEncoder().fit([0, 1, 2, 3, 4])
}

# Unique values for selectbox
education_levels = ['No School', 'Primary School', 'Secondary School', 'Diploma/Degree']
education_levels_mapping = {'No School': 0, 'Primary School': 1, 'Secondary School': 2, 'Diploma/Degree': 3}
family_history_options = ['No', 'Yes']
family_history_mapping = {'No': 0, 'Yes': 1}
smoking_status_options = ['Never Smoked', 'Former Smoker', 'Current Smoker']
smoking_status_mapping = {'Never Smoked': 0, 'Former Smoker': 1, 'Current Smoker': 2}
apoe_e4_options = ['Negative', 'Positive']
apoe_e4_mapping = {'Negative': 0, 'Positive': 1}
depression_status_options = ['No', 'Yes']
depression_status_mapping = {'No': 0, 'Yes': 1}
physical_activity_levels = ['Sedentary', 'Moderate Activity', 'Mild Activity']
physical_activity_mapping = {'Sedentary': 0, 'Moderate Activity': 1, 'Mild Activity': 2}
prescription_options = ['No prescription', 'Galantamine', 'Donepezil', 'Memantine', 'Rivastigmine']
prescription_mapping = {'No prescription': 0, 'Galantamine': 1, 'Donepezil': 2, 'Memantine': 3, 'Rivastigmine': 4}
diab_options = ['No', 'Yes']
diab_mapping = {'No': 0, 'Yes': 1}

def preprocess_input(data):
    # Create DataFrame from input data
    df = pd.DataFrame([data])

    # Encode categorical features
    for column in label_encoders:
        if column in df.columns:
            df[column] = label_encoders[column].transform(df[column])

    # Fill missing values if necessary (assuming 0 for simplicity)
    df.fillna(0, inplace=True)

    return df

def predict(user_input):
    # Preprocess the user input
    processed_input = preprocess_input(user_input)

    # Make prediction
    prediction = model_log.predict(processed_input)

    # Return the prediction
    return prediction[0]


st.markdown("""
<style>
    .main-container {
        border: 2px solid #f0f0f5;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1);
        background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
    }
    .input-container {
        border: 2px solid #e0e0e0;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 20px;
        background-color: #f9f9f9;
    }
    .output-container {
        border: 2px solid #e0e0e0;
        padding: 10px;
        border-radius: 10px;
        margin-top: 20px;
        background-color: #f9f9f9;
    }
    .heading {
        font-family: 'Arial', sans-serif;
        font-size: 3em;
        text-align: center;
        color: #007BFF;
        font-weight: bold;
    }
    .subheading {
        font-family: 'Arial', sans-serif;
        font-size: 1.5em;
        color: #ffffff;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="heading">Dementia Prediction App</h1>', unsafe_allow_html=True)

with st.form("dementia_form"):
    st.markdown('<h3 class="subheading">Input Information</h3>', unsafe_allow_html=True)
    user_input = {
        'Diabetic': diab_mapping[st.selectbox("Do You Have Diabetes?", diab_options)],
        'BloodOxygenLevel': st.slider("Enter Your Blood Oxygen Level (SpO2):", 60, 120, 90),
        'BodyTemperature': st.slider("Enter Your Body Temperature (in degree Celsius):", 25, 45, 35),
        'Weight': st.slider("Enter Your Weight (in kg):", 10, 150, 30),
        'Prescription': prescription_mapping[st.selectbox("Enter any type of prescription associated with you:", prescription_options)],
        'Age': st.slider("Enter Your Age:", 0, 120, 20),
        'Education_Level': education_levels_mapping[st.selectbox("Choose Your Education Level:", education_levels)],
        'Family_History': family_history_mapping[st.selectbox("Do you have family history of Dementia?", family_history_options)],
        'Smoking_Status': smoking_status_mapping[st.selectbox("Choose your smoking status:", smoking_status_options)],
        'APOE_ε4': apoe_e4_mapping[st.selectbox("Do you have any problem associated with APOE ε4?", apoe_e4_options)],
        'Depression_Status': depression_status_mapping[st.selectbox("Are you suffering from Depression?", depression_status_options)],
        'Cognitive_Test_Scores': st.slider("What is your cognitive test score?", 0, 10, 5)
    }
    submitted = st.form_submit_button("Submit")

if submitted:
    prediction = predict(user_input)
    result = "You have Dementia" if prediction == 1 else "You don't have Dementia"

    st.markdown('<h3 class="subheading">Prediction Result</h3>', unsafe_allow_html=True)
    if prediction == 1:
        st.error(result)
    else:
        st.success(result)