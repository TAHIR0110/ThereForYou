import detect
import cv2

import mediapipe as mp


if __name__ == '__main__':
    vid = cv2.VideoCapture(0)
    _, frame = vid.read()
    h, w, _ = frame.shape

    face_detection = mp.solutions.face_detection.FaceDetection()

    mphands = mp.solutions.hands
    hands = mphands.Hands()

    while vid.isOpened():
        _, frame = vid.read()
        frame = cv2.flip(frame, 1)

        # Face
        face_results = face_detection.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if face_results.detections:
            for detection in face_results.detections:
                face_data = detection.location_data
                box_data = face_data.relative_bounding_box
                x = round(box_data.xmin * w)
                y = round(box_data.ymin * h)
                wi = round(box_data.width * w)
                he = round(box_data.height * h)

                cv2.rectangle(frame, (x, y), (x + wi, y + he), (0, 255, 0), 2)
        
        # Hands
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
        
        # Rope
        boxes = detect.main(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), (w, h))
        for b in boxes:
            for box in b:
                if box.any():
                    _x, _y, _w, _h = box
                    x1 = round(_x * w)
                    y1 = round(_y * h)
                    wo = round(_w * w)
                    ho = round(_h * h)

                cv2.rectangle(frame, (x1, y1), (x1 + wo, y1 + ho), (255, 0, 0), 2)

        cv2.imshow('Cam', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'): break # Exit when 'q' is pressed
        if cv2.waitKey(1) == 27: break # Exit when 'ESC' is pressed
        if cv2.getWindowProperty('Cam', cv2.WND_PROP_VISIBLE) < 1: break # Exit when window is closed