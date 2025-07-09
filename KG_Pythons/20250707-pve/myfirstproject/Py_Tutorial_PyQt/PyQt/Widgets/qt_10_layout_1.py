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
        win_main = QVBoxLayout()       # 레이아웃 생성
        layout_h_1 = QHBoxLayout()
        layout_h_2 = QHBoxLayout()
        
        wg_1 = QPushButton("Button 1") # 위젯 생성
        wg_2 = QPushButton("Button 2")
        wg_3 = QPushButton("Button 3")
        wg_4 = QPushButton("Button 4")
        wg_5 = QPushButton("Button 5")

        layout_h_1.addWidget(wg_1)     # 레이아웃에 위젯 추가
        layout_h_1.addWidget(wg_2)

        layout_h_2.addWidget(wg_4)
        layout_h_2.addWidget(wg_5)

        win_main.addLayout(layout_h_1)  # 메인에 레이아웃 추가
        win_main.addWidget(wg_3)        # 메인에 위젯 추가
        win_main.addLayout(layout_h_2)  # 메인에 레이아웃 추가
        
        self.setLayout(win_main)
        self.resize(500, 500)
        self.show()
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
