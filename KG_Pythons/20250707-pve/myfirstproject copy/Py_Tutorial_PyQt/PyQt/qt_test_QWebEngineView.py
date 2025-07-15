
# QWebEngineView는 PyQt5(Qt)의 위젯 중 하나:

# “앱 안에 웹 브라우저를 내장할 수 있게 해 주는 위젯”

# ✅ 한 줄 정의
# ✅ QWebEngineView = 웹 페이지(HTML, CSS, JavaScript)를 네 앱 안에서 그대로 띄워 주는 브라우저 뷰

# ✅ 어디서 나옴?
# Qt가 제공하는 모듈 중 QtWebEngine 안에 있음

# Qt 5.6 이후 → Chromium(크롬) 엔진을 내장

# ✅ 무엇을 할 수 있나?
# ✔ 웹사이트 보여주기
# ✔ 로컬 HTML 파일 렌더링
# ✔ JavaScript 실행
# ✔ HTML5/CSS3 지원 (크롬 엔진이니까 최신)
# ✔ Python ↔ JavaScript 통신

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl




class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QWebEngineView Example")
        self.resize(1200, 800)

        # 웹뷰 위젯 생성
        self.webview = QWebEngineView()
        self.webview.load(QUrl("https://www.python.org"))

        # 메인 윈도우에 추가
        self.setCentralWidget(self.webview)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec_())