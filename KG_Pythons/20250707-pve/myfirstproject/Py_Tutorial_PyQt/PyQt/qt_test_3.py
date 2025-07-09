# 🌟 문제 1. 버튼과 레이블
# 목표: 버튼을 누르면 레이블의 텍스트가 바뀌도록 만들어라.

# 요구사항

# QLabel 하나: 초기 텍스트는 "Hello!"

# QPushButton 하나: 텍스트는 "Click me"

# 버튼을 누르면 레이블의 텍스트가 "Button clicked!"로 바뀌도록 한다.

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
        # 1. 레이아웃 생성
        form_main = QVBoxLayout()

        button_widget = QPushButton("button1")
        self.input_widget = QLineEdit()
        

        #button 이벤트
        button_widget.clicked.connect(self.button_clicked)
        form_main.addWidget(button_widget)

        #input 값 처리
        self.input_widget.setText('Hello!')
        form_main.addWidget(self.input_widget)

        # 4. 메인 구현
        self.setLayout(form_main)
        self.resize(500, 500)
        self.show()    

    def button_clicked(self):
        print('클릭')
        self.input_widget.setText('Click me')


if __name__=='__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())


