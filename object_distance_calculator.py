import cv2
import numpy as np

H = 0.05

def calibrate(img_path, D_cal):
    img = cv2.imread(img_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([99, 74, 76])
    upper_blue = np.array([119, 134, 136])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    c = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(c)

    f_px = (h * D_cal) / H
    print(f"f_px = {f_px:.2f} pixels")
    return f_px

def measure_distance(f_px):
    img=cv2.VideoCapture(0)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])
    while True:
        state, frame = img.read()
        if not state:
            break
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            area = cv2.contourArea(c)
            if area > 500:
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)
                D = (f_px * H) / h
                print(f"Estimated distance: {D:.2f} m")
        

        cv2.imshow("distance_measurement",frame)
        key=cv2.waitKey(1)
        if ord("q")==key:
            break

f_px = calibrate("openCV\caliberation_img.jpg", D_cal=0.3)
measure_distance(f_px)
cv2.destroyAllWindows()