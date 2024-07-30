# Cataract Disease Detection using Machine Learning


## Model Training and evaluation :
 
CNN model is trained over batch size = 32 , input image size =(224,224) over 20 epocchs and achieved average validation accuracy of 87.5 %.

## Dataset :

https://www.kaggle.com/datasets/akshayramakrishnan28/cataract-classification-dataset/data


## Inference : 

Deployed the model with the help streamlit web application to predict the possibility of eye  cataract , cataract disease symptoms , risks , statistics , grpahs and nearby eye clinic search.

## Libraries Used

1. **Joblib**: For downloading the random forest model
2. **Scikit learn**: For machine learning processing  and operations
3. **Matplotlib**: For plotting and visualizing the detection results.
4. **Pandas**: For image manipulation.
5. **NumPy**: For efficient numerical operations.
6. **Seaborn** : for advanced data visualizations
7. **plotly** : for 3D data visualizations .
8. **Streamlit** : for creating gui of the web application.
9. **Tensorflow** : for image based manipulation operations.


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
    (download the model cataract_detection_model.h5 from below link and put in same directoy :
      https://drive.google.com/file/d/17Um-KcGOBz8G3s6s4nJj1lJ-C8BPT8rN/view?usp=sharing)

    ```python
    streamlit run app.py
    ```

4. **View Results**: The script will allow you to predict the possbility of cataract.

**DEMO** :

https://github.com/user-attachments/assets/0db9e7ca-48cd-4dc5-8bc9-c97c9fa766b1




