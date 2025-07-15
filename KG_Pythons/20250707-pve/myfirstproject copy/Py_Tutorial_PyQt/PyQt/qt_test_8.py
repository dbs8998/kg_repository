# 🌟 문제 3. 일정 관리 앱
# 목표: 날짜/시간 선택과 리스트 추가

# 요구사항

# QDateTimeEdit : 일정 날짜와 시간 선택

# QLineEdit : 일정 내용 입력

# QPushButton : "추가하기"

# QListWidget : 일정 목록 출력

# "추가하기" 버튼 누르면 리스트에 아래 형태로 추가

# 2025-07-07 14:30 - 회의

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

        
        button_widget = QPushButton("추가하기")
        
        self.text_widget = QLineEdit()
        self.date_widget = QDateTimeEdit()
   
        self.lable_widget = QListWidget()


        #input 값 처리
        form_main.addRow("일정",  self.date_widget)
        form_main.addRow("내용",  self.text_widget)

        self.lable_widget.setFixedSize(430, 300)
        form_main.addRow("",  self.lable_widget)


        #button 이벤트
        button_widget.clicked.connect(self.button_clicked)
        form_main.addRow(button_widget)

        # 4. 메인 구현
        self.setLayout(form_main)
        self.resize(500, 500)
        self.show()    

    def button_clicked(self):
        print('클릭')

        # "추가하기" 버튼 누르면 리스트에 아래 형태로 추가

        #내용 기입
        if not self.text_widget.text().strip():
            QMessageBox.warning(self, "경고", "일정 내용을 입력하세요!")
            return

        # 2025-07-07 14:30 - 회의
        result = self.date_widget.dateTime().toString("yyyy-MM-dd hh:mm") + " - " + self.text_widget.text()
        self.lable_widget.addItem(result)

        #이전 내용 초기화
        self.text_widget.clear()

if __name__=='__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())


