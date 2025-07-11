import cv2

pic = r'101\Images\cat1.jpg'

img_color = cv2.imread(pic, cv2.IMREAD_COLOR)
img_gray = cv2.imread(pic, cv2.IMREAD_GRAYSCALE)
img_alpha = cv2.imread(pic, cv2.IMREAD_UNCHANGED)

# 리턴값 보기
print(img_color.shape) # numpy의 ndarray type (246(Y축), 205(X축), 3(각 픽셀의 원소수 = BGR)) 이미지 사이즈는 246 X 205


# 보기
cv2.imshow('Color', img_color)
cv2.imshow('Gray', img_gray)
cv2.imshow('Alpha', img_alpha)

cv2.waitKey(0)    # 0이면 무한 대기, 밀리세컨드
cv2.destroyAllWindows()
