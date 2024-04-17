import cv2
import numpy as np
from keras.models import load_model

gender_dict = {0:'Male', 1:'Female'}

def preprocess_frame(frame):
    return cv2.resize(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), (128, 128)).astype('float32') / 255.0

def predict_gender_age(frame, model):
    pred = model.predict(frame.reshape(1, 128, 128, 1))
    return gender_dict[round(pred[0][0][0])], round(pred[1][0][0])

model = load_model('my_model.h5')
cap = cv2.VideoCapture(0)

ret, frame = cap.read()

cap.release()

def essential():

    pred_gender, pred_age = predict_gender_age(preprocess_frame(frame), model)

    return pred_gender

print(essential())