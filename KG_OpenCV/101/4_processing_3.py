# https://opencv-python.readthedocs.io/en/latest/doc/08.imageProcessing/imageProcessing.html
# 이미지 프로세싱: BGR->HSV -> 이진화 -> 마스크 -> 특정 색만 남기고 모두 검정색 -> 파랑 Object Tracing!!

import cv2
import numpy as np

cap = cv2.VideoCapture(0)  #0 = 기본 카메라
cap.set(3, 320)    # 웹캠의 너비
cap.set(4, 240)    # 웹캠의 높이

while(1):
    ret, frame = cap.read()  # 현재 프레임 읽기

    if ret:
        #BGR -> HSV (HSV는 색상 강조. 즉,색 추출에 유리함)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # 어두운 ~ 밝은 blue 영역 상한/하한
        lower_blue = np.array([110, 50, 50])
        upper_blue = np.array([130, 255, 255])

        # 이미지에서 blue 영역
        mask1 = cv2.inRange(hsv, lower_blue, upper_blue)

        # bit 연산자를 통해 blue 영역만 흰색 남김(나머지 검정)
        res = cv2.bitwise_and(frame, frame, mask = mask1)
        
        cv2.imshow('frame', frame)
        cv2.imshow("HSV", hsv)
        cv2.imshow('Mask', mask1)
        cv2.imshow('Result', res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
