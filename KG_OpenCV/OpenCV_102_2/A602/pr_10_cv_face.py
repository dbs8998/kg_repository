import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

path = 'C:/Users/AI06/Documents/_Pr_1/Python/OpenCV/cv_env/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml'

face_cascade = cv2.CascadeClassifier(path)

# 실행부
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=3, minSize=(20, 20))

    
    # 바운딩 박스 표시
    if len(faces):
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2, cv2.LINE_4)
    
    cv2.imshow("Original", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

