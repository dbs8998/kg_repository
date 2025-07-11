# [마스크 외부 영역 회색 배경 처리]

# ✅ 조건:

# 색상 영역만 남기고 나머지 배경을 (128,128,128)의 회색으로 처리

# 배경 부분 색상 바꾸는 연산 수행

# 결과 이미지 출력

# ✅ 힌트:

# 마스크 반전

# numpy 배열 연산 활용

# ✅ 목표 함수:

# cv2.bitwise_not()

# numpy 연산

#흐름 원본 이미지 와 hsv 이미지 구분 -> hsv이미지로 mask이미지를 생성 -> 해당 mask이미지를 반전

# -> 

import numpy as np
import cv2

img_path = 'Images/box_r1.png'

# ① 이미지 읽기 (BGR)
bgr = cv2.imread(img_path)
hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)

# ② 색 범위 마스크 생성 (빨간색 예제)
low1 = np.array([0, 100, 100])
upper1 = np.array([10, 255, 255])
low2 = np.array([170, 100, 100])
upper2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, low1, upper1)
mask2 = cv2.inRange(hsv, low2, upper2)
mask = cv2.bitwise_or(mask1, mask2)

# ③ 마스크 반전
mask_inv = cv2.bitwise_not(mask)

# ④ 색상 영역 → 원본 이미지
foreground = cv2.bitwise_and(bgr, bgr, mask=mask)
cv2.imshow('foreground',foreground)

# ⑤ 회색 배경 이미지 생성
gray_background = np.full_like(bgr, (128, 128, 128))

# ⑥ 배경 영역 → 회색 적용
background = cv2.bitwise_and(gray_background, gray_background, mask=mask_inv)
cv2.imshow('background',background)
# ⑦ 둘 합치기
result = cv2.add(foreground, background)

# ⑧ 결과 출력
cv2.imshow('Original', bgr)
cv2.imshow('Mask', mask)
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
