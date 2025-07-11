# 상세 설명: 0_basics_1.py

import cv2

img_path = r'101\Images\person_2.jpg'

# 읽기
img_color = cv2.imread(img_path, cv2.IMREAD_COLOR)
img_gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
img_alpha = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

# 리턴값 보기
print(img_color.shape) # numpy의 ndarray type (246(Y축), 205(X축), 3(각 픽셀의 원소수 = BGR)) 이미지 사이즈는 246 X 205

# 보기
cv2.imshow('Color', img_color)
cv2.imshow('Gray', img_gray)
cv2.imshow('Alpha', img_alpha)

# 저장하기
cv2.imwrite('101/Images/person_2_gray.jpg', img_gray)

cv2.waitKey(0)    # 0이면 무한 대기, 밀리세컨드
cv2.destroyAllWindows()

###############################
# # 미션: 적당한 이미지를 다운받아 3가지 플래그를 적용하고 3개의 창에 띄우시오.

# import cv2

# fname = r'OpenCV\101\Images\person_4.jpg'

# original = cv2.imread(fname, cv2.IMREAD_COLOR)
# gray = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
# unchange = cv2.imread(fname, cv2.IMREAD_UNCHANGED)

# cv2.imshow('Original', original)
# cv2.imshow('Gray', gray)
# cv2.imshow('Unchange', unchange)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
################################