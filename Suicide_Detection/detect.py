from pathlib import Path

import cv2
import mediapipe as mp
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator

_face_detection = mp.solutions.face_detection.FaceDetection()

mphands = mp.solutions.hands
hands = mphands.Hands()


def load_model():
    """Loads the YOLO model for detection"""

    model_path = (
        Path(__file__).resolve().parent
        / "Model/Model_Data/logs/runs/detect/SuicideDetection2/weights/best.pt"
    )

    model = YOLO(model_path)
    return model


def detect(model, frame, frame_size):
    """Detects objects in the image"""

    results = model.predict(
        source=frame,
        verbose=False,
        imgsz=frame_size,
        conf=0.6,
        iou=0.7,
        save=False,
        save_txt=False,
        show_conf=False,
        show_labels=False,
        show_boxes=True,
        stream=True,
    )

    return results


def face_detection(frame, w, h):
    """Detection for face detection"""

    global _face_detection

    box_list = []

    face_results = _face_detection.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    if face_results.detections:
        for detection in face_results.detections:
            face_data = detection.location_data
            box_data = face_data.relative_bounding_box
            x = round(box_data.xmin * w)
            y = round(box_data.ymin * h)
            wi = round(box_data.width * w)
            he = round(box_data.height * h)

            box_list.append((x, y, wi, he))

            cv2.rectangle(frame, (x, y), (x + wi, y + he), (0, 255, 0), 2)

    return box_list


def hand_detection(frame, w, h):
    """Detection for hand detection"""

    global hands

    box_list = []

    hands_results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    hand_landmarks = hands_results.multi_hand_landmarks

    if hand_landmarks:
        for handLMs in hand_landmarks:
            if handLMs:
                x1 = round(min([val.x for val in handLMs.landmark]) * w)
                y1 = round(min([val.y for val in handLMs.landmark]) * h)
                x2 = round(max([val.x for val in handLMs.landmark]) * w)
                y2 = round(max([val.y for val in handLMs.landmark]) * h)

                box_list.append((x1, y1, x2, y2))

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), 2)

    return box_list


def rope_detection(frame, frame_size):
    """Processed output for the detection"""

    model = load_model()
    results = detect(model, frame, frame_size)

    box_list = []

    for r in results:
        annotator = Annotator(frame)

        boxes = r.boxes

        for box in boxes:
            b = box.xyxy[0]
            annotator.box_label(b)

        box_list.append(boxes.xyxy.tolist())

    annotator.result()

    return box_list


def suicide_prevention(rope_box, face_box, hands_box):
    """Return a string specifying the detected condition of threat"""

    txt = "None"

    # Condition 1: Warning
    if rope_box and face_box:
        for boxes in rope_box:
            for box in boxes:
                x1, y1, x2, y2 = box

                for face in face_box:
                    fy, fh = face[1], face[3]
                    if y2 < fy:
                        txt = "Warning: Face detected below rope area"

                        # Condition 2: Danger
                        if hands_box:
                            for hand in hands_box:
                                hx1, hy1, hx2, hy2 = hand

                                if y1 < hy1 < y2:
                                    return "Danger: Face below rope area and hand near rope area detected"

                        return txt
                    # Condition 3: Critical Danger
                    elif y1 < fy + fh:
                        return "Critical Danger: Face detected near rope area"

    return txt
