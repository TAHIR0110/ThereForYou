from ultralytics import YOLO
from pathlib import Path

import cv2


def load_model():
    '''Loads the YOLO model for detection'''

    model_path = Path(__file__).resolve().parent / 'Model/Model_Data/logs/runs/detect/SuicideDetection/weights/best.pt'

    model = YOLO(model_path)
    return model


def detect(model, image):
    '''Detects objects in the image'''

    image = cv2.resize(image, (640, 640))

    results = model.predict(
        source=image,
        verbose=False,
        imgsz=(640, 640),
        conf=0.5,
        iou=0.7,
        save=False,
        save_txt=False,
        show_conf=False,
        show_labels=False,
        show_boxes=False
    )

    return results


def main(image):
    '''Processed output for the detection'''


    model = load_model()
    results = detect(model, image)

    boxes = [r.boxes.cpu().numpy().xywhn for r in results]

    return boxes