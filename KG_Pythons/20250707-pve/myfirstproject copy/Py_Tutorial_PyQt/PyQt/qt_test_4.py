# 🌟 문제 2. 입력창과 출력
# 목표: 사용자가 입력한 내용을 출력 레이블에 반영.

# 요구사항

# QLineEdit 하나: 사용자 입력 받기

# QPushButton 하나: "확인" 버튼

# QLabel 하나: 결과 출력

# 버튼을 누르면 QLineEdit에 입력한 내용을 QLabel에 표시한다.

# 예시 동작

# [QLineEdit] -> "파이썬"
# [Button Click]
# [QLabel] -> "파이썬"

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
        self.lable_widget = QLabel()

        #button 이벤트
        button_widget.clicked.connect(self.button_clicked)
        form_main.addWidget(button_widget)

        #input 값 처리
        form_main.addWidget(self.input_widget)
        form_main.addWidget(self.lable_widget)

        # 4. 메인 구현
        self.setLayout(form_main)
        self.resize(500, 500)
        self.show()    

    def button_clicked(self):
        print('클릭')
        self.lable_widget.setText(self.input_widget.text())


if __name__=='__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())


