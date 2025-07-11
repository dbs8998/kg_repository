## CV2 기본 문법

import cv2

pic = r'101\Images\person_2.jpg'

# 1. 이미지 읽기
# cv2.imread(파일명, 옵션 플래그)
# 리턴 타입: numpy.ndarray
img = cv2.imread(pic, cv2.IMREAD_COLOR)
print(img.shape) # 리턴된 img 행렬: (246, 205, 3)
# 246: 행(Y축)
# 205: 열(X축)
# 3  : xy 교차점에 있는 원소가 3개(BGR)
'''
# 대표 flag 3가지
cv2.IMREAD_COLOR 또는 1: 이미지를 칼라로 읽음. 투명 = 디폴트값으로 대체
cv2.IMREAD_GRAYSCALE 또는 0: Grayscale로 읽음. 이미지 처리 중간 단계임.
cv2.IMREAD_UNCHANGED 또는 -1: Alpha channel(투명)까지 포함해 읽음.
'''
img_gray = cv2.imread(pic, 0)
print(img_gray.shape)  # 리턴된 img 행렬: (246, 205)

# 2. 이미지 보기
# cv2.imshow(창이름, 보여줄 이미지)
# cv2.waitKey()  
# cv2.destroyAllWindows()
cv2.imshow('Show', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 3. 이미지 저장하기
# cv2.imwrite(저장 파일명, 저장할 이미지)
cv2.imwrite(r'OpenCV\101\Images\101_1.png', img_gray)

# 4. 창 닫기
# cv2.waitKey(시간)    # (0: 키 입력까지 무한 대기, 시간: 밀리 초)
# cv2.destroyAllWindows()
cv2.waitKey(0)
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