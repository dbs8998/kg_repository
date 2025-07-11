''' 절차
1. 이미지 불러오기: OpenCV의 cv2.imread() 함수를 사용하여 이미지를 불러옵니다.
2. 빨간 색상 감지: HSV(Hue, Saturation, Value) 색 공간을 사용하여 빨간 색상을 감지합니다. 이를 위해 cv2.cvtColor() 함수로 이미지를 HSV로 변환하고, cv2.inRange() 함수로 빨간색 범위 내의 픽셀을 마스킹합니다.
3. 윤곽선 검출: cv2.findContours() 함수를 사용하여 마스크된 이미지에서 물체의 윤곽선을 찾습니다.
4. 빨간 네모 상자 필터링: 빨간 네모 상자의 경우에는 윤곽선 중 가장 큰 것을 찾아야 합니다. 이를 위해 윤곽선의 넓이를 계산하고, 일정 크기 이상인 윤곽선만을 선택합니다.
5. 네모 상자의 중심 좌표 계산: 선택된 윤곽선의 바운딩 박스의 중심 좌표를 계산합니다.
+ 
6. 네모 상자의 기울어진 각도 출력: (네 꼭지점 찾아야 함)
  - cv2.minAreaRect() : 최소 크기의 사각형 얻기. 
  - 리턴값: 중심좌표, 크기, 회전 각도
'''

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
    
    # 빨간 네모 상자 필터링
    red_boxes = []
    for contour in contours:
        # 윤곽선의 바운딩 박스 계산
        x, y, w, h = cv2.boundingRect(contour)
        area = cv2.contourArea(contour)
        # 넓이가 일정 크기 이상인 윤곽선만 선택 (임의의 값으로 설정)
        if area > 100:
            # 네모 상자의 중심 좌표 계산
            center_x = x + w // 2
            center_y = y + h // 2
            red_boxes.append((center_x, center_y))

    return red_boxes

# 이미지 불러오기
image = cv2.imread('images/image3.png')

# 빨간 네모 상자 찾기
red_boxes = find_red_boxes(image)

# 찾은 빨간 네모 상자들의 좌표 출력
for box in red_boxes:
    print("빨간 네모 상자의 좌표:", box)
