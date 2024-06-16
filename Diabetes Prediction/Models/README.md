# Diabetes Prediction :

### Goal:
This Project helps us to build  a model which helps us to predict if have is diabetic or not.
Diabetes is a chronic medical condition that occurs when the body is unable to properly regulate blood sugar (glucose) levels.

## Dataset

Content: The datasets consists of several medical predictor variables and one target variable, Outcome. Predictor variables includes the number of pregnancies the patient has had, their BMI, insulin level, age, and so on.

### About  model: 
What I have used in the model:

#### Dense;-
- Dense Layer is simple layer of neurons in which each neuron receives input from all the neurons of previous layer, thus called as dense. Dense Layer is used to classify image based on output from convolutional layers. Working of single neuron.

#### Activation Function:-
- Relu: ReLU, or Rectified Linear Unit, is an activation function commonly used in artificial neural networks, particularly in deep learning models.

- Softmax: The softmax function is a mathematical function commonly used in machine learning, particularly in classification tasks. It converts a vector of numbers into a probability distribution, effectively highlighting the most likely class while suppressing less likely ones.

#### Optimizers:-
- Adam:- Adam (Adaptive Moment Estimation) is an optimization algorithm used in training deep learning models. It combines the advantages of two other popular optimization techniques: AdaGrad and RMSProp, providing an efficient and effective method for training deep neural networks.


## What I have done!
- Load CSV file into DataFrame.
- Get DataFrame's dimensions (rows, columns).
- computes pairwise correlation of columns, excluding NA/null values. 
- create a heatmap of the correlation matrix corr with annotations.
- created an instance of the StandardScaler class from the sklearn.preprocessing module. 
- transform the data in x to a standardized form.
- created a grid of pairwise plots of the variables in the DataFrame data
- Logistic Regression classifier from scikit-learn was used to classify the data.
- Support Vector Machine classifier from scikit-learn was used  to classify the data.
- Dense layers were  added for the classification.
- Activation function Relu and softmax is used to improve acccuracy.
- Optimizer Adam is used to reduce loss.
- Displayed summary of the model created .
- Trained the Model



## Conclusion:-
This study focuses on the development and evaluation of a diabetes prediction model using machine learning techniques. The model was trained on a dataset consisting of various features such as age, BMI, glucose levels, and insulin levels, among others, to predict the likelihood of an individual having diabetes.




