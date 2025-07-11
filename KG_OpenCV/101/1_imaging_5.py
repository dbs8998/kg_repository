# https://opencv-python.readthedocs.io/en/latest/doc/07.imageArithmetic/imageArithmetic.html
# 이미지 연산: Trackbar로 이미지 더하기 2

import cv2
import numpy as np

img1 = cv2.imread('101/Images/flower1.jpg')
img2 = cv2.imread('101/Images/flower2.jpg')

def nothing(x):
    pass

cv2.namedWindow('Blender')
cv2.createTrackbar('W', 'Blender', 0, 100, nothing)
# Blender라는 창에 "W"라는 트랙바를 생성(0 ~ 100), 콜백함수=nothing

while True:
    # 슬라이더의 현재값을 pos에 대입
    pos = cv2.getTrackbarPos('W', 'Blender')

    # img1, img2에 대한 가중합
    w1 = pos / 100.0   # (0 ~ 100)/100
    w2 = 1.0 - w1
    dst = cv2.addWeighted(img1, w1, img2, w2, 0)

    cv2.imshow("Blender", dst)

    if cv2.waitKey(1) & 0xff == 27:
        break

cv2.destroyAllWindows()