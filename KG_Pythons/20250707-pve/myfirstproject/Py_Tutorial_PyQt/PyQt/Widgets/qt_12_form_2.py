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
        # 1. 레이아웃 생성
        form_main = QFormLayout()
        birthday_layout = QHBoxLayout()
        phone_layout = QHBoxLayout()
        agree_layout = QHBoxLayout()
        
        # 2. 위젯 생성
        # 2.1 입력창 위젯
        input_name = QLineEdit()
        
        # 2.2 날찌 위젯
        combo_year = QComboBox()
        combo_month = QComboBox()
        combo_date = QComboBox()
        
        for year in range(1900,2025):
            combo_year.addItem(str(year))

        for month in range(1, 13):
            combo_month.addItem(str(month))
        
        for date in range(1, 32):
            combo_date.addItem(str(date))
            
        # 2.3 전화번호 위젯
        combo_phone = QComboBox()
        phone_1 = ['017', '018', '019', '010', '011']
        for ph in phone_1:
            combo_phone.addItem(ph)
        
        label_phone1 = QLabel(" - ")
        label_phone2 = QLabel(" - ")
        input_phone1 = QLineEdit()
        input_phone2 = QLineEdit()
             
        # 2.4 .수신 동의 위젯
        checkBox_agree = QCheckBox("이메일 수신 동의")
                
        # 3. 레이아웃에 위젯 추가
        form_main.addRow("이름: ", input_name)
        
        birthday_layout.addWidget(combo_year)
        birthday_layout.addWidget(combo_month)
        birthday_layout.addWidget(combo_date)
        form_main.addRow("생일: ", birthday_layout)
                
        phone_layout.addWidget(combo_phone)
        phone_layout.addWidget(label_phone1)
        phone_layout.addWidget(input_phone1)
        phone_layout.addWidget(label_phone2)
        phone_layout.addWidget(input_phone2)
        form_main.addRow("전화: ", phone_layout)
        
        agree_layout.addWidget(checkBox_agree)
        form_main.addRow("     ", agree_layout)
        
        # 4. 메인 구현
        self.setLayout(form_main)
        self.resize(500, 500)
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
