import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QColorDialog

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("QColorDialog Example")
        self.resize(300, 200)

        self.button = QPushButton("Choose Color")
        self.button.clicked.connect(self.show_color_dialog)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def show_color_dialog(self):
        color = QColorDialog.getColor()

        if color.isValid():
            print("Selected Color:", color.name())  # 예: "#ff0000"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())