# 파랑, 노랑, 초록 네모 상자 인식 (+ 좌표/기울어진 각도 출력)
# mask 한 개로 처리한 예

import cv2
import numpy as np

def find_color_boxes(image, lower_color, upper_color):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # 색상 범위에 대한 마스크 생성
    mask = cv2.inRange(hsv, lower_color, upper_color)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    color_boxes = []
    for contour in contours:
        # 윤곽선의 바운딩 박스 계산
        x, y, w, h = cv2.boundingRect(contour)
        area = cv2.contourArea(contour)
        # 넓이가 일정 크기 이상인 윤곽선만 선택 (임의의 값으로 설정)
        if area > 100:
            # 네모 상자의 중심 좌표 계산
            center_x = x + w // 2
            center_y = y + h // 2
            color_boxes.append((center_x, center_y))

    return color_boxes

# 이미지 불러오기
image = cv2.imread('images/box_bgy1.png')

# 파란색에 대한 범위
lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])

# 노란색에 대한 범위
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

# 초록색에 대한 범위
lower_green = np.array([45, 100, 100])
upper_green = np.array([75, 255, 255])

# 파란색 상자 찾기
blue_boxes = find_color_boxes(image, lower_blue, upper_blue)

# 노란색 상자 찾기
yellow_boxes = find_color_boxes(image, lower_yellow, upper_yellow)

# 초록색 상자 찾기
green_boxes = find_color_boxes(image, lower_green, upper_green)

# 찾은 상자들의 좌표 출력
print("파란색 상자 좌표:", blue_boxes)
print("노란색 상자 좌표:", yellow_boxes)
print("초록색 상자 좌표:", green_boxes)

