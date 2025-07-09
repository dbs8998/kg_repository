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

        checkBox_widget_1 = QCheckBox("Op 1")
        checkBox_widget_2 = QCheckBox("Op 2")

        checkBox_widget_1.setFont(QFont("verdanda", 20))
        checkBox_widget_1.setFixedSize(300, 30)
        checkBox_widget_1.setStyleSheet("background-color:#FFB2F5; color: black;")
        
        checkBox_widget_2.setFont(QFont("verdanda", 20))
        checkBox_widget_2.setFixedWidth(400)
        checkBox_widget_2.setFixedHeight(30)
        checkBox_widget_2.setStyleSheet("background-color: #FFD9FA; color:black;")
        
        win.addWidget(checkBox_widget_1)
        win.addWidget(checkBox_widget_2)
        
        self.setLayout(win)
        self.resize(500, 500)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
        