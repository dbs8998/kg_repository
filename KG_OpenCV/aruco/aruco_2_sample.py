import cv2
import cv2.aruco as aruco
import numpy as np

# ① 카메라 보정 파라미터 로드
camera_matrix = np.load('source/camera_matrix.npy')
dist_coeffs = np.load('source/dist_coeffs.npy')

print("Loaded camera matrix:\n", camera_matrix)
print("Loaded distortion coefficients:\n", dist_coeffs)

# ② ArUco 딕셔너리, 파라미터
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters()
detector = aruco.ArucoDetector(aruco_dict, parameters)

# ③ 캡처 시작
cap = cv2.VideoCapture(0)
marker_length = 0.022  # 단위: m

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # ④ 마커 탐지
    corners, ids, rejectedImgPoints = detector.detectMarkers(gray)

    if ids is not None:
        aruco.drawDetectedMarkers(frame, corners, ids)

        for i in range(len(ids)):
            # ⭐ ArUco 마커의 3D 월드 좌표 정의 (정사각형 기준)
            obj_points = np.array([
                [-marker_length / 2,  marker_length / 2, 0],
                [ marker_length / 2,  marker_length / 2, 0],
                [ marker_length / 2, -marker_length / 2, 0],
                [-marker_length / 2, -marker_length / 2, 0]
            ], dtype=np.float32)

            # ⭐ 감지된 이미지 좌표
            img_points = corners[i][0].astype(np.float32)

            # ⭐ solvePnP로 rvec, tvec 계산
            retval, rvec, tvec = cv2.solvePnP(obj_points, img_points, camera_matrix, dist_coeffs)

            if retval:
                distance = np.linalg.norm(tvec)
                print(f"ID {ids[i][0]} Distance: {distance:.3f} m")

                # 축 그리기
                cv2.drawFrameAxes(frame, camera_matrix, dist_coeffs, rvec, tvec, 0.01)

                # 거리 표시
                cv2.putText(frame,
                            f"ID:{ids[i][0]} Dist:{distance:.2f}m",
                            (10, 30 + i * 30),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 255, 0), 2)

    # ⑤ 화면 출력
    cv2.imshow('Aruco Detector', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
