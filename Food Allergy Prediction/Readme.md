# Food Allergy Prediction

This project aims to predict food allergies based on various features using a Neural Network model built with TensorFlow and Keras. The model is wrapped in a custom class to enable hyperparameter tuning using `GridSearchCV` from `scikit-learn`.

## Table of Contents
- [Overview](#overview)
- [Data Preprocessing](#data-preprocessing)
- [Model Building](#model-building)
- [Hyperparameter Tuning](#hyperparameter-tuning)
- [Evaluation](#evaluation)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)

## Overview
Food allergies are an increasing concern worldwide. This project uses a dataset containing various features related to food allergies and builds a neural network to predict whether an individual has a food allergy.

## Data Preprocessing
1. **Loading the Data**: The data is loaded from a CSV file.
2. **One-Hot Encoding**: Categorical features, such as 'Gender', are encoded using one-hot encoding.
3. **Feature Scaling**: Numerical features are scaled using `StandardScaler`.

## Model Building
The neural network model is built using TensorFlow and Keras. The model consists of:
- An input layer with 64 neurons and ReLU activation.
- A hidden layer with 32 neurons and ReLU activation.
- An output layer with 1 neuron and sigmoid activation.

## Hyperparameter Tuning
A custom wrapper class `KerasModelWrapper` is created to allow the use of `GridSearchCV` for hyperparameter tuning. The following hyperparameters are tuned:
- `optimizer`: Optimizer to use (`adam`, `rmsprop`).
- `batch_size`: Batch size for training (10, 20, 30).
- `epochs`: Number of epochs for training (50, 100).

## Evaluation
The model is evaluated using accuracy, confusion matrix, and ROC-AUC score.

## Installation
To run this project, you need to have Python installed along with the following libraries:
- pandas
- numpy
- tensorflow (version 2.15.0)
- scikit-learn
- matplotlib
- seaborn

You can install these dependencies using pip:
```bash
pip install pandas numpy tensorflow scikit-learn matplotlib seaborn
```

## Usage
1. **Upload the Data**: Upload the CSV file containing the food allergy data.
2. **Run the Script**: Execute the script to preprocess the data, build the model, perform hyperparameter tuning, and evaluate the results.

## Results
The best model achieved an accuracy of approximately 98%. The confusion matrix and classification report provide further details on the model's performance. The ROC curve and AUC score demonstrate the model's ability to distinguish between classes.
