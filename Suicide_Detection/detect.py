from ultralytics import YOLO
from pathlib import Path

import cv2


def load_model():
    '''Loads the YOLO model for detection'''

    model_path = Path(__file__).resolve().parent / 'Model/Model_Data/logs/runs/detect/SuicideDetection/weights/best.pt'

    model = YOLO(model_path)
    return model


def detect(model, image, image_size):
    '''Detects objects in the image'''

    results = model.predict(
        source=image,
        verbose=False,
        imgsz=image_size,
        conf=0.5,
        iou=0.7,
        save=False,
        save_txt=False,
        show_conf=False,
        show_labels=False,
        show_boxes=False
    )

    return results


def main(image, image_size):
    '''Processed output for the detection'''


    model = load_model()
    results = detect(model, image, image_size)

    boxes = [r.boxes.cpu().numpy().xywhn for r in results]

    return boxes