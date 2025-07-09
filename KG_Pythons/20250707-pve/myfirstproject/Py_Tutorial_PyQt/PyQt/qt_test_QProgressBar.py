import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar, QPushButton, QLabel
from PyQt5.QtCore import QTimer, Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Progress Bar with Timer")
        self.resize(300, 200)

        # 프로그레스 바
        self.progress = QProgressBar()
        self.progress.setMinimum(0)
        self.progress.setMaximum(100)
        self.progress.setValue(0)

        # 버튼
        self.button = QPushButton("Start")
        self.button.clicked.connect(self.start_progress)

        # 결과 표시할 라벨
        self.result_label = QLabel("")
        self.result_label.setStyleSheet("font-size: 16px; color: green;")
        self.result_label.setAlignment(Qt.AlignCenter)

        # 타이머
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)

        # 레이아웃
        layout = QVBoxLayout()
        layout.addWidget(self.progress)
        layout.addWidget(self.button)
        layout.addWidget(self.result_label)
        self.setLayout(layout)

    def start_progress(self):
        self.progress.setValue(0)
        self.result_label.setText("")  # 초기화
        self.timer.start(100)          # 100ms마다 timeout 발생

    def update_progress(self):
        val = self.progress.value() + 1
        if val > 100:
            self.timer.stop()
            self.result_label.setText("성공")
        else:
            self.progress.setValue(val)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
