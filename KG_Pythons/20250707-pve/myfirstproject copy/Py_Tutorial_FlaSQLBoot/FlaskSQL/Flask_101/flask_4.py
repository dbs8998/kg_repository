from flask import Flask

app = Flask(__name__)

topics = [
    {'id':1, 'title': 'HTML', 'body': 'HTML is ...'},
    {'id':2, 'title': 'JAVA', 'body': 'JAVA is ...'},
    {'id':3, 'title': 'CSS', 'body': 'CSS is ...'}
]

@app.route('/')
def index():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
        
    return f'''
        <!doctype html>
        <html>
            <body>
                <h1><a href='/'>WEB</a></h1>
                <ol>
                    {liTags}
                </ol>
                <h2>Welcome</h2>
                Welcome to my world!
            </body>
        </html>
        '''

@app.route('/create/')
def create():
    return "Create"

@app.route('/read/<int:id>/')
def read(id):
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return f'''
        <!doctype html>
        <html>
            <body>
                <h1><a href='/'>WEB</a></h1>
                <ol>
                    {liTags}
                </ol>
                <h2>{topics[id-1]["title"]}</h2>
                {topics[id-1]["body"]}
            </body>
        </html>
        '''

app.run(port=5001, debug=True)
