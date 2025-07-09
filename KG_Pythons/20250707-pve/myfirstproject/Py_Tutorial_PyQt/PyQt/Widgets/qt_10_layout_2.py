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
        win_main = QHBoxLayout()
        layout_h_1 = QHBoxLayout()
        layout_h_2 = QHBoxLayout()
        layout_v_1 = QVBoxLayout()
        layout_v_2 = QVBoxLayout()
        layout_v_3 = QVBoxLayout()
        
        # 2. 위젯 생성
        label_1 = QLabel("아이스크림")
        button_1 = QPushButton("누르시오.")
        spinBox_1 = QSpinBox()
        comboB_1 = QComboBox()
        list_1 = QListWidget()
        checkB_1 = QCheckBox("스푼 포함")
        checkB_2 = QCheckBox("초 포함")
        radioB_1 = QRadioButton("포장")
        radioB_2 = QRadioButton("매장")

        # 3. 위젯의 항목 추가
        comboB_1.addItem("바닐라맛")
        comboB_1.addItem("딸기맛")
        comboB_1.addItem("사과맛")
        
        list_1.addItem(QListWidgetItem("Large"))
        list_1.addItem(QListWidgetItem("Small"))

        # 4. 레이아웃에 위젯 추가
        layout_h_1.addWidget(label_1)
        layout_h_1.addWidget(button_1)

        layout_v_1.addLayout(layout_h_1)
        layout_v_1.addWidget(spinBox_1)

        layout_v_2.addWidget(checkB_1)
        layout_v_2.addWidget(checkB_2)
        layout_v_2.addWidget(radioB_1)
        layout_v_2.addWidget(radioB_2)

        layout_h_2.addWidget(list_1)
        layout_h_2.addLayout(layout_v_2)
        
        layout_v_3.addWidget(comboB_1)
        layout_v_3.addLayout(layout_h_2)
        
        # 5. 메인에 레이아웃 추가
        win_main.addLayout(layout_v_1)
        win_main.addLayout(layout_v_3)

        self.setLayout(win_main)
        self.resize(500, 500)
        self.show()
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
