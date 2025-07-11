# ⭐️ 문제 3
# [HSV 채널 분리 및 출력하기]

# ✅ 조건:

# HSV 이미지에서 H, S, V 채널을 분리

# 각 채널을 회색조 이미지로 개별 출력

# ✅ 목표 함수:

# cv2.split()

# cv2.imshow()


import cv2

# ① 이미지 읽기
img = cv2.imread('Images/person_1.png')
cv2.imshow('Original', img)

# ② BGR -> HSV 변환
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(hsv)
# ③ 채널 분리
h, s, v = cv2.split(hsv)

# ④ 각 채널을 회색조로 출력
cv2.imshow('Hue Channel', h)
cv2.imshow('Saturation Channel', s)
cv2.imshow('Value Channel', v)

cv2.waitKey(0)
cv2.destroyAllWindows()