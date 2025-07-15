# 위젯 렌덤 위치 띄우기
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
        # Label
        label = QLabel("Label", self)
        label.move(50, 20)  # x, y coordinates
        
        # 위젯의 위치와 크기 지정
        button = QPushButton("Button", self)
        button.setGeometry(100, 100, 100, 30) # x, y, width, height
        
        self.setWindowTitle("절대 좌표")
        self.resize(300, 280)
        self.show()
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
