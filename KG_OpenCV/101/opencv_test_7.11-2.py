# ✅ 문제 2 (하급 ⭐️)
# [RGB → HSV 변환 후 출력하기]

# ✅ 조건:

# 이미지를 HSV 색공간으로 변환

# 변환된 HSV 이미지를 새 창에 출력

# ✅ 목표 함수:

# cv2.cvtColor()

import cv2

img_path = 'Images/person_1.png'

img = cv2.imread(img_path, cv2.IMREAD_COLOR)

# BGR → HSV 변환
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 색 범위 지정 (예: 파랑)
lower_blue = (100, 150, 0)
upper_blue = (140, 255, 255)

# 마스크 생성
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# 원본과 마스크 합성
result = cv2.bitwise_and(img, img, mask=mask)

#imshow()의 경우 출력되는 이미지는 RGB값을 기준으로 출력된다 그래서 HSV로 바꾼 값을 그대로 show로 출력시 색깔이 이상하게 보이는것
#HSV로 작업한 이미지를 정상적으로 보기 위해서는 다시 RGB값으로 변환해주어야 한다.
bgr_again = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# 출력
cv2.imshow('Mask', mask)
cv2.imshow('Result', result)
cv2.imshow('bgr_again',bgr_again)

# 출력
# cv2.imshow('Original', img)
# cv2.imshow('HSV', hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()