import cv2
import detect


def mse(img1, img2):
    '''
    Calculates the Mean Squared Error between two images. In short, the lower the value, the more similar the images are.

    Args:
        img1: The first image.
        img2: The second image.
    
    Returns:
        mse: The mean squared error between the two images.
    '''

    h, w = img1.shape
    diff = cv2.subtract(img1, img2)
    err = np.sum(diff ** 2)
    mse = err / (float(h * w))

    return mse


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