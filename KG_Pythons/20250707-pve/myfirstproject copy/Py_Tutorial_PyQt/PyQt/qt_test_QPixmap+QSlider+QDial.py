import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QDial, QSlider, QPushButton, QCalendarWidget
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsBlurEffect

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image with Dial, Slider, Buttons, and Calendar")
        self.resize(500, 800)

        # ✅ 모드 상태 ("size" or "blur")
        self.mode = "size"

        # ✅ 메인 레이아웃
        main_layout = QVBoxLayout()

        # ✅ 이미지 라벨
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)

        # ✅ 이미지 로드 (경로는 너 컴퓨터 경로로 맞게 변경!)
        self.original_pixmap = QPixmap(r"C:\Users\dbstj\workplace\kg_repository\KG_Pythons\example1.jpg")
        self.current_size = 200
        self.update_image()
        self.image_label.setFixedSize(300, 300)
        self.image_label.setScaledContents(False)

        # ✅ 다이얼
        self.dial = QDial()
        self.dial.setMinimum(50)
        self.dial.setMaximum(300)
        self.dial.setValue(200)
        self.dial.valueChanged.connect(self.on_value_changed)

        # ✅ 슬라이더
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(50)
        self.slider.setMaximum(300)
        self.slider.setValue(200)
        self.slider.valueChanged.connect(self.on_value_changed)

        # ✅ 버튼들
        self.size_button = QPushButton("크기 변경 모드")
        self.size_button.clicked.connect(self.set_size_mode)

        self.blur_button = QPushButton("흐림 변경 모드")
        self.blur_button.clicked.connect(self.set_blur_mode)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.size_button)
        button_layout.addWidget(self.blur_button)

        # ✅ 다이얼과 슬라이더 한 줄에 배치
        control_layout = QHBoxLayout()
        control_layout.addWidget(self.dial)
        control_layout.addWidget(self.slider)

        # ✅ 달력 위젯
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.clicked.connect(self.update_selected_date)

        # ✅ 선택 날짜 라벨
        self.date_label = QLabel("Selected Date: ")
        self.date_label.setAlignment(Qt.AlignCenter)
        self.date_label.setStyleSheet("font-size: 16px; color: blue;")

        # ✅ 메인 레이아웃 구성
        main_layout.addWidget(self.image_label)
        main_layout.addLayout(button_layout)
        main_layout.addLayout(control_layout)
        main_layout.addWidget(self.calendar)
        main_layout.addWidget(self.date_label)

        self.setLayout(main_layout)

    def set_size_mode(self):
        self.mode = "size"
        self.dial.setMinimum(50)
        self.dial.setMaximum(300)
        self.dial.setValue(self.current_size)
        self.slider.setMinimum(50)
        self.slider.setMaximum(300)
        self.slider.setValue(self.current_size)

    def set_blur_mode(self):
        self.mode = "blur"
        # 흐림 정도는 0~30 정도로 설정
        self.dial.setMinimum(0)
        self.dial.setMaximum(30)
        self.dial.setValue(0)
        self.slider.setMinimum(0)
        self.slider.setMaximum(30)
        self.slider.setValue(0)
        self.clear_blur()

    def on_value_changed(self, value):
        # 다이얼과 슬라이더 값 동기화
        self.dial.blockSignals(True)
        self.dial.setValue(value)
        self.dial.blockSignals(False)

        self.slider.blockSignals(True)
        self.slider.setValue(value)
        self.slider.blockSignals(False)

        if self.mode == "size":
            self.current_size = value
            self.update_image()
            self.clear_blur()
        elif self.mode == "blur":
            self.apply_blur(value)

    def update_image(self):
        scaled = self.original_pixmap.scaled(self.current_size, self.current_size, Qt.KeepAspectRatio)
        self.image_label.setPixmap(scaled)

    def apply_blur(self, radius):
        blur = QGraphicsBlurEffect()
        blur.setBlurRadius(radius)
        self.image_label.setGraphicsEffect(blur)

    def clear_blur(self):
        self.image_label.setGraphicsEffect(None)

    def update_selected_date(self, date):
        self.date_label.setText(f"Selected Date: {date.toString('yyyy-MM-dd')}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
