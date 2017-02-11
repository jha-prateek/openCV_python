import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cv2.namedWindow('Vid')

def nothing(x):
    pass

cv2.createTrackbar('H','Vid',0,180,nothing)
cv2.createTrackbar('S','Vid',0,255,nothing)
cv2.createTrackbar('V','Vid',0,255,nothing)

while (1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h = cv2.getTrackbarPos('H','Vid')
    s = cv2.getTrackbarPos('S', 'Vid')
    v = cv2.getTrackbarPos('V', 'Vid')

    lower_yellow = np.array([h,s,v])
    upper_yellow = np.array([180,255,255])

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    res = cv2.bitwise_and(frame, frame, mask= mask)

    cv2.imshow('Vid',res)
    cv2.imshow('mask', mask)

    k = cv2.waitKey(5) & 0xFF
    if k==27:
        break

cv2.destroyAllWindows()
cap.release()