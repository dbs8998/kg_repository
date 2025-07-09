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
        spinBox_widget = QSpinBox()

        win.addWidget(label_widget)
        win.addWidget(button_widget)
        win.addWidget(spinBox_widget)

        self.setLayout(win)
        self.resize(500, 500)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
