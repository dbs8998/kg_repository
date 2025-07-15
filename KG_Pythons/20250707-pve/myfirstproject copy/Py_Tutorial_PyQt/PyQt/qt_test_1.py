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
        date_layout = QHBoxLayout()
        time_layout = QHBoxLayout()

        main_layout = QVBoxLayout()

        #그룹박스
        group_box = QGroupBox("Appointment Details")

        # 2. 위젯 생성
        # 2.1 입력창 위젯
        
        item_1 = QListWidgetItem("Developer meetiong")
        item_2 = QListWidgetItem("A brief meeting to check the status of each project in the development department.")

        date_widget = QDateEdit()
        time_widget = QTimeEdit()
        location_widget = QLineEdit()
        text_widget = QListWidget()
 
        # 3. 레이아웃에 위젯 추가
        date_widget.setDisplayFormat("dd MMM yyyy")
        date_layout.addWidget(date_widget)
        form_main.addRow("Date: ", date_layout)
        
        time_widget.setDisplayFormat("hh:mm:ss AP")
        time_layout.addWidget(time_widget)
        form_main.addRow("Time: ", time_layout)
        
        location_widget.setText("Meeting room 1")
        form_main.addRow("Location: ", location_widget)           

        text_widget.addItem(item_1)
        item_1.setFont(QFont("Arial", 12, QFont.Bold))
        text_widget.addItem(item_2)
        
        text_widget.setFixedSize(450, 300)
        text_widget.setWordWrap(True)
        form_main.addRow(text_widget)

        # ---------- 그룹박스에 레이아웃 적용 ----------
        group_box.setLayout(form_main)

        # ---------- 메인 레이아웃에 그룹박스 추가 ----------
        main_layout.addWidget(group_box)
    
        # 4. 메인 구현
        self.setLayout(main_layout)
        self.resize(500, 500)
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
