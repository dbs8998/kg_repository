# 음원: https://pixabay.com/ko/sound-effects/search/beep/
# 바코드/QR코드 리더기 (이미지)
'''
pip install opencv-python
pip install playsound==1.2.2  # Beep 사운드 재생
pip install pyzbar      # QR / Bar 코드 인식
* pyzbar 오류나면: https://www.microsoft.com/ko-KR/download/details.aspx?id=40784 다운받아 설치
pip uninstall pyzbar -> pip install pyzbar
pip install requests
pip install beautifulsoup4
'''
import cv2
from pyzbar.pyzbar import decode

# 이미지 읽기
image = cv2.imread("./images/1234.png")

# QR 코드 디코딩
barcodes = decode(image)

# 디코딩 결과 출력
if barcodes:
    for barcode in barcodes:
        print(barcode.data.decode("utf-8"))  # 출력: 1234
else:
    print("QR 코드를 찾지 못했습니다.")
