import cv2
import numpy as np
import time

camera = cv2.VideoCapture(0)
time.sleep(3)

for _ in range(60):
    success, bg_frame = camera.read()
bg_frame = cv2.flip(bg_frame, 1)

while camera.isOpened():
    success, current_frame = camera.read()
    if not success:
        break

    current_frame = cv2.flip(current_frame, 1)

    hsv_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)

    green_lower = np.array([35, 40, 40])
    green_upper = np.array([85, 255, 255])

    green_mask = cv2.inRange(hsv_frame, green_lower, green_upper)

    kernel = np.ones((3, 3), np.uint8)
    green_mask = cv2.morphologyEx(green_mask, cv2.MORPH_OPEN, kernel, iterations=2)
    green_mask = cv2.dilate(green_mask, kernel, iterations=1)

    inverse_mask = cv2.bitwise_not(green_mask)

    background_part = cv2.bitwise_and(bg_frame, bg_frame, mask=green_mask)
    foreground_part = cv2.bitwise_and(current_frame, current_frame, mask=inverse_mask)

    output_frame = cv2.addWeighted(background_part, 1, foreground_part, 1, 0)

    cv2.imshow("Invisibility Effect", output_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

camera.release()
cv2.destroyAllWindows()
