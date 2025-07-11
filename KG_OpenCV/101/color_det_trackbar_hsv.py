import cv2
import numpy as np


def do_nothing(x):
    pass

# 카메라 0번 선택 (노트북은 보통 0번)
cap = cv2.VideoCapture(0)

# trackbar 윈도우 생성
cv2.namedWindow("HSV")

# 6개의 trackbar 생성
cv2.createTrackbar("h_low", "HSV", 90, 179, do_nothing)
cv2.createTrackbar("s_low", "HSV", 100, 255, do_nothing)
cv2.createTrackbar("v_low", "HSV", 100, 255, do_nothing)
cv2.createTrackbar("h_high", "HSV", 150, 179, do_nothing)
cv2.createTrackbar("s_high", "HSV", 250, 255, do_nothing)
cv2.createTrackbar("v_high", "HSV", 250, 255, do_nothing)

while True:   # 'q'가 눌러 질때까지 무한 반복
    # 카메라를 통해서 frame 읽기
    ret, frame = cap.read() 
    
    # bgr -> hsv 변환
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV )

		# 트랙바로 조정한 값 가져오기
    h_low = cv2.getTrackbarPos("h_low", "HSV")
    s_low = cv2.getTrackbarPos("s_low", "HSV")
    v_low = cv2.getTrackbarPos("v_low", "HSV")
    h_high = cv2.getTrackbarPos("h_high", "HSV")
    s_high = cv2.getTrackbarPos("s_high", "HSV")
    v_high = cv2.getTrackbarPos("v_high", "HSV")

		# threshold 범위 지정
    th_low = np.array([h_low, s_low, v_low])
    print(th_low)
    th_high = np.array([h_high, s_high, v_high])
    print(th_low)
		
		# hsv화면에 threshlod 적용하여 마스크 생성
    mask = cv2.inRange(hsv_frame, th_low, th_high)
		
		# 이미지에 마스크 적용
    result = cv2.bitwise_and(frame, frame, mask = mask)


    # 1ms초 마다  키보드 'q'를 기다리기
    if cv2.waitKey(1) & 0xFF == ord('q'):         
        break

    cv2.imshow("Camera", frame)
    cv2.imshow("HSV", hsv_frame)
    cv2.imshow("RESULT", result)
   

cap.release()
cv2.destroyAllWindows()