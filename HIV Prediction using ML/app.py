import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the trained model
model = joblib.load('xgboost_HIV_model.pkl')

# Function to perform label encoding on categorical variables
def label_encode(input_data):
    label_encoders = {}
    categorical_columns = ['marital_status', 'std', 'educational_background', 'hiv_test_in_past_year', 'aids_education',
                           'places_of_seeking_sex_partners', 'sexual_orientation', 'drug-_taking',
                           'Before_marriage_awareness']

    for col in categorical_columns:
        label_encoders[col] = LabelEncoder()
        input_data[col] = label_encoders[col].fit_transform(input_data[col])

    return input_data

# Function to make predictions
def predict_hiv(age, marital_status, std, educational_background, hiv_test_in_past_year, aids_education,
                places_of_seeking_sex_partners, sexual_orientation, drug_taking, before_marriage_awareness):
    # Create a DataFrame from the inputs
    input_data = pd.DataFrame({
        'age': [age],
        'marital_status': [marital_status],
        'std': [std],
        'educational_background': [educational_background],
        'hiv_test_in_past_year': [hiv_test_in_past_year],
        'aids_education': [aids_education],
        'places_of_seeking_sex_partners': [places_of_seeking_sex_partners],
        'sexual_orientation': [sexual_orientation],
        'drug-_taking': [drug_taking],
        'Before_marriage_awareness': [before_marriage_awareness]
    })

    # Label encode the input data
    input_data = label_encode(input_data)

    # Make prediction
    prediction = model.predict(input_data)
    return prediction[0]

# Add custom CSS
st.markdown(
    """
    <style>
    body {
        background-color: #222;
        color: #fff;
        font-family: 'Roboto', sans-serif;
    }

    .main {
        padding: 20px 40px;
        background-color: #333;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }

    h2 {
        margin-bottom: 20px;
        text-align: center;
        color: #f0f0f0;
    }

    .stSlider {
        margin-bottom: 20px;
    }

    .stSelectbox {
        margin-bottom: 20px;
    }

    .stButton {
        margin-top: 20px;
        text-align: center;
    }

    .stButton button {
        font-size: 18px;
        font-weight: bold;
        background-color: #4CAF50;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
    }

    .stAlert {
        margin-top: 20px;
        font-size: 18px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h2 style='text-align: center; color: red; font-weight: bold;'>HIV Disease Prediction</h2>",
            unsafe_allow_html=True)

# Inputs
age = st.slider('Age', 0, 150, 40)
marital_status = st.selectbox('Marital Status', ['Unmarried', 'Married', 'Widowed', 'Divorced', 'Others'])
std = st.selectbox('STD', ['No', 'Yes'])
educational_background = st.selectbox('Educational Background',
                                      ['Graduate', '12th pass', '10th pass', 'Illiterate', 'Others'])
hiv_test_in_past_year = st.selectbox('HIV Test in Past Year', ['Yes', 'No'])
aids_education = st.selectbox('AIDS Education', ['No', 'Yes'])
places_of_seeking_sex_partners = st.selectbox('Places of Seeking Sex Partners',
                                              ['Bar', 'Others', 'Park', 'Internet', 'Public bath'])
sexual_orientation = st.selectbox('Sexual Orientation', ['Heterosexual', 'Bisexual', 'Homosexual'])
drug_taking = st.selectbox('Drug Taking', ['Yes', 'No'])
before_marriage_awareness = st.selectbox('Before Marriage Awareness', ['No', 'Yes'])

# Prediction
if st.button('Predict'):
    result = predict_hiv(age, marital_status, std, educational_background, hiv_test_in_past_year, aids_education,
                         places_of_seeking_sex_partners, sexual_orientation, drug_taking, before_marriage_awareness)

    if result == 1:
        st.error('HIV Report: **Negative**')
    else:
        st.success('HIV Report: **Positive**')
