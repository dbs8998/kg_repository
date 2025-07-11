# 기존 + 창 띄워서 보기

import cv2
import numpy as np

def find_red_boxes(image):
    # 이미지를 HSV로 변환
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # 빨간 색상 범위 지정 (OpenCV에서는 H값이 0-180이므로 0-10, 170-180 범위를 더해줌)
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    lower_red2 = np.array([170, 100, 100])
    upper_red2 = np.array([180, 255, 255])

    # 빨간 색상을 마스킹
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    # 마스크된 이미지에서 윤곽선을 찾음
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # 빨간 네모 상자 및 각도 필터링
    red_boxes = []
    for contour in contours:
        # 윤곽선의 바운딩 박스 계산
        rect = cv2.minAreaRect(contour)
        box = cv2.boxPoints(rect)
        box = np.intp(box)
        
        # 바운딩 박스 그리기
        cv2.drawContours(image, [box], 0, (0, 255, 0), 2)
        
        # 바운딩 박스의 각도 계산
        angle = rect[2]
        
        # 넓이가 일정 크기 이상인 윤곽선만 선택 (임의의 값으로 설정)
        if cv2.contourArea(contour) > 100:
            # 네모 상자의 중심 좌표 계산
            M = cv2.moments(contour)
            center_x = int(M["m10"] / M["m00"])
            center_y = int(M["m01"] / M["m00"])
            red_boxes.append((center_x, center_y, angle))

    return red_boxes, image

# 이미지 불러오기
image = cv2.imread('images/box_r1.png')

# 빨간 네모 상자와 각도 찾기
red_boxes, image_with_boxes = find_red_boxes(image)

# 찾은 빨간 네모 상자들의 좌표와 각도 출력
for box in red_boxes:
    print("빨간 네모 상자의 좌표:", (box[0], box[1]))
    print("빨간 네모 상자의 각도:", box[2])

# 이미지 창에 표시
cv2.imshow('Image with Red Boxes', image_with_boxes)
cv2.waitKey(0)
cv2.destroyAllWindows()
