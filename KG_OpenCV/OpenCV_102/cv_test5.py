import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('Controls')

# HSV 각 채널 트랙바 생성
cv2.createTrackbar('H_min', 'Controls', 0, 179, nothing)
cv2.createTrackbar('H_max', 'Controls', 179, 179, nothing)
cv2.createTrackbar('S_min', 'Controls', 0, 255, nothing)
cv2.createTrackbar('S_max', 'Controls', 255, 255, nothing)
cv2.createTrackbar('V_min', 'Controls', 0, 255, nothing)
cv2.createTrackbar('V_max', 'Controls', 255, 255, nothing)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 트랙바 값 읽기
    h_min = cv2.getTrackbarPos('H_min', 'Controls')
    h_max = cv2.getTrackbarPos('H_max', 'Controls')
    s_min = cv2.getTrackbarPos('S_min', 'Controls')
    s_max = cv2.getTrackbarPos('S_max', 'Controls')
    v_min = cv2.getTrackbarPos('V_min', 'Controls')
    v_max = cv2.getTrackbarPos('V_max', 'Controls')

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Result', result)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
