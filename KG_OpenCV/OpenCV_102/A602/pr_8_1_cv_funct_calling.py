import cv2
from pr_8_cv_funct_called import ImageProcessor

imgEditor = ImageProcessor()

# imgEditor.run_editing()

while True:
    ret, frame = imgEditor.cap.read()

    # 원본 이미지
    cv2.imshow("Original2", frame)

    # 20만큼 밝아진 이미지
    brightened = imgEditor.set_brightness(frame, 30)
    cv2.imshow("Brighter2", brightened)

    if cv2.waitKey(1) == ord('q'):
        break

imgEditor.cap.release()
cv2.destroyAllWindows()