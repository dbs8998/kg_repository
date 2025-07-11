# https://opencv-python.readthedocs.io/en/latest/doc/07.imageArithmetic/imageArithmetic.html#id3
# 이미지 비트연산(AND, OR, NOT, XOR)

import cv2
import numpy as np

img1 = cv2.imread('101/Images/person_1.png')
img2 = cv2.imread('101/Images/logo.png')
img2 = cv2.resize(img2, (100, 100))

# 삽입할 이미지의 row, col, channel
rows, cols, channels = img2.shape

# 배경 이미지에서 삽입 영역 지정: 0부터 rows/cols까지
roi = img1[0:rows, 0:cols]

# mask 만들기: img2 -> gray -> binary 이미지
# mask: logo = 흰색(255), 바탕 = 검정(0)
# mask_inv: 로고=검정, 바탕=흰
img_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img_gray, 10, 255, cv2.THRESH_BINARY)

mask_inv = cv2.bitwise_not(mask)

# bitwise_and()는 둘다 0이 아닌 경우만 값을 통과 시킴.
# 즉, 검정색 아니면 통과 = mask 영영 외 모두 제거.
# 아래 img2_logo의 경우 bg가 제거되고 로고만 남음.
img2_logo = cv2.bitwise_and(img2, img2, mask=mask)
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# 두 이미지 합쳐 = 투명 배경 로고 + 그 부분 배경 이미지
dst = cv2.add(img2_logo, img1_bg)

# 합친 이미지를 원몬 이미지에 추가
img1[0:rows, 0:cols] = dst

cv2.imshow('Result', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
