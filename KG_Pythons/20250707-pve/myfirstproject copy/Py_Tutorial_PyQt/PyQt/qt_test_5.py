# 🌟 문제 3. 간단 계산기
# 목표: 두 수를 입력받아 합을 구한다.

# 요구사항

# QLineEdit 2개: 첫 번째 숫자, 두 번째 숫자

# QPushButton 하나: "더하기" 버튼

# QLabel 하나: 결과 출력

# 버튼 클릭 시 두 입력값을 더해 레이블에 출력

# 예시 동작


# Input1: 5
# Input2: 7
# [Button Click]
# Result: 12


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
        
        button_widget = QPushButton("더하기")
        self.input_widget1 = QLineEdit()
        self.input_widget2 = QLineEdit()
        self.lable_widget = QLabel()

        #button 이벤트
        button_widget.clicked.connect(self.button_clicked)
        form_main.addWidget(button_widget)

        #input 값 처리
        form_main.addWidget(self.input_widget1)
        form_main.addWidget(self.input_widget2)
        form_main.addWidget(self.lable_widget)

        # 4. 메인 구현
        self.setLayout(form_main)
        self.resize(500, 500)
        self.show()    

    def button_clicked(self):
        print('클릭')
        num1 = int(self.input_widget1.text())
        num2 = int(self.input_widget2.text())
        result = num1 + num2
        print(self.input_widget2.text())
        self.lable_widget.setText(str(result))


if __name__=='__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())


