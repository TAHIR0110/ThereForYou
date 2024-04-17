import cv2
import numpy as np
from keras.models import load_model

def essen():
    model = load_model("choking_detection_model_augmented71.h5")

    def preprocess_frame(frame):
        resized_frame = cv2.resize(frame, (128, 128))
        normalized_frame = resized_frame / 255.0
        expanded_frame = np.expand_dims(normalized_frame, axis=0)
        return expanded_frame

    def predict_frame(frame):
        preprocessed_frame = preprocess_frame(frame)
        prediction = model.predict(preprocessed_frame)
        return prediction

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        prediction = predict_frame(frame)

        if prediction[0][0] > 0.5: 
            return "choking"

    cap.release()
