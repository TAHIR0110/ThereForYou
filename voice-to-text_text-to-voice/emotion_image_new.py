import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing import image


def essential():

    model = load_model("gender_model_toh_hai.h5")

    def preprocess_image(img_path):
        img = image.load_img(img_path, target_size=(150, 150))
        img = image.img_to_array(img)
        img = img / 255.0
        img = np.expand_dims(img, axis=0)
        return img

    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Error: Could not open camera.")
        exit()

    return_value, img = camera.read()
    if not return_value:
        print("Error: Could not capture image.")
        camera.release()
        exit()

    cv2.imwrite("captured_image.jpg", img)

    camera.release()

    img = preprocess_image("captured_image.jpg")

    prediction = model.predict(img)

    threshold = 0.5
    if prediction > threshold:
        return "Female"
    if prediction < threshold:
        return "Male"
