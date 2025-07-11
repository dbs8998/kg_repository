# 가상환경 구축: python -m venv myenv
# 가상환경 활성화: myenv\Scripts\activate
# 가상환경 안 되면: PowerShell 관리자모드 > Set-ExecutionPolicy RemoteSigned 입력 > Y 입력 > 터미널 껐다 다시 켜기
# OpenCV-python 설치: pip install opencv-python
# python -m pip install --upgrade pip  
# haarcascade 확인: myenv\Lib\cv2\data
# 혹시 없다면 안면인식만 다운로드: wget 

import cv2

# 기본 탬플릿
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = capture.read()
    cv2.imshow("Original", frame)
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
