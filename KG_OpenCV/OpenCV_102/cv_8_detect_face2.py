#   얼굴/눈 인식
# HarrCascade 위치: pip show opencv-python으로 찾으면 됨. 

import cv2

# OpenCV Python 기본 3줄: 객체(영상 소스, 해상도 설정)
capt = cv2.VideoCapture(0)
capt.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capt.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# harr cascade 검출기 객체 생성
face_cascade = cv2.CascadeClassifier('myenv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('myenv/Lib/site-packages/cv2/data/haarcascade_eye.xml')

# 실행
while True:
    ret, frame = capt.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # scaleFactor를 1에 가깝게 해주면 정확도가 상승하나 시간이 오래걸림. 기본값 1.1
    # minNeighbors를 높여주면 검출률이 상승하나 오탐지율도 상승. 각 후보 사각영역이 여러 영역과 겹쳐야 하며 기준보다 적으면 얼굴이 아니라고 판단함.
    # minSize: 얼마나 작은 이미지까지 얼굴로 인정하나?
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=3, minSize=(20,20))
    # eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=3, minSize=(10,10))
    
    # 바운딩 박스 표시
    if len(faces):
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2, cv2.LINE_4)
    # if len(eyes):
    #     for x, y, w, h in eyes:
    #         cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2, cv2.LINE_4)
    
    frame = cv2.flip(frame, 1)
    cv2.imshow("Original", frame)
    if cv2.waitKey(1) == ord('q'):
        break

capt.release()
cv2.destroyAllWindows()