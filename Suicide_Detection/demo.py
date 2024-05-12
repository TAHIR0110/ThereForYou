import detect
import cv2

import mediapipe as mp


if __name__ == '__main__':
    vid = cv2.VideoCapture(0)
    _, frame = vid.read()
    h, w, _ = frame.shape

    face_detection = mp.solutions.face_detection.FaceDetection()

    while vid.isOpened():
        _, frame = vid.read()
        frame = cv2.flip(frame, 1)

        results = face_detection.process(frame)
        if results.detections:
            for detection in results.detections:
                face_data = detection.location_data
                box_data = face_data.relative_bounding_box
                x = round(box_data.xmin * w)
                y = round(box_data.ymin * h)
                wi = round(box_data.width * w)
                he = round(box_data.height * h)

                cv2.rectangle(frame, (x, y), (x + wi, y + he), (0, 255, 0), 2)

        cv2.imshow('Cam', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'): break
        if cv2.waitKey(1) == 27: break
        if cv2.getWindowProperty('Cam', cv2.WND_PROP_VISIBLE) < 1: break