# 🌟 문제 2. 회원 가입 폼
# 목표: 다양한 위젯과 레이아웃 배치

# 요구사항

# QLineEdit 3개: 이름, 이메일, 비밀번호

# QRadioButton 2개: 성별 선택 (남, 여)

# QDateEdit : 생년월일 입력

# QPushButton : "가입하기"

# QLabel : 결과 출력

# 동작

# 버튼 클릭 시 입력 내용을 한 줄로 출력:

# 이름: Alice, 이메일: alice@example.com, 성별: 여, 생년월일: 1995-07-02

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
        # 폼 1. 레이아웃 생성
        form_main = QFormLayout()
        gender_layout = QHBoxLayout()
  
        
        button_widget = QPushButton("가입하기")
        
        self.name_widget = QLineEdit()
        self.email_widget = QLineEdit()
        self.pw_widget = QLineEdit()
        # 사용자 입력이 ●●●●● 형태로 숨겨집니다.
        self.pw_widget.setEchoMode(QLineEdit.Password)
        
        self.date_widget = QDateEdit()
   
        self.lable_widget = QLabel()

        #성별
        self.gender_widget1 = QRadioButton('남')
        self.gender_widget2 = QRadioButton('여')
        gender_layout.addWidget(self.gender_widget1)
        gender_layout.addWidget(self.gender_widget2)


        #button 이벤트
        button_widget.clicked.connect(self.button_clicked)
        form_main.addWidget(button_widget)

        #input 값 처리
        form_main.addRow("이름", self.name_widget)
        form_main.addRow("이메일", self.email_widget)
        form_main.addRow("성별", gender_layout)
        form_main.addRow("생년월일",  self.date_widget)
        form_main.addRow("출력",  self.lable_widget)


        # 4. 메인 구현
        self.setLayout(form_main)
        self.resize(500, 500)
        self.show()    

    def button_clicked(self):
        print('클릭')


        # 이름: Alice, 이메일: alice@example.com, 성별: 여, 생년월일: 1995-07-02

    
        gender = ""
        if self.gender_widget1.isChecked():
            gender = self.gender_widget1.text()
        elif self.gender_widget2.isChecked():
            gender = self.gender_widget2.text()
        else:
            gender = "선택 안함"

        result = "고객명:"+self.name_widget.text() 
        result += ", 이메일:"+self.email_widget.text()
        result += ", 성별:"+ gender
        result += ", 생년월일:"+ self.date_widget.date().toString("yyyy-MM-dd")
        
        self.lable_widget.setText(result)




if __name__=='__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())


