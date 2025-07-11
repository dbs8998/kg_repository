import cv2
from cv2 import aruco
import numpy as np

# 마커의 종류를 규정하는 Dic
marker_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)

# 마커 찾기 객체 생성
param_markers = aruco.DetectorParameters()

# 카메라
cap = cv2.VideoCapture(0)

# 비디오 프레임 처리
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 마커 코너좌표, ID, 거부된 마커 = 마커 탐지()
    marker_corners, marker_IDs, reject = aruco.detectMarkers(
        gray_frame, marker_dict, parameters=param_markers
    )
    
    # 마커 모서리 찾기
    if marker_corners:
        for ids, corners in zip(marker_IDs, marker_corners):
            cv2.polylines(
                frame, [corners.astype(np.int32), True, (0, 255, 255), 4, cv2.LINE_AA]
            )  # NumPy 배열인 frame(이미지)에 각 마커의 코너를 이어서 다각형 태두리 그림. OpenCV 계산을 위해 코너 좌표값은 np.int32 형식으로 변환함. 선의 종류는 cv2.LINE_AA임.
            corners = corners.reshape(4, 2)  # 코너 배열모양 변경 -> 코너좌표
            corners = corners.astype(int)  # 좌표를 int로 변환
            top_right = tuple(corners[0]) # 마커의 각 코너 좌표 대입
            top_left = tuple(corners[1])
            bottom_right = tuple(corners[2])
            bottom_left = tuple(corners[3])
            cv2.putText(       # 마커 ID를 우상단에 표시
                frame,
                f"id: {ids[0]}",
                top_right,
                cv2.FONT_HERSHEY_PLAIN,
                1.3,
                (200, 100, 0),
                2,
                cv2.LINE_AA,
            )
            print(ids, "   ", corners)
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)        # 키 입력 대기
    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()