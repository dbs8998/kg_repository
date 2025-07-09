# 기본 위젯들
import sys, os
import PyQt5
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Main(QDialog):          # QDialog 클래스 상속
    def __init__(self):       # Main의 생성자
        super().__init__()    # QDialog의 생성자
        self.init_ui()        # init_ui() 호출해서 인터페이스 초기화
        
    def init_ui(self):        # 기본 화면 구성
        win = QVBoxLayout()   # vertical box
        # win = QHBoxLayout()   # Horizontal box

        label_widget1 = QLabel("Hello 1")
        label_widget2 = QLabel("Hello 2")
        
        # 라벨 서식
        label_widget1.setAlignment(Qt.AlignVCenter)
        label_widget1.setFont(QFont("Arial", 20, QFont.Bold))
        label_widget1.setStyleSheet("color: blue; background-color: #B2CCFF")
        label_widget1.move(100, 240) # x, y
        
        win.addWidget(label_widget1)
        win.addWidget(label_widget2)

        self.setLayout(win)
        self.resize(500, 500)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()       # Main 클래스의 인스턴스를 생성하고 main 변수에 할당해서 열린 창 유지.
    sys.exit(app.exec_())
    
    ###################################
# 주요 정렬 옵션
# Qt.AlignLeft: 왼쪽 정렬
# Qt.AlignRight: 오른쪽 정렬
# Qt.AlignHCenter: 수평 중앙 정렬
# Qt.AlignTop: 위쪽 정렬
# Qt.AlignBottom: 아래쪽 정렬
# Qt.AlignVCenter: 수직 중앙 정렬
# Qt.AlignCenter: 수평 및 수직 중앙 정렬
# Qt.AlignJustify: 양쪽 정렬