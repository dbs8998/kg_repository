import cv2
import numpy as np


low_th = np.array ([104, 122, 100 ]) #LDH ([38, 100, 101 ])
high_th = np.array([150, 255, 255]) #LDH ([179, 255, 255])

def do_nothing(x):
    pass

# 카메라 0번 선택 (노트북은 보통 0번)
cap = cv2.VideoCapture(0)

# cv2.namedWindow("HSV")

# cv2.createTrackbar("h_low", "HSV", 90, 179, do_nothing)
# cv2.createTrackbar("s_low", "HSV", 100, 255, do_nothing)
# cv2.createTrackbar("v_low", "HSV", 100, 255, do_nothing)
# cv2.createTrackbar("h_high", "HSV", 150, 179, do_nothing)
# cv2.createTrackbar("s_high", "HSV", 250, 255, do_nothing)
# cv2.createTrackbar("v_high", "HSV", 250, 255, do_nothing)

while True:   # 'q'가 눌러 질때까지 무한 반복
    # 카메라를 통해서 frame 읽기
    ret, frame = cap.read() 
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV )

    # h_low = cv2.getTrackbarPos("h_low", "HSV")
    # s_low = cv2.getTrackbarPos("s_low", "HSV")
    # v_low = cv2.getTrackbarPos("v_low", "HSV")
    # h_high = cv2.getTrackbarPos("h_high", "HSV")
    # s_high = cv2.getTrackbarPos("s_high", "HSV")
    # v_high = cv2.getTrackbarPos("v_high", "HSV")

    # th_low = np.array([h_low, s_low, v_low])
    # print(th_low)
    # th_high = np.array([h_high, s_high, v_high])
    # print(th_low)

    mask = cv2.inRange(hsv_frame, low_th, high_th)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # --- 컨투어 반복하며 필터링 + 바운딩 박스 그리기 ---
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:  # 너무 작은 면적은 무시 (노이즈 제거)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) 

        result = cv2.bitwise_and(frame, frame, mask = mask)


    # 1ms초 마다  키보드 'q'를 기다리기
    if cv2.waitKey(1) & 0xFF == ord('q'):         
        break

    cv2.imshow("Camera", frame)
    # cv2.imshow("HSV", hsv_frame)
    # cv2.imshow("RESULT", result)
   

cap.release()
cv2.destroyAllWindows()