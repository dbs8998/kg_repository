import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ 카메라를 열 수 없습니다.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ 프레임을 읽을 수 없습니다.")
        break

    cv2.imshow('Webcam', frame)

    # ① 창이 닫혔는지 감지
    if cv2.getWindowProperty('Webcam', cv2.WND_PROP_VISIBLE) < 1:
        print("✅ 창이 닫혀서 루프를 종료합니다.")
        break

    # ② q 키로 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("✅ q 키를 눌러서 종료합니다.")
        break

cap.release()
cv2.destroyAllWindows()
