# ⭐⭐⭐⭐ 문제 7
# [마스크에서 색상 영역 윤곽선 검출 + 사각형 그리기]

# ✅ 조건:

# cv2.findContours()로 마스크에서 윤곽선 탐색

# 각 검출된 윤곽선의 외접 사각형(bounding box) 계산

# 원본 이미지 위에 사각형을 그려 강조

# ✅ 목표 함수:

# cv2.findContours()

# cv2.boundingRect()

# cv2.rectangle()

# cv2.imshow()
import cv2
import numpy as np



# ① 이미지 읽기
img = cv2.imread('Images/box_r1.png')




# bgr -> hsv 변환
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )

# threshold 범위 지정
low1 = np.array([0, 100, 100])
high1 = np.array([10, 255, 255])
low2 = np.array([170, 100, 100])
high2 = np.array([180, 255, 255])



# hsv화면에 threshlod 적용하여 마스크 생성
mask1 = cv2.inRange(hsv, low1, high1)
mask2 = cv2.inRange(hsv, low2, high2)

mask = cv2.bitwise_or(mask1,mask2)

#  cv2.inRange()의 출력 = 흑백 이진 이미지
# 흰색(255) → 관심 영역
# 검정(0) → 배경

# ✅ findContours()는
# 255로 채워진 흰색 blob의 경계 좌표를 모두 반환
# 리스트 형태로 저장

# ✅ ② cv2.RETR_EXTERNAL
# 가장 바깥쪽 윤곽선만 찾기
# 중첩된 내부 윤곽선은 무시

# ✅ ③ cv2.CHAIN_APPROX_SIMPLE
# 윤곽선을 단순화 (꼭짓점만 저장)
# 중복된 경계점 제거
# 메모리 절약

contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
  # 너무 작은 잡음은 무시 (옵션)
  area = cv2.contourArea(cnt)
  if area < 100:
      continue

  # 외접 사각형 좌표 구하기
  x, y, w, h = cv2.boundingRect(cnt)

# 원본 이미지 위에 사각형 그리기
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('result', img)


cv2.waitKey(0)
cv2.destroyAllWindows()