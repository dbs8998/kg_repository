# ⭐️ 문제 2
# [실시간 프레임 → HSV 변환 후 출력]

# ✅ 조건:

# 웹캡 프레임을 읽어

# BGR → HSV 변환

# HSV 영상을 새 창에 출력

# ✅ 목표 함수:

# cv2.cvtColor()

# ✅ 주의:

# HSV 영상은 사람이 보기엔 색이 이상해 보일 수 있음 (설명 포함)

import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480)


while True:
    
    ref, frame = capture.read()

    cv2.imshow('test', frame)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.imshow('hsv', hsv)

    if cv2.waitKey(1) & 0xff == 27:
        capture.release()
        cv2.destroyAllWindows()
        break