# 수정: read로 들어가면 Create 아래에 Update 메뉴가 나타나고 
# Updata를 클릭하면 페이지 링크가 /read/id/ -> /update/id/로 변경됨
from flask import Flask, request, redirect

app = Flask(__name__)

nextId = 4
topics = [
    {'id':1, 'title': 'HTML', 'body': 'HTML is ...'},
    {'id':2, 'title': 'JAVA', 'body': 'JAVA is ...'},
    {'id':3, 'title': 'PYTHON', 'body': 'PYTHON is ...'}
]

def template(contents, content, id=None):
    contextUI = ''
    if id != None:
        contextUI = f'''
            <li><a href="/update/{id}/">Update</a></li>
        '''
    return f'''
        <!doctype html>
        <html>
            <body>
                <h1><a href='/'>WEB</a></h1>
                <ol>
                    {contents}
                </ol>
                {content}
                <ul>
                    <li><a href='/create/'>Create</a></li>
                    {contextUI}
                </ul>
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
    return template(getContents(), '<h2>Welcome</h2>Be happy in my world')

@app.route('/read/<int:id>/')
def read(id):
    return template(getContents(), f'<h2>{topics[id-1]["title"]}</h2>{topics[id-1]["body"]}', id)

@app.route('/create/', methods=['GET', 'POST'])
def create():
    print("Request Method: ", request.method)
    if(request.method == 'GET'):
        content = '''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit" value="Create1"></p>
            </form>
        '''
        return template(getContents(), content)
    elif request.method == "POST":
        global nextId
        title = request.form['title']
        body = request.form['body']
        newtopic = {'id':nextId, 'title':title, 'body':body}
        topics.append(newtopic)
        url = '/read/'+str(nextId)+'/'
        nextId += 1
        return redirect(url)

@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id):
    if request.method == "GET":
        title = ''
        body = ''
        for topic in topics:
            if id == topic['id']:
                title = topic['title']
                body = topic['body']
                break
        content = f'''
            <form action="/update/{id}/" method="POST">
                <p><input type="text" name="title" placeholder="title" value="{title}"></p>
                <p><textarea name="body" placeholder="body">{body}</textarea></p>
                <p><input type="submit" value="Update"></p>
            </form>
        '''
        return template(getContents(), content)
    elif request.method == "POST":
        global nextId
        title = request.form['title']
        body = request.form['body']
        for topic in topics:
            if id == topic['id']:
                topic['title'] = title
                topic['body'] = body
                break
        url = '/read/'+str(id)+'/'
        return redirect(url)

app.run(port=5001, debug=True)