# HSV 색공간 적용

import cv2
import numpy as np

img_src = cv2.imread('101/Images/person_4.jpg')
img_hsv = cv2.cvtColor(img_src, cv2.COLOR_BGR2HSV)

# 어두운 ~ 밝은 파랑 하한/상한 픽셀값
low_blue = np.array([110, 50, 50])
high_blue = np.array([130, 255, 255])

# mask 만들기
mask1 = cv2.inRange(img_hsv, low_blue, high_blue)

# mask 적용: 파랑=흰색, 나머지=검정
result = cv2.bitwise_and(img_hsv, img_hsv, mask=mask1)

cv2.imshow("HSV", img_hsv)
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
