# 노이즈 필터링
import cv2
import numpy as np

# 카메라 객체 생성: 소스 + 해상도 설정
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 동영상 처리: 반복문
while True:
    ret, frame = cap.read()

    if not ret:
        print("Capture Failure")
        break

    # frame에 적용할 salt & papper 노이즈 생성
    noise = np.uint8(np.random.normal(loc=00, scale=0.4, size=frame.shape))
    noised_img = cv2.add(frame, noise)    

    # Blur 필터를 적용함.
    blur = cv2.blur(noised_img, (5,5))

    # 가우시안 Blur: 그냥 blur 보다는 외곽선이 살아남
    gaussian = cv2.GaussianBlur(noised_img, (5,5), 0)

    # bilateral 필터: 가우시안보다 외곽선이 더 살아남.
    bilateral = cv2.bilateralFilter(noised_img, 9, 75, 75)

    # Median blur: salt & pepper를 잘 없애줌. 외곽선도 잘 살림.
    median = cv2.medianBlur(noised_img, 5)

    # ---------------------------
    # 화면에 띄우기
    # # 원본 영상
    # cv2.imshow("Original", frame)

    # # 노이즈 적용영상 (salt & pepper)
    # cv2.imshow("Noised", noised_img)

    # # blur 필터를 적용한 영상
    # cv2.imshow("Blurred", blur)

    # # gaussian blur 적용한 영상
    # cv2.imshow("Gaussian", gaussian)

    # # bilateral 필터 적용한 영상
    # cv2.imshow("Bilateral", bilateral)

    # # Median Blur 적용한 영상
    # cv2.imshow("Median Blurred", median)

    # 여러 영상 창을 하나로 결합
    row1 = cv2.hconcat([frame, noised_img, blur])
    row2 = cv2.hconcat([gaussian, bilateral, median])

    all_windows = cv2.vconcat([row1, row2])
    cv2.imshow("All Win", all_windows)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()