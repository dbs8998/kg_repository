# https://opencv-python.readthedocs.io/en/latest/doc/10.imageTransformation/imageTransformation.html
# 이미지 회전

import cv2

img = cv2.imread(r'101\Images\person_1.png')
row, col = img.shape[:2]
mat = cv2.getRotationMatrix2D((col/2,row/2),90,0.5)

dst = cv2.warpAffine(img, mat, (col,row))

cv2.imshow('Source', img)
cv2.imshow('Rotated', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()