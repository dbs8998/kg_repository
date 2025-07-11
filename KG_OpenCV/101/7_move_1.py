# https://opencv-python.readthedocs.io/en/latest/doc/10.imageTransformation/imageTransformation.html
# 틀 안에서 이미지 이동

import cv2
import numpy as np

img = cv2.imread('101/Images/person_1.png')
row, col = img.shape[:2]
mat = np.float32([[1,0,40],[0,1,30]])

dst = cv2.warpAffine(img, mat, (col, row))
cv2.imshow('Source', img)
cv2.imshow('Translation', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()