# OpenCV program to detect face in real time
# import libraries of python OpenCV
# where its functionality resides
import cv2

# Trained XML classifiers describes some features of some
# object we want to detect a cascade function is trained
# from a lot of positive(faces) and negative(non-faces)
# images.
face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')

# Trained XML file for detecting eyes
eye_cascade = cv2.CascadeClassifier(r'haarcascade_eye.xml')

# capture frames from a camera
cap = cv2.VideoCapture(0)


frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_center_x = frame_width // 2
DISTANCE_SCALE = 300  # 임의값, 실험으로 맞추자
ANGLE_SCALE = 0.1     # 임의값, 픽셀 → 각도 환산

# loop runs if capturing has been initialized.
while 1:

    # reads frames from a camera
    ret, img = cap.read()

    # convert to gray scale of each frames
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detects faces of different sizes in the input image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)


    for (x,y,w,h) in faces:
        # To draw a rectangle in a face
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        # Detects eyes of different sizes in the input image
        eyes = eye_cascade.detectMultiScale(roi_gray)

        # To draw a rectangle in eyes
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
        
        # ---------- 거리 추정 ----------
        # 간단히 얼굴 크기 → 거리 근사
        distance_estimate = DISTANCE_SCALE / w
        distance_text = f"Dist: {distance_estimate:.2f}"

        # ---------- 각도 추정 ----------
        face_center_x = x + w // 2
        angle_offset = (face_center_x - frame_center_x) * ANGLE_SCALE
        angle_text = f"Angle: {angle_offset:.1f} deg"

        # ---------- 화면에 표시 ----------
        cv2.putText(img, distance_text, (x, y - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
        cv2.putText(img, angle_text, (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
        
    # Display an image in a window
    cv2.imshow('img',img)

    # Wait for Esc key to stop
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()