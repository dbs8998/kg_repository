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

        date_widget = QDateEdit()
        time_widget = QTimeEdit()
        
        date_widget.setFont(QFont("verdanda", 20))
        date_widget.setFixedSize(200, 30)
        date_widget.setStyleSheet("background-color:#B2EBF4; color:black")

        time_widget.setFont(QFont("verdanda", 20))
        time_widget.setFixedSize(200, 30)
        time_widget.setStyleSheet("background-color:#B2EBF4; color:black;")

        win.addWidget(date_widget)
        win.addWidget(time_widget)

        self.setLayout(win)
        self.resize(500, 500)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
