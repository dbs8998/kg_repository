# ⭐⭐⭐ 문제 6
# [마스크를 이용해 색상 부분만 추출하기]

# ✅ 조건:

# inRange()로 만든 마스크를 사용

# cv2.bitwise_and()로 원본 이미지에서 지정한 색상 영역만 남기기

# 나머지 영역은 검은색 처리

# 결과 이미지 출력

# ✅ 목표 함수:

# cv2.bitwise_and()

# cv2.imshow()


import cv2
import numpy as np



# ① 이미지 읽기
img = cv2.imread('Images/cat1.jpg')


while True:   # 'q'가 눌러 질때까지 무한 반복

    # bgr -> hsv 변환
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )

		# threshold 범위 지정
    low = np.array([10, 50, 30])

    high = np.array([180, 150, 150])

		
		# hsv화면에 threshlod 적용하여 마스크 생성
    mask = cv2.inRange(hsv, low, high)
		
		# 이미지에 마스크 적용
    result = cv2.bitwise_and(img, img, mask = mask)

    cv2.imshow("mask", mask)
    cv2.imshow("result", result)

    # 1ms초 마다  키보드 'q'를 기다리기
    if cv2.waitKey(1) & 0xFF == ord('q'):         
        break



cv2.destroyAllWindows()