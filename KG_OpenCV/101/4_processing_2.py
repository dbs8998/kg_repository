# https://opencv-python.readthedocs.io/en/latest/doc/08.imageProcessing/imageProcessing.html
# 이미지 Processing (BGR->GRAY, BGR->HSV 등 150여 변환 플래그가 있음)

import cv2
import numpy as np

img_original = cv2.imread("101/Images/flower1.jpg")
img_gray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray", img_gray)
cv2.imshow("Orig", img_original)
cv2.waitKey(0)
cv2.destroyAllWindows()
