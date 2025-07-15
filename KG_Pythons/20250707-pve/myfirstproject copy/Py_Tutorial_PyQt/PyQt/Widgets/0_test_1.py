# pip install PyQt5
# 테스팅용 코드
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)  # GUI 앱 인스턴스 생성

win = QWidget()               # 위젯 인스턴스 생성
win.setWindowTitle('PyQt5 Test')   # 창 제목
win.setGeometry(100, 100, 280, 80)  # x여백, y여백, 가로, 세로
# win.move(60, 15)             # 창 이동 위치 x좌표, y좌표
helloMsg = QLabel('<h1>Hello World!</h1>', parent=win) # 이 라벨을 win의 자식으로 설정
helloMsg.move(60, 15)          # 메시지 이동 위치 x좌표, y좌표

win.show()                     # 창 띄우기

sys.exit(app.exec_())   # app 이벤트 루프 시작. -> 시스템 종료.
