# 🌟 문제 1. 음식 주문 폼
# 목표: 다양한 위젯을 조합해 사용자 주문폼 GUI 제작

# 요구사항

# QLineEdit : 고객 이름 입력

# QComboBox : 메뉴 선택 (예: "피자", "파스타", "샐러드")

# QSpinBox : 수량 선택 (1~10)

# QCheckBox : 옵션 (예: "추가 치즈", "콜라 포함")

# QPushButton : "주문하기"

# QLabel : 주문 요약 출력

# 동작

# 버튼 클릭 시 아래 포맷으로 주문 내용 출력:

# 고객명: Alice
# 메뉴: 피자
# 수량: 2
# 옵션: 추가 치즈, 콜라 포함

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


        
        button_widget = QPushButton("주문하기")
        self.name_widget = QLineEdit()
        self.menu_widget = QComboBox()
        self.num_widget = QSpinBox()

        self.lable_widget = QLabel()

        #메뉴
        self.menu_widget.addItems(['피자','파스타','샐러드'])

        #수량
        self.num_widget.setRange(0, 10)

        #추가메뉴
        self.side1 = QCheckBox("추가 치즈")
        self.side2 = QCheckBox("콜라 포함")
        side_layout = QHBoxLayout()
        side_layout.addWidget(self.side1)
        side_layout.addWidget(self.side2)

        #button 이벤트
        button_widget.clicked.connect(self.button_clicked)
        form_main.addWidget(button_widget)

        #input 값 처리
        form_main.addRow("고객 이름", self.name_widget)
        form_main.addRow("메뉴 선택", self.menu_widget)
        form_main.addRow("수량 선택", self.num_widget)
        form_main.addRow("추가 옵션",  side_layout)
        form_main.addRow("출력",  self.lable_widget)


        # 4. 메인 구현
        self.setLayout(form_main)
        self.resize(500, 500)
        self.show()    

    def button_clicked(self):
        print('클릭')
        # 고객명: Alice
        # 메뉴: 피자
        # 수량: 2
        # 옵션: 추가 치즈, 콜라 포함
        options = []
        if self.side1.isChecked():
            options.append(self.side1.text())
        if self.side2.isChecked():
            options.append(self.side2.text())

        side = ", ".join(options) if options else "없음"


        result = "고객명:"+self.name_widget.text() + "\n"
        result += "메뉴:"+self.menu_widget.currentText() + "\n"
        result += "수량:"+str(self.num_widget.value()) + "\n"
        result += "옵션:"+side + "\n"
        
        self.lable_widget.setText(result)




if __name__=='__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())


