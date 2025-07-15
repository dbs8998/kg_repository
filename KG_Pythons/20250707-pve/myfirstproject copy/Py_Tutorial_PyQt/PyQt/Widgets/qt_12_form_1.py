# 입력 폼 만들기
import sys, os
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        # 폼 레이아웃 생성
        form_main = QFormLayout()
        
        # 위젯 생성
        input_name = QLineEdit()
        
        # 폼 레이아웃에 위젯 추가
        form_main.addRow("이름: ", input_name)

        # 메인 구현
        self.setLayout(form_main)
        self.resize(500, 500)
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
