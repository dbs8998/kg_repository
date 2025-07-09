# 기본 플라스크 구성 보기
from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    return 'random : <strong>'+str(random.random())+'</strong>'

app.run(port=5001, debug=True)