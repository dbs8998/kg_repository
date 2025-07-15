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
        
        label_widget = QLabel("Hello Robot")
        button_widget = QPushButton("Click")
        spinBox_widget = QSpinBox()
        comboBox_widget = QComboBox()
        
        checkBox_widget_1 = QCheckBox("Op 1")
        checkBox_widget_2 = QCheckBox("Op 2")
        
        radioB_widget_1 = QRadioButton("Target 1")
        radioB_widget_2 = QRadioButton("Target 2")

        comboBox_widget.addItem("Motor 1")
        comboBox_widget.addItem("Motor 2")
        comboBox_widget.addItem("Motor 3")

        win.addWidget(label_widget)
        win.addWidget(button_widget)
        win.addWidget(spinBox_widget)
        win.addWidget(comboBox_widget)
        win.addWidget(checkBox_widget_1)
        win.addWidget(checkBox_widget_2)
        win.addWidget(radioB_widget_1)
        win.addWidget(radioB_widget_2)

        self.setLayout(win)
        self.resize(500, 500)
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
