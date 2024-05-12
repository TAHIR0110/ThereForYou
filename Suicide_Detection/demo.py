import detect
import cv2


if __name__ == '__main__':
    vid = cv2.VideoCapture(0)
    vid.set(3, 640)
    vid.set(4, 640)

    _, frame = vid.read()
    h, w, _ = frame.shape

    while vid.isOpened():
        _, frame = vid.read()
        frame = cv2.flip(frame, 1)

        # Face
        face_box = detect.face_detection(frame, w, h)
        
        # Hands
        hands_box = detect.hand_detection(frame, w, h)
        
        # Rope
        rope_box = detect.rope_detection(frame, (w, h))

        # Add text
        txt = detect.suicide_prevention(rope_box, face_box, hands_box)
        cv2.putText(frame, txt, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1, cv2.LINE_AA)

        cv2.imshow('Cam', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'): break # Exit when 'q' is pressed
        if cv2.waitKey(1) == 27: break # Exit when 'ESC' is pressed
        if cv2.getWindowProperty('Cam', cv2.WND_PROP_VISIBLE) < 1: break # Exit when window is closed