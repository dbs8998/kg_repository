# https://opencv-python.readthedocs.io/en/latest/doc/11.imageSmoothing/imageSmoothing.html
# 이미지 필터링

import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('101/Images/person_1.png')
cv2.namedWindow('Filter')
cv2.createTrackbar('F', 'Filter', 1, 20, nothing)

while True:
    if cv2.waitKey(1) & 0xff == 27:
        break
    fil = cv2.getTrackbarPos('F', 'Filter')

    #(0,0)이면 에러니까 1로 치환함.
    if fil == 0:
        fil = 1
    
    #트랙바로 (1,1)~(20,20) kernel 생성
    kernel = np.ones((fil, fil), np.float32)/(fil*fil)
    dst = cv2.filter2D(img,-1,kernel)

    cv2.imshow('Filter', dst)
    
cv2.waitKey(0)
cv2.destroyAllWindows()
