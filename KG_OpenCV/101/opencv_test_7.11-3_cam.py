# ⭐️ 문제 3
# [HSV 채널 분리 실시간 출력]

# ✅ 조건:

# 실시간으로 입력되는 프레임을 HSV 변환

# H, S, V 채널 분리

# 각 채널을 개별 흑백 이미지로 출력

# ✅ 목표 함수:

# cv2.split()

import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480)


while True:
    
    ref, frame = capture.read()

    cv2.imshow('test', frame)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    cv2.imshow('h', h)
    cv2.imshow('s', s)
    cv2.imshow('v', v)

    if cv2.waitKey(1) & 0xff == 27:
        capture.release()
        cv2.destroyAllWindows()
        break