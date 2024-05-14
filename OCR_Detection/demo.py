import cv2
import detect


if __name__ == '__main__':
    vid = cv2.VideoCapture(0)

    while True:
        _, frame = vid.read()

        image_data = detect.detect_text(frame)
        detected_text = detect.process_data(frame, image_data)

        cv2.putText(frame, detected_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

        cv2.imshow('Cam', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'): break # Exit when 'q' is pressed
        if cv2.waitKey(1) == 27: break # Exit when 'ESC' is pressed
        if cv2.getWindowProperty('Cam', cv2.WND_PROP_VISIBLE) < 1: break # Exit when window is closed