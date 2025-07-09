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
        # win = QHBoxLayout()

        button_widget = QPushButton("Click")
        
        button_widget.setFixedSize(200, 50)
        button_widget.setFont(QFont("Times", 20, QFont.Bold))
        button_widget.setStyleSheet("background-color: green; color: white;")

        win.addWidget(button_widget)   # 화면에 추가

        self.setLayout(win)
        self.resize(500, 500)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
