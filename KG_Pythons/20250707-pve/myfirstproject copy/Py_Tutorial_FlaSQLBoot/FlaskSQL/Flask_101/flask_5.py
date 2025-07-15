# 중복 코드 함수로 합침
from flask import Flask

app = Flask(__name__)

topics = [
    {'id':1, 'title': 'HTML', 'body': 'HTML is ...'},
    {'id':2, 'title': 'JAVA', 'body': 'JAVA is ...'},
    {'id':3, 'title': 'CSS', 'body': 'CSS is ...'}
]

def template(contents, content):
    return f'''
        <!doctype html>
        <html>
            <body>
                <h1><a href='/'>WEB</a></h1>
                <ol>
                    {contents}
                </ol>
                {content}
            </body>
        </html>
        '''
        
def getContents():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags

@app.route('/')
def index():
    return template(getContents(), '<h2>Welcome</h2>Be happy in my world!')

@app.route('/create/')
def create():
    return "Create"

@app.route('/read/<int:id>/')
def read(id):
    return template(getContents(), f'<h2>{topics[id-1]["title"]}</h2>{topics[id-1]["body"]}')

app.run(port=5001, debug=True)
