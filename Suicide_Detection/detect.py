from ultralytics import YOLO
from pathlib import Path
from ultralytics.utils.plotting import Annotator

import cv2

import mediapipe as mp


_face_detection = mp.solutions.face_detection.FaceDetection()

mphands = mp.solutions.hands
hands = mphands.Hands()


def load_model():
    '''Loads the YOLO model for detection'''

    model_path = Path(__file__).resolve().parent / 'Model/Model_Data/logs/runs/detect/SuicideDetection2/weights/best.pt'

    model = YOLO(model_path)
    return model


def detect(model, frame, frame_size):
    '''Detects objects in the image'''

    results = model.predict(
        source=frame,
        verbose=False,
        imgsz=frame_size,
        conf=0.4,
        iou=0.7,
        save=False,
        save_txt=False,
        show_conf=False,
        show_labels=False,
        show_boxes=True
    )

    return results


def face_detection(frame, w, h):
    '''Detection for face detection'''

    global _face_detection

    face_results = _face_detection.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    if face_results.detections:
        for detection in face_results.detections:
            face_data = detection.location_data
            box_data = face_data.relative_bounding_box
            x = round(box_data.xmin * w)
            y = round(box_data.ymin * h)
            wi = round(box_data.width * w)
            he = round(box_data.height * h)

            cv2.rectangle(frame, (x, y), (x + wi, y + he), (0, 255, 0), 2)


def hand_detection(frame, w, h):
    '''Detection for hand detection'''

    global hands

    hands_results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    hand_landmarks = hands_results.multi_hand_landmarks

    if hand_landmarks:
        for handLMs in hand_landmarks:
            if handLMs:
                x1 = round(min([val.x for val in handLMs.landmark]) * w)
                y1 = round(min([val.y for val in handLMs.landmark]) * h)
                x2 = round(max([val.x for val in handLMs.landmark]) * w)
                y2 = round(max([val.y for val in handLMs.landmark]) * h)

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), 2)


def rope_detection(frame, frame_size):
    '''Processed output for the detection'''


    model = load_model()
    results = detect(model, frame, frame_size)

    for r in results:
        annotator = Annotator(frame)

        boxes = r.boxes

        for box in boxes:
            b = box.xyxy[0]
            c = box.cls
            annotator.box_label(b)
        
    annotator.result()