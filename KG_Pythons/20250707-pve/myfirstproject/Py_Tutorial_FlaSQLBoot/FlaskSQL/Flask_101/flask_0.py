# pip install flask
from flask import Flask

# Flask 객체 생성
app = Flask(__name__)

# @app.route('/') 데코레이터: '/' URL에서 호출하라. (그럼 리턴 줌.)
@app.route('/')
def hello():
    return 'hello world'

def main():
    app.run(debug=True, port=8081, host='0.0.0.0')
# 디버그 모드 활성화: 코드 변경 시 서버 자동 재시작 
# 서버가 8081 포트에서 실행되도록 지정


if __name__ == '__main__':
    main()
    