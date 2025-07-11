# ⭐⭐⭐ 문제 5
# [트랙바로 색상 범위 실시간 조정]

# ✅ 조건:

# OpenCV 트랙바로 HSV의 min/max 값을 조정 가능

# 사용자가 트랙바를 움직이면 → 마스크가 실시간으로 업데이트

# 트랙바 UI 구현

# ✅ 목표 함수:

# cv2.createTrackbar()

# cv2.getTrackbarPos()


import cv2
import numpy as np

def do_nothing(x):
  pass

cat =  cv2.VideoCapture(0)
cat.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cat.set(cv2.CAP_PROP_FRAME_HEIGHT, 680)

cv2.namedWindow("HSV", cv2.WINDOW_NORMAL)

cv2.createTrackbar("h_low", "HSV", 0, 179, do_nothing)
cv2.createTrackbar("s_low", "HSV", 0, 255, do_nothing)
cv2.createTrackbar("v_low", "HSV", 10, 255, do_nothing)
cv2.createTrackbar("h_high", "HSV", 150, 179, do_nothing)
cv2.createTrackbar("s_high", "HSV", 250, 255, do_nothing)
cv2.createTrackbar("v_high", "HSV", 250, 255, do_nothing)


while True:
    ref, frame = cat.read()

    # 트랙바로 조정한 값 가져오기
    h_low = cv2.getTrackbarPos("h_low", "HSV")
    s_low = cv2.getTrackbarPos("s_low", "HSV")
    v_low = cv2.getTrackbarPos("v_low", "HSV")
    h_high = cv2.getTrackbarPos("h_high", "HSV")
    s_high = cv2.getTrackbarPos("s_high", "HSV")
    v_high = cv2.getTrackbarPos("v_high", "HSV")

    lows = np.array((h_low, s_low, v_low))
    highs = np.array((h_high, s_high, v_high))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lows, highs)


    

    result = cv2.bitwise_or(frame,frame, mask)
    cv2.imshow('mask',mask)
    cv2.imshow('HSV', result)


    if cv2.waitKey(1) & 0xff==27:
        cat.release()
        cv2.destroyAllWindows()
        break



