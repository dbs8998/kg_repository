# EasyOCR: https://github.com/lagunerio/ML-Practice/tree/main/EasyOCR 
# pip install easyocr
# pip install opencv-python-headless==4.5.4.60
import easyocr
import cv2

reader = easyocr.Reader(['en'], gpu=False)
imgSrc = 'images/19오7777.jpg'
result = reader.readtext(imgSrc)

# 이미지를 올바르게 로드하는지 확인
img = cv2.imread(imgSrc)

if img is not None:
    result = reader.readtext(img)
    print(result)
else:
    print("이미지 인식 실패")
