# ⭐️ 문제 1
# [카메라 캡처 & 실시간 영상 출력하기]

# ✅ 조건:

# 웹캠을 열어서 실시간 영상을 캡처

# OpenCV 창에 영상 출력

# ESC나 q 키로 종료

# ✅ 목표 함수:

# cv2.VideoCapture()

# cv2.imshow()

# cv2.waitKey()


import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480)


while True:
    
    ref, frame = capture.read()

    cv2.imshow('test', frame)


    if cv2.waitKey(1) & 0xff == 27:
        capture.release()
        cv2.destroyAllWindows()
        break



