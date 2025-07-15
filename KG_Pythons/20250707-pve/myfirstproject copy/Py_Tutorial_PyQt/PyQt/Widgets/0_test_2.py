# 기본 창
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

        self.setLayout(win)   # 레이아웃 설정
        self.setWindowTitle("창 이름") # 창 이름 설정
        self.resize(500, 500) # 화면 크기 조정
        self.show()           # 화면 열기

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()       # Main 클래스의 인스턴스를 생성하고 main 변수에 할당해서 열린 창 유지.
    sys.exit(app.exec_())
    