import streamlit as st
import joblib
import pandas as pd

# Load the trained XGBoost model
model_xgb = joblib.load('xgb_model.pkl')

# Function to make predictions
def predict_risk_level(age, systolic_bp, diastolic_bp, bs, body_temp, heart_rate):
    # Create a DataFrame for the input data
    input_data = pd.DataFrame({
        'Age': [age],
        'SystolicBP': [systolic_bp],
        'DiastolicBP': [diastolic_bp],
        'BS': [bs],
        'BodyTemp': [body_temp],
        'HeartRate': [heart_rate]
    })

    # Predict using the loaded model
    prediction_proba = model_xgb.predict_proba(input_data)[0]

    # Determine risk level based on probability thresholds
    low_risk_threshold = 0.33
    mid_risk_threshold = 0.66

    if prediction_proba[2] > mid_risk_threshold:
        risk_level = 'High Maternal risk'
    elif prediction_proba[1] > low_risk_threshold:
        risk_level = 'Medium Maternal risk'
    else:
        risk_level = 'Low Maternal risk'

    return risk_level

# Streamlit app interface
st.set_page_config(page_title="Maternal Risk Prediction", page_icon=":baby:", layout="wide")

# Add a maternal-themed image as background with blur
st.markdown("""
    <style>
    .title {
        text-align: center;
        color: #FF6347;
        font-size: 36px;
        font-weight: bold;
        margin-top: 20px;
    }
    .subtitle {
        color: #4682B4;
        font-size: 28px;
        font-weight: bold;
    }
    .input-container {
        border: 2px solid #4682B4;
        border-radius: 10px;
        padding: 20px;
        background-color: rgba(240, 248, 255, 0.8); /* Semi-transparent background */
    }
    .output-container {
        border: 2px solid #4682B4;
        border-radius: 10px;
        padding: 20px;
        background-color: rgba(240, 248, 255, 0.8); /* Semi-transparent background */
    }
    .img-container {
        text-align: center;
        margin-bottom: 20px;
    }
    .img-container img {
        width: 100%;
        max-width: 1000px; /* Adjust max-width as needed */
        height: auto;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Background image
st.markdown("<div class='background'></div>", unsafe_allow_html=True)

# Main title
st.markdown("<div class='title'>Maternal Risk Prediction</div>", unsafe_allow_html=True)


# Input container with styling
with st.container():
    st.markdown("<div class='subtitle'>Enter the details below:</div>", unsafe_allow_html=True)

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            age = st.slider('Age', min_value=10, max_value=100, value=30, key='age')
            systolic_bp = st.slider('Systolic BP', min_value=70, max_value=200, value=120, key='systolic_bp')
            diastolic_bp = st.slider('Diastolic BP', min_value=50, max_value=120, value=80, key='diastolic_bp')
            bs = st.slider('Blood Sugar', min_value=5.0, max_value=20.0, value=7.0, format="%.1f", key='bs')

        with col2:
            body_temp = st.slider('Body Temperature (Fahrenheit)', min_value=95.0, max_value=105.0, value=98.6,
                                  format="%.1f", key='body_temp')
            heart_rate = st.slider('Heart Rate', min_value=50, max_value=150, value=80, key='heart_rate')

        st.markdown("<hr>", unsafe_allow_html=True)

        # Prediction button
        if st.button('Predict Risk Level'):
            risk_level = predict_risk_level(age, systolic_bp, diastolic_bp, bs, body_temp, heart_rate)

            # Display the prediction with proper styling
            with st.container():
                if risk_level == 'Low Maternal risk':
                    st.success(f'**Predicted Risk Level:** {risk_level.upper()}')
                elif risk_level == 'Medium Maternal risk':
                    st.warning(f'**Predicted Risk Level:** {risk_level.upper()}')
                elif risk_level == 'High Maternal risk':
                    st.error(f'**Predicted Risk Level:** {risk_level.upper()}')
