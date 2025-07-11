import cv2
import numpy as np

# 1. 색상 처리 함수
def color_filter(img, color, scale):
    dst = np.array(img, np.uint8)
    if color == "blue" or color == 0:
        # ([가로모든열, 세로모든열, 0=파랑] * 비율)
        dst[:, :, 0] = cv2.multiply(dst[:, :, 0], scale)
    elif color == 'green' or color == 1:
        dst[:, :, 1] = cv2.multiply(dst[:, :, 1], scale)
    elif color == 'red' or color == 2:
        dst[:, :, 2] = cv2.multiply(dst[:, :, 2], scale)
    return dst

# 2. 밝기 조절 함수
def set_brightness(img, scale):
    return cv2.add(img, scale)

# 3. 대비 조절 함수
def set_contrast(img, scale):
    return np.uint8(np.clip((1+scale)*img - 128*scale, 0, 255))

# 4. 이미지 사이즈 변경 함수
def set_size(img, scale):
    return cv2.resize(img, dsize=(int(img.shape[1]*scale), int(img.shape[0]*scale)), interpolation=cv2.INTER_AREA)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()

    cv2.imshow("Original", frame)

    # # 빨간색 강조하기
    # redStrong = color_filter(frame, 'red', 1.2)
    # cv2.imshow("Redder", redStrong)

    # # 20 밝게 이미지 구현
    # brightened = set_brightness(frame, 20)
    # cv2.imshow("Brighter", brightened)

    # # 대비값 = 0.9 
    # constrast_ = set_contrast(frame, 0.9)
    # cv2.imshow("Contrast", constrast_)

    # 이미지 사이즈 2배로
    bigger = set_size(frame, 2)
    cv2.imshow("Bigger", bigger)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()