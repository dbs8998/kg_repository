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
        
        list_widget = QListWidget()
        # item_1 = QListWidgetItem("Dog")
        # itme_2 = QListWidgetItem("Cat")

        # list_widget.addItems([item_1, itme_2])
        list_widget.addItems(["Dog", "Cat", "Dino"]) # itmes인 것 주의
        
        list_widget.setFont(QFont("Arial", 20, QFont.Bold))
        list_widget.setFixedSize(300, 200)
        list_widget.setStyleSheet("background-color: #B2EBF4; color: #5F00FF;")
        
        win.addWidget(list_widget)
        
        self.setLayout(win)
        self.resize(500, 500)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
