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

        radioB_widget_1 = QRadioButton("Target 1")
        radioB_widget_2 = QRadioButton("Target 2")
        
        radioB_widget_1.setFont(QFont("SansSerif", 20))
        radioB_widget_1.setStyleSheet("background-color: black; color:white;")
        radioB_widget_1.setFixedSize(300, 50)
        
        radioB_widget_2.setFont(QFont("verdanda", 20))
        radioB_widget_2.setFixedWidth(300)
        radioB_widget_2.setFixedHeight(50)
        radioB_widget_2.setStyleSheet("color:green;")

        win.addWidget(radioB_widget_1)
        win.addWidget(radioB_widget_2)

        self.setLayout(win)
        self.resize(500, 500)
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
