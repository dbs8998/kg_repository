# ⭐⭐⭐ 문제 5
# [트랙바로 색상 범위 조정하기]

# ✅ 조건:

# OpenCV 트랙바(슬라이더) UI를 사용해

# H/S/V의 min/max 값을 실시간으로 조정

# 트랙바 값이 변경되면 → 마스크 결과를 즉시 갱신

# 사용자 인터페이스 구현

# ✅ 목표 함수:

# cv2.createTrackbar()

# cv2.getTrackbarPos()


import cv2
import numpy as np


def do_nothing(x):
    pass

# ① 이미지 읽기
img = cv2.imread('Images/cat1.jpg')

# trackbar 윈도우 생성
cv2.namedWindow("HSV", cv2.WINDOW_NORMAL)
cv2.resizeWindow("HSV", 800, 600)  # 가로 800 x 세로 600

# 6개의 trackbar 생성
cv2.createTrackbar("h_low", "HSV", 0, 179, do_nothing)
cv2.createTrackbar("s_low", "HSV", 0, 255, do_nothing)
cv2.createTrackbar("v_low", "HSV", 10, 255, do_nothing)
cv2.createTrackbar("h_high", "HSV", 150, 179, do_nothing)
cv2.createTrackbar("s_high", "HSV", 250, 255, do_nothing)
cv2.createTrackbar("v_high", "HSV", 250, 255, do_nothing)



while True:   # 'q'가 눌러 질때까지 무한 반복

    # bgr -> hsv 변환
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )

		# 트랙바로 조정한 값 가져오기
    h_low = cv2.getTrackbarPos("h_low", "HSV")
    s_low = cv2.getTrackbarPos("s_low", "HSV")
    v_low = cv2.getTrackbarPos("v_low", "HSV")
    h_high = cv2.getTrackbarPos("h_high", "HSV")
    s_high = cv2.getTrackbarPos("s_high", "HSV")
    v_high = cv2.getTrackbarPos("v_high", "HSV")

		# threshold 범위 지정
    th_low = np.array([h_low, s_low, v_low])

    th_high = np.array([h_high, s_high, v_high])

		
		# hsv화면에 threshlod 적용하여 마스크 생성
    mask = cv2.inRange(hsv, th_low, th_high)
		
		# 이미지에 마스크 적용
    result = cv2.bitwise_and(img, img, mask = mask)


    # 1ms초 마다  키보드 'q'를 기다리기
    if cv2.waitKey(1) & 0xFF == ord('q'):         
        break

    # cv2.imshow("mask", mask)
    cv2.imshow("HSV", result)
    # cv2.imshow("RESULT", result)
   


cv2.destroyAllWindows()