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
        mainLayout = QVBoxLayout()
        
        # 테이블 생성
        table_widget = QTableWidget(3, 3) # 3x3 table
        # 테이블 디자인
        table_widget.setFont(QFont("Times", 20))
        table_widget.setFixedSize(300, 200)
        table_widget.setStyleSheet("background-color: #FAF4C0; color: #47C83E;")
        # 테이블 항목 추가
        for i in range(3):
            for j in range(3):
                item = QTableWidgetItem(f"cell {i+1}, {j+1}")
                item.setBackground(QColor('darkblue'))
                item.setForeground(QColor('white'))
                table_widget.setItem(i, j, item)

        mainLayout.addWidget(table_widget)

        self.setLayout(mainLayout)
        self.setWindowTitle("테이블 예시")
        self.resize(400, 400)
        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
