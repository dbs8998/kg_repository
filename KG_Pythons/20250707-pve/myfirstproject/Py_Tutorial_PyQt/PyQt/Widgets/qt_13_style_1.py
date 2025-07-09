import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QLabel, QPushButton, QSpinBox, QComboBox, QCheckBox, QRadioButton, QVBoxLayout)
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Label
        label = QLabel("This is a label")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont("Arial", 14, QFont.Bold))
        label.setStyleSheet("color: blue; background-color: yellow;")
        layout.addWidget(label)
        
        # Button
        button = QPushButton("Click Me")
        button.setFixedSize(100, 50)
        button.setFont(QFont("Times", 12))
        button.setStyleSheet("background-color: green; color: white;")
        layout.addWidget(button)
        
        # SpinBox
        spinbox = QSpinBox()
        spinbox.setRange(0, 100)
        spinbox.setValue(10)
        spinbox.setFixedSize(80, 30)
        spinbox.setFont(QFont("Courier", 10))
        layout.addWidget(spinbox)
        
        # ComboBox
        combobox = QComboBox()
        combobox.addItems(["Option 1", "Option 2", "Option 3"])
        combobox.setFont(QFont("Helvetica", 10))
        combobox.setStyleSheet("color: black; background-color: lightgray;")
        layout.addWidget(combobox)
        
        # CheckBox
        checkbox = QCheckBox("Accept Terms")
        checkbox.setFont(QFont("Verdana", 11))
        checkbox.setStyleSheet("color: purple;")
        layout.addWidget(checkbox)
        
        # RadioButton
        radiobutton = QRadioButton("Select Option")
        radiobutton.setFont(QFont("SansSerif", 10))
        radiobutton.setStyleSheet("color: brown;")
        layout.addWidget(radiobutton)
        
        self.setLayout(layout)
        self.setWindowTitle("해보자 Widget Styling")
        self.resize(500, 500)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
