# 음원: https://pixabay.com/ko/sound-effects/search/beep/
# 바코드/QR코드 리더기 (동영상)
'''
pip install opencv-python
pip install playsound==1.2.2  # Beep 사운드 재생
pip install pyzbar      # QR / Bar 코드 인식
* pyzbar 오류나면: https://www.microsoft.com/ko-KR/download/details.aspx?id=40784 다운받아 설치
pip uninstall pyzbar -> pip install pyzbar
'''

import cv2
from pyzbar.pyzbar import decode
from playsound import playsound

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if ret:
        barcodes = decode(frame)
        for barcode in barcodes:
            qr_data = barcode.data.decode("utf-8")
            print("QR Code Data:", qr_data)
            playsound("sound/beep1.mp3")  # QR 코드 스캔 시 소리 재생

        cv2.imshow("QR Code Scanner", frame)

        key = cv2.waitKey(1)
        if key == ord("q"):  # 'q'를 누르면 종료
            break
    else:
        print("Webcam not available.")
        break

cap.release()
cv2.destroyAllWindows()