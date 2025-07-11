# Tesseract 다운/설치: https://github.com/UB-Mannheim/tesseract/wiki 
# 한글은 잘 안 됨. Naver Clova OCR이 한글 인식률은 더 좋음.

import pytesseract       # Tesseract설치 후 pip install pytesseract
from PIL import Image
import os                
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = Image.open(r'images\ocr_img_2.jpg')
# result = pytesseract.image_to_string(img)
result = pytesseract.image_to_string(img, lang='kor') #한국어: lang 옵션 필요
## 영어 한글 동시 인식
# my_config = "-l eng+kor --oem 3 --psm 6 --tessdata-dir 'C:/Program Files/Tesseract-OCR/tessdata'"
# result = pytesseract.image_to_string(img, config=my_config)

print(result)
