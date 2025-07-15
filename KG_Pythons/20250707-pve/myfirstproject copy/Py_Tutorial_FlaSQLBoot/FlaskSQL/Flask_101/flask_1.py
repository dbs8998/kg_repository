# pip install flask
from flask import Flask 

# Flask 객체 생성
app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello page'

@app.route('/1')
def page1():
    return 'page 1'

@app.route('/2')
def page2():
    return 'page 2'

def main():
    app.run(debug=True, port=8081, host='0.0.0.0')

if __name__ == '__main__':
    main()
    
#  ✅ 1️⃣ if __name__ == '__main__': 이거 왜 쓰는가?
# ✔️ 파이썬 모듈의 __name__ 변수
# 파이썬에서는 스크립트를 실행할 때 __name__ 이라는 특별한 변수가 자동으로 정의됨

# 실행 방식에 따라 값이 달라짐

# 상황	__name__ 값
# 파일을 직접 실행할 때	'__main__'
# 다른 모듈이 import할 때	그 모듈의 파일명(모듈명)

# ✅ 예제
# app.py를 직접 실행:


# python app.py
# → __name__ == '__main__' → True

# 다른 스크립트에서 import app:


# import app
# → app.__name__ == 'app' → False

# ✅ Flask 코드에서는 왜 쓰나?

# 직접 실행할 때만 서버가 뜨도록 하기 위해

# 라이브러리처럼 import해서 다른 코드에서 재사용할 때는 app.run()이 실행되지 않게 함

# ✅ 간단한 비유

# “이 파일이 메인 프로그램이면 서버 켜라.
# 라이브러리로 쓰면 서버는 켜지지 마라!”

# ✅ Flask 예제 코드에서:


# if __name__ == '__main__':
#     main()
# → 이 코드는 이 파일을 직접 실행할 때만 Flask 서버를 시작하게 만드는 안전장치



# ✅ 2️⃣ @app.route()의 역할
# ✔️ Flask의 핵심: “라우팅(Routing)”
# 라우팅 = URL 경로와 처리 함수(뷰 함수)를 연결하는 것

# ✅ @app.route('/')

# Flask의 데코레이터 문법

# 아래 함수를 “/” 경로의 핸들러로 등록

# ✅ 예제 코드

# @app.route('/')
# def hello():
#     return 'hello page'
# → 브라우저에서

# http://localhost:8081/
# 접속 시


# hello page
# 가 출력

# ✅ 다른 경로 예

# python
# 복사
# 편집
# @app.route('/1')
# def page1():
#     return 'page 1'
# 접속 URL:

# http://localhost:8081/1
# → 결과:


# page 1
# ✅ 어떻게 작동하나?
# Flask 내부적으로


# 요청 URL → 등록된 함수
# 를 매핑 테이블로 관리

# URL 경로	함수 이름	리턴 내용
# /	hello	'hello page'
# /1	page1	'page 1'
# /2	page2	'page 2'

# ✅ 비유

# @app.route() = “주소를 함수와 연결해 주는 표지판”

# ✅ 한 문장 요약
# __name__ == '__main__': 이 파일을 메인으로 실행할 때만 서버를 실행하도록 조건 거는 것

# @app.route(): 특정 URL 경로로 접속하면 어떤 함수를 실행할지 Flask에게 알려주는 것   