import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # ① BGR → HSV 변환
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # 1. 대비 & 밝기 조정
    alpha = 1.5
    beta = 20
    adjusted = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)

    # 2. 샤프닝
    kernel = np.array([[0, -1, 0],
                        [-1, 5, -1],
                        [0, -1, 0]])
    sharpened = cv2.filter2D(adjusted, -1, kernel)

    # 3. HSV 변환
    hsv = cv2.cvtColor(sharpened, cv2.COLOR_BGR2HSV)

    # 4. 색 마스크
    # ② 노란색 범위 설정
    # lower_yellow = np.array([20, 100, 100])
    # upper_yellow = np.array([30, 255, 255])
    # 파랑
    # lower_blue = np.array([100, 150, 0])
    # upper_blue = np.array([140, 255, 255])
    # lower_blue = np.array([100, 50, 30])
    # upper_blue = np.array([140, 255, 180])
    lower_yellow = np.array([20, 30, 30])
    upper_yellow = np.array([30, 255, 200])


    # ③ 색상 마스크 생성
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # ④ 노이즈 제거 (선택)
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

    # ⑤ 컨투어 찾기
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)



    # ⑥ 컨투어에서 사각형 그리고 표시
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:   # 너무 작은 노이즈는 무시
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
            cv2.putText(frame, 'Yellow Detected', (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

    # ⑦ 화면 출력
    cv2.imshow('Original with Yellow Boxes', frame)
    cv2.imshow('Mask', mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
