import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd

# Load the trained model
model = load_model('cataract_detection_model.h5')

# Define the image size expected by the model
IMG_SIZE = (224, 224)  # Change this to match your model's input size

# Function to preprocess the image
def preprocess_image(image):
    image = image.resize(IMG_SIZE)
    image = img_to_array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# Function to make a prediction
def predict(image):
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    return 'Cataract' if prediction[0] > 0.5 else 'Normal'

# Function to fetch cataract stats
def fetch_cataract_stats():
    stats = {
        "Global Prevalence": "51% of global blindness",
        "Leading Cause": "Leading cause of blindness worldwide",
        "Treatable": "Cataract is treatable with surgery"
    }
    return stats

# Function to fetch cataract remedies
def fetch_cataract_remedies():
    remedies = [
        "Surgical removal of the cataract",
        "Wearing sunglasses to reduce glare",
        "Using magnifying lenses for reading",
        "Improving lighting in your home"
    ]
    return remedies

# Function to fetch cataract risks
def fetch_cataract_risks():
    risks = [
        "Aging",
        "Diabetes",
        "Excessive exposure to sunlight",
        "Smoking",
        "Obesity",
        "High blood pressure",
        "Previous eye injury or inflammation"
    ]
    return risks

# Function to plot stats about cataracts
def plot_cataract_stats():
    labels = ['Cataract', 'Other Causes']
    sizes = [51, 49]
    colors = ['#ff9999','#66b3ff']
    explode = (0.1, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=140)

    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)

# Function to fetch cataract symptoms
def fetch_cataract_symptoms():
    symptoms = [
        "Clouded, blurred or dim vision",
        "Increasing difficulty with vision at night",
        "Sensitivity to light and glare",
        "Seeing 'halos' around lights",
        "Frequent changes in eyeglass or contact lens prescription",
        "Fading or yellowing of colors",
        "Double vision in a single eye"
    ]
    return symptoms

# Streamlit app
st.markdown(
    """
    <style>
    .centered-heading {
        font-size: 2.5rem;
        color: blue;
        text-align: center;
        font-weight: bold;
    }
    .subheading {
        font-size: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="centered-heading">Cataract Detection</h1>', unsafe_allow_html=True)

# Image upload section
st.markdown('<h2 class="subheading">Upload an Image</h2>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("Classifying...")
    label = predict(image)
    if label == 'Cataract':
        st.error(f'Prediction: {label}')
    else:
        st.success(f'Prediction: {label}')

    # Display cataract statistics
    st.markdown('<h2 class="subheading">Cataract Statistics</h2>', unsafe_allow_html=True)
    stats = fetch_cataract_stats()
    st.write(stats)
    plot_cataract_stats()

    # Display cataract remedies
    st.markdown('<h2 class="subheading">Cataract Remedies</h2>', unsafe_allow_html=True)
    remedies = fetch_cataract_remedies()
    st.write(remedies)

    # Display cataract risks
    st.markdown('<h2 class="subheading">Cataract Risks</h2>', unsafe_allow_html=True)
    risks = fetch_cataract_risks()
    st.write(risks)

    # Display cataract symptoms in tabular form
    st.markdown('<h2 class="subheading">Cataract Symptoms</h2>', unsafe_allow_html=True)
    symptoms = fetch_cataract_symptoms()
    symptoms_df = pd.DataFrame(symptoms, columns=["Symptoms"])
    st.table(symptoms_df)

# Display nearby eye clinics using an embedded Google Maps link
st.markdown('<h2 class="subheading">Nearby Eye Clinics</h2>', unsafe_allow_html=True)
st.write("View eye clinics in Pune on Google Maps:")
st.components.v1.iframe("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3783.197742711061!2d73.83969451542263!3d18.520430787407185!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2c07df1d121c1%3A0x562b1c8f58f3728b!2sPune%2C%20India!5e0!3m2!1sen!2sus!4v1654594546546!5m2!1sen!2sus", width=600, height=450)

city = st.text_input('Enter your city')
if st.button('Submit'):
    map_url = f"https://www.google.com/maps/search/eye+clinics+in+{city}"
    st.write(f"Redirecting to eye clinics in {city} on Google Maps...")
    st.markdown(f'<meta http-equiv="refresh" content="0; url={map_url}">', unsafe_allow_html=True)
