#  HIV Syndrome Prediction using Machine learning

This project aims to develop a web application for predicting HIV disease status using a machine learning model. The application leverages the powerful XGBoost algorithm, which has been pre-trained to analyze a variety of health-related and behavioral inputs to determine the likelihood of an individual being HIV positive. The inputs include factors such as age, marital status, history of sexually transmitted diseases (STDs), educational background, HIV testing history, AIDS education, places of seeking sex partners, sexual orientation, drug-taking habits, and awareness before marriage.

The application is built using Streamlit, a popular framework for creating interactive web applications in Python. The user interface is designed to be both functional and visually appealing, featuring stylish fonts, custom CSS for enhanced aesthetics, and relevant images to provide an engaging experience. Users can input their data through sliders and select boxes, ensuring an intuitive and user-friendly interaction.

One of the standout features of the application is the dynamic and responsive design. The app includes a background image related to HIV/AIDS awareness, adding context and visual depth. Additionally, a moving HIV ribbon image is positioned in the corner, symbolizing the cause and drawing attention to the importance of awareness and education. The input and output sections are enclosed in stylish containers with shadows and rounded borders, enhancing readability and focus.

The model's prediction process involves label encoding categorical variables to convert them into numerical format suitable for the model. Upon clicking the 'Predict' button, the app processes the input data, applies the XGBoost model, and displays the prediction result. If the model predicts a positive HIV status, a highlighted error message is shown; otherwise, a success message indicates a negative result.

This project not only demonstrates the practical application of machine learning in healthcare but also highlights the importance of accessible tools for early detection and awareness. By providing a seamless and informative user experience, the application aims to contribute to the ongoing efforts in HIV prevention and education. The integration of relevant imagery and user-friendly design principles ensures that the tool is not only functional but also engaging and supportive of the overall mission to combat HIV/AIDS.



 **Model Training and evaluation**: 
     The four machine learning model random forest ,XGBoost , Naive Bayes , Logistic Regression are selected for model training over the inputed processed data:

 **Inference**: 
      Deployed the model with the help streamlit web application to predict the HIV report for the user (positive or negative).


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

4. **View Results**: The script will allow you to predict Whether the person is sufferinf from HIV/AIDS or not.

**DEMO** :


https://github.com/user-attachments/assets/60aa2300-f166-46fe-825d-23d969ffd6d0



