import cv2
import numpy as np

# ① 이미지 불러오기
img = cv2.imread('example1.jpg')
img_copy = img.copy()

# ② 트랙바용 윈도우 생성
cv2.namedWindow('Trackbars')

# ③ 트랙바 생성 함수
def nothing(x):
    pass

cv2.createTrackbar('H_min', 'Trackbars', 0, 179, nothing)
cv2.createTrackbar('H_max', 'Trackbars', 179, 179, nothing)

cv2.createTrackbar('S_min', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('S_max', 'Trackbars', 255, 255, nothing)

cv2.createTrackbar('V_min', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('V_max', 'Trackbars', 255, 255, nothing)

while True:
    # ④ HSV 변환
    hsv = cv2.cvtColor(img_copy, cv2.COLOR_BGR2HSV)

    # ⑤ 트랙바 값 읽기
    h_min = cv2.getTrackbarPos('H_min', 'Trackbars')
    h_max = cv2.getTrackbarPos('H_max', 'Trackbars')
    s_min = cv2.getTrackbarPos('S_min', 'Trackbars')
    s_max = cv2.getTrackbarPos('S_max', 'Trackbars')
    v_min = cv2.getTrackbarPos('V_min', 'Trackbars')
    v_max = cv2.getTrackbarPos('V_max', 'Trackbars')

    # ⑥ inRange로 마스크 생성
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(hsv, lower, upper)

    # ⑦ 마스크 적용해 색상 추출
    result = cv2.bitwise_and(img_copy, img_copy, mask=mask)

    # ⑧ 윤곽선 검출
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # ⑨ 원본 복사
    output = img_copy.copy()

    # ⑩ 윤곽선마다 사각형 그리기
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100:  # 너무 작은 잡음은 무시
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # ⑪ 결과 출력
    cv2.imshow('Original', img_copy)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', result)
    cv2.imshow('Detected', output)

    # 종료 조건
    if cv2.waitKey(1) & 0xFF == 27:  # ESC 키
        break

cv2.destroyAllWindows()
