import os
import numpy as np
from ultralytics import YOLO


# load the trained model
model = YOLO("/home/kyouma45/Documents/GitHub/ThereForYou/Gender_Classification/runs/classify/train/weights/best.pt")


def predict(img_path):
    #Predict with the model
    results = model(img_path)

    names=['Female','Male']
    resultsprobs = results[0].probs # Probs object for classification outputs
    return names[np.argmax(resultsprobs.data)]


#Running on Sample_Images:
print('face_0.jpg:',predict('Gender_Classification/Sample Images/face_0.jpg'))
print('face_1.jpg:',predict('Gender_Classification/Sample Images/face_1.jpg'))
print('face_2.jpg:',predict('Gender_Classification/Sample Images/face_2.jpg'))
print('face_3.jpg:',predict('Gender_Classification/Sample Images/face_3.jpg'))