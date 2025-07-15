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

        label_widget = QLabel("Hello Robot")
        button_widget = QPushButton("Click")

        win.addWidget(label_widget)    # 화면에 추가
        win.addWidget(button_widget)   # 화면에 추가

        self.setLayout(win)
        self.resize(500, 500)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
        