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
        
        win.addWidget(label_widget1)
        win.addWidget(label_widget2)

        self.setLayout(win)
        self.resize(500, 500)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()       # Main 클래스의 인스턴스를 생성하고 main 변수에 할당해서 열린 창 유지.
    sys.exit(app.exec_())