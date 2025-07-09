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
        win_main = QGridLayout()
        
        wg_1 = QPushButton("Button 1")
        wg_2 = QPushButton("Button 2")
        wg_3 = QPushButton("Button 3")
        wg_4 = QPushButton("Button 4")
        # wg_5 = QPushButton("Button 5")
        # wg_6 = QPushButton("Button 6")
        # wg_7 = QPushButton("Button 7")

        win_main.addWidget(wg_1, 0, 0)
        win_main.addWidget(wg_2, 0, 1)
        win_main.addWidget(wg_3, 1, 0)
        win_main.addWidget(wg_4, 1, 1)
        # win_main.addWidget(wg_5, 2, 0)
        # win_main.addWidget(wg_6, 3, 1)
        # win_main.addWidget(wg_7, 4, 1)
        
        self.setLayout(win_main)
        self.resize(500, 500)
        self.show()
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
