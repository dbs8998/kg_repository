# https://opencv-python.readthedocs.io/en/latest/doc/10.imageTransformation/imageTransformation.html
# Resizing

import cv2
import numpy as np

img = cv2.imread('101/Images/logo.png')

# 행(Height), 열(width)
height, width = img.shape[:2]

# 이미지 배율
shrink = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Custom Size 지정
custom1 = cv2.resize(img, (300, 500), interpolation=cv2.INTER_CUBIC)

custom2 = cv2.resize(img, (width*2, height*2), interpolation=cv2.INTER_CUBIC)

cv2.imshow("Source", img)
cv2.imshow('Shrink', shrink)
cv2.imshow('Custom1', custom1)
cv2.imshow('Custom2', custom2)

cv2.waitKey(0)
cv2.destroyAllWindows()