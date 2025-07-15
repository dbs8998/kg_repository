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

        comboBox_widget = QComboBox()

        # 주: 배열을 넣을 경우 addItem -> addItems
        comboBox_widget.addItems(["Motor 1", "Motor 2", "Motor 3"])

        comboBox_widget.setFont(QFont("Helvetica", 20))
        comboBox_widget.setFixedSize(400, 40)
        comboBox_widget.setStyleSheet("color: black; background-color: lightgray;")
        
        win.addWidget(comboBox_widget) # 화면에 추가

        self.setLayout(win)
        self.resize(500, 500)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
        