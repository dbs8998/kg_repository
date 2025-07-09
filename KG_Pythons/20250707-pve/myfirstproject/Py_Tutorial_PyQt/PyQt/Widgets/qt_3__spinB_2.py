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
        
        spinBox_widget = QSpinBox()
        
        spinBox_widget.setRange(0, 4)
        spinBox_widget.setValue(1)
        spinBox_widget.setFixedWidth(300)     # 가로
        spinBox_widget.setFixedHeight(30)     # 세로
        # spinBox_widget.setFixedSize(80, 30) # 가로, 세로 한 번에
        spinBox_widget.setFont(QFont("courier", 20))
        spinBox_widget.setStyleSheet("background-color: #B5B2FF; color:black;")

        win.addWidget(spinBox_widget)

        self.setLayout(win)
        self.resize(500, 500)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
