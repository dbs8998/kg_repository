# ⭐⭐⭐ 문제 4
# [특정 색상 범위로 마스크 생성 (실시간)]

# ✅ 조건:

# HSV 변환한 카메라 프레임에서

# 특정 색상 범위 (H_min ~ H_max, S_min ~ S_max, V_min ~ V_max)를 지정

# cv2.inRange()로 마스크 생성

# 마스크 실시간 출력

# ✅ 목표 함수:

# cv2.inRange()

import cv2
import numpy as np

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 680)

while True:

    ref, falme = capture.read()

    hsv = cv2.cvtColor(falme, cv2.COLOR_BGR2HSV)

    low = np.array((10,10,10))
    upper = np.array((170,255,255))

    mask = cv2.inRange(hsv, low, upper)

    cv2.imshow('hsv',hsv)
    cv2.imshow('mask',mask)

    if cv2.waitKey(1) & 0xff == 27:
        capture.release()
        cv2.destroyAllWindows()
        break