# Aruco 마커 생성 (체커보드 생성은 카메라 보정에서 함)

import cv2 as cv
from cv2 import aruco

# 마커 생성 시 사용할 딕셔너리 지정
marker_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)

# MARKER_ID = 0
MARKER_SIZE = 200  # pixels

# for 문으로 원하는 수의 마커 생성
for id in range(5):  
    marker_image = aruco.generateImageMarker(marker_dict, id, MARKER_SIZE)
    cv.imshow("img", marker_image)
    cv.imwrite(f"source/marker_{id}.png", marker_image)
    # cv.waitKey(0)
    # break
    
    