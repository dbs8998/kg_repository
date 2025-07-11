# 빨간 네모 상자 인식 + 좌표/기울어진 각도 출력
# RGB -> HSV 변환기: https://www.rapidtables.org/ko/convert/color/rgb-to-hsv.html 
# HSV 색상표: https://m.blog.naver.com/jdancor/222881600118 

import cv2
import numpy as np

def find_red_boxes(image):
    # 이미지를 HSV로 변환: 파녹빨 -> 색(0~360각도)채(0~100%)명(0~100%)
    # H -> 0: 적, 60: 황, 120: 녹, 240: 청
    # S -> 0: 무색, 255: 유색
    # v -> 0: 암, 255: 명
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # 빨간 색상 범위 지정 (OpenCV에서는 H값이 0-180(H/2)이므로 0-10, 170-180 범위를 더해줌)
    lower_red = np.array([0, 100, 100])   # 원통의 시작지점부터 10만큼
    upper_red = np.array([10, 255, 255])  # 0 ~ 10
    lower_red2 = np.array([170, 100, 100]) # 원통의 반대 끝부터 10만큼
    upper_red2 = np.array([180, 255, 255]) # 180 ~ 170

    # 빨간 색상을 마스킹(선택 영역(빨간영역)=255(흰색), 그 외=0(검정색))
    mask1 = cv2.inRange(hsv, lower_red, upper_red) # (이미지, 하단, 상단)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    # 두 마스크를 하나의 마스크로 결합 -> 하나의 바이너리 마스크 이미지 도출
    mask = cv2.bitwise_or(mask1, mask2)

    # 마스크된 이미지에서 윤곽선을 찾음
    # mask: 위에서 얻은 이진 이미지
    # cv2.RETR_EXTERNAL: 최외곽 윤곽선만 찾기
    # cv2.CHAIN_APPROX_SIMPLE: 꼭짓점만 반환 (cv2.CHAIN_APPROX_NONE: 윤곽선 모든 점)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # 빨간 네모 상자 및 각도 필터링
    red_boxes = []
    for contour in contours:
        # 윤곽선의 바운딩 박스 계산
        rect = cv2.minAreaRect(contour) # 대상을 둘러싸는 최소 크기 사각형. 리턴값 ((중앙x, 중앙y), (폭, 높이), 각도)
        box = cv2.boxPoints(rect) # 최소 크기 사각형의 네 꼭짓점
        # box = np.int0(box)
        box = box.astype(int)
        # 바운딩 박스의 각도
        angle = rect[2]
        
        # 넓이가 일정 크기 이상인 윤곽선만 선택 (임의의 값으로 설정)
        if cv2.contourArea(contour) > 100: # 노이즈 말고 굵기가 100 이상인
            # 네모 상자의 중심 좌표 계산
            # 키값(m10: x축 방향 질량중심(픽셀의 위치를 기준으로 한 가중치 중심 = x 윤곽선의 중심), m01: y축 방향 질량중심, m00: 질량(위치별 가중치의 합))
            M = cv2.moments(contour)
            center_x = int(M["m10"] / M["m00"]) # 중심이 x축 방향으로 얼마나 떨어져 있나?
            center_y = int(M["m01"] / M["m00"]) # 중심이 y축 방향으로 얼마나 떨어져 있나?
            red_boxes.append((center_x, center_y, angle))

    return red_boxes

# 이미지 불러오기
image = cv2.imread('images/box_r1.png')

# 빨간 네모 상자와 각도 찾기
red_boxes = find_red_boxes(image)

# 찾은 빨간 네모 상자들의 좌표와 각도 출력
for box in red_boxes:
    print("빨간 네모 상자의 좌표:", (box[0], box[1]))
    print("빨간 네모 상자의 각도:", box[2])

