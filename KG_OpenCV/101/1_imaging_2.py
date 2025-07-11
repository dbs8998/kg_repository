# https://opencv-python.readthedocs.io/en/latest/doc/06.operation/operation.html
# 이미지 ROI 

import cv2
import numpy as np

img = cv2.imread('101/Images/person_4.jpg')

#ROI: img[행 시작:끝, 열 시작:끝]
ball = img[409:454, 817:884] 

img[470:515, 817:884] = ball #근처에 Copy

cv2.imshow("Ball 2", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

###########################################
# 이미지 크기 참고용 (행, 열, 채널)
print(img.shape)   # (641, 963, 3)
###########################################

# 미션 1: 아무 이미지나 다운 받아 ROI를 복사해보시오.

# 주의: 행열의 폭이 일치해야 에러가 안 남.  
# ball2 = img2[60:100, 80:120]   # 행폭: 40, 열 동일
# img2[120:160, 80:120] = ball2  # 행폭 40으로 맞춤
