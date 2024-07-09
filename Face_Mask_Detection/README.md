# Face Mask Detection

## Overview
This project uses a Convolutional Neural Network (CNN) to detect whether a person is wearing a face mask or not. The model is trained on a dataset containing images of people with and without face masks.

## Dataset
The dataset is divided into two folders:
- `with_mask`: Images of people wearing face masks.
- `without_mask`: Images of people without face masks.
- download images from https://github.com/chandrikadeb7/Face-Mask-Detection/tree/master/dataset 

## Model Architecture
The model consists of the following layers:
- Convolutional layers with ReLU activation and MaxPooling
- Flatten layer
- Fully connected Dense layers with Dropout
- Output layer with Softmax activation

## Training
The dataset is split into 75% training and 25% testing sets. The model is trained for 10 epochs with a batch size of 32.

## Results
The model achieves good accuracy in detecting face masks, as shown in the classification report and accuracy score.

## Usage
To train the model and make predictions, run the provided script. The trained model will be saved as `face_mask_detection_model.h5`.

## Requirements
- numpy
- opencv-python
- tensorflow
- keras
- matplotlib
- scikit-learn

## How to Run
1. Ensure you have the required libraries installed.
2. Run the script to download the dataset, train the model, and make predictions.

## Display Predictions
The script includes a function to display test images along with their predicted labels, indicating whether the person is wearing a mask or not.
