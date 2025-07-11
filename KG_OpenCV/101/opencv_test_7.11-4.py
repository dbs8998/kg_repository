# ⭐⭐⭐ 문제 4
# [특정 색상 범위로 마스크 생성]

# ✅ 조건:

# HSV 이미지에서 특정 색상 범위(H_min ~ H_max, S_min ~ S_max, V_min ~ V_max)를 지정

# cv2.inRange()를 사용해 마스크 생성

# 마스크 이미지 출력

# ✅ 목표 함수:

# cv2.inRange()

# cv2.imshow()

import cv2
import numpy as np

# ① 이미지 읽기
img = cv2.imread('Images/person_1.png')
cv2.imshow('Original', img)

# ② BGR -> HSV 변환
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 색 범위 지정
lower = np.array((100, 100, 100))
upper = np.array((140, 255, 255))

# 마스크 생성
mask = cv2.inRange(img, lower, upper)

# 마스크를 이용해 원본이미지에서 색상 추출
test = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('mask',mask )

cv2.waitKey(0)
cv2.destroyAllWindows()