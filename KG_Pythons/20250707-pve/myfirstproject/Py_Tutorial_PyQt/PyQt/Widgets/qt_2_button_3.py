# 버튼 클릭 액션 1
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
        win = QVBoxLayout()
        
        pushbutton = QPushButton("button 1")
        pushbutton.clicked.connect(self.button_clicked)
        win.addWidget(pushbutton)
        
        self.line_input = QLineEdit()  # 외부 접근을 위해 self를 붙임
        win.addWidget(self.line_input) 
        
        self.setLayout(win)
        self.resize(400, 400)
        self.show()
    
    def button_clicked(self):
        print("클릭됨")
        self.line_input.setText("클릭함")
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
