import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QAction, QMessageBox
)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Menu Example")
        self.setGeometry(200, 200, 600, 400)

        # 메뉴바 생성
        menubar = self.menuBar()

        # File 메뉴
        file_menu = menubar.addMenu("File")

        new_action = QAction("New", self)
        new_action.triggered.connect(self.new_file)

        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        # View 메뉴
        help_menu = menubar.addMenu("View")

        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)

        help_menu.addAction(about_action)

        # Search 메뉴
        help_menu = menubar.addMenu("Search")

        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)

        help_menu.addAction(about_action)

        # Tools 메뉴
        help_menu = menubar.addMenu("Tools")

        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)

        help_menu.addAction(about_action)

        # Help 메뉴
        help_menu = menubar.addMenu("Help")

        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)

        help_menu.addAction(about_action)

    def new_file(self):
        QMessageBox.information(self, "New", "Create a new file.")

    def open_file(self):
        QMessageBox.information(self, "Open", "Open an existing file.")

    def show_about(self):
        QMessageBox.about(self, "About", "This is a PyQt5 menu example.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())