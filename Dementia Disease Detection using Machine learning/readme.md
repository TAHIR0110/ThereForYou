# Dementia Disease Detection using Machine Learning

The Dementia Prediction App is a user-friendly web application built with Streamlit that predicts the likelihood of dementia based on health and lifestyle inputs. It uses a pre-trained Logistic Regression model to analyze features such as age, blood oxygen level, body temperature, weight, education level, family history, smoking status, cognitive test scores, and more. Users input their data through an intuitive form, and the app provides real-time predictions with clear results indicating whether the user is likely to have dementia. The app features a visually appealing interface with custom CSS styles for an enhanced user experience. Installation is straightforward, requiring cloning the repository, setting up a virtual environment, installing dependencies, and running the app. Contributions to the project are welcome, and future enhancements include adding more features, user authentication, integrating health APIs, and improved visualizations.


**Model Training and evaluation**: 
     The four machine learning model random forest ,KNN , Naive Bayes , Logistic Regression are selected for model training over the inputed processed data:

 **Inference**: 
      Deployed the model with the help streamlit web application to predict the  Dementia report for the user (Having Dementia or Not)

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

4. **View Results**: The script will allow you to predict Whether the person is suffering from Dementia or not.

**DEMO** :

https://github.com/user-attachments/assets/88ca9ba4-96db-4612-8320-e80d09b26087



