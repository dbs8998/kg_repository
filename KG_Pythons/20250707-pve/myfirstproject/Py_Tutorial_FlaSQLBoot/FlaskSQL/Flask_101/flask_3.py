# Home 만들기 + 라우트 구현
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                <li><a href='/read/1/HTML 테스트입니다.'>HTML</a></li>
                <li><a href='/read/2/CSS 어렵다'>CSS</a></li>
                <li><a href='/read/3/JAVA PTSD'>Java</a></li>
            </ol>
            <h2>Welcome</h2>
            Welcome to My World!
        </body>
    </html>
    '''

@app.route('/create')
def create():
    return 'Create'

@app.route('/read/<id>/<text>')
def read(id, text):
    return f"Read {id} : {text}\n <a href='/'>Back</a>"

app.run(port=5001, debug=True)

