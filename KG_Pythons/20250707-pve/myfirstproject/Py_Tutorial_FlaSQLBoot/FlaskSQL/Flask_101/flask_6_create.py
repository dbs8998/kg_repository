# 중복 코드 함수로 합침 + Create
from flask import Flask, request, redirect

app = Flask(__name__)

nextId = 4  # 아래 3개에 새항목이 추가될 경우 새 ID 부여
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
                <ul>
                    <li><a href='/create/'>Create</a></li>
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
    return template(getContents(), '<h2>Welcome</h2>Be happy in my world!')

@app.route('/read/<int:id>/')
def read(id):
    return template(getContents(), f'<h2>{topics[id-1]["title"]}</h2>{topics[id-1]["body"]}')

@app.route('/create/', methods=['GET', 'POST'])
def create():
    print('Request Method: ', request.method)
    if(request.method == 'GET'):
        content = '''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit" value="Create1"></p>
            </form>
        '''
        return template(getContents(), content)
    elif request.method=='POST':
        global nextId
        title = request.form['title']
        body = request.form['body']
        newtopic = {'id': nextId, 'title': title, 'body':body}
        topics.append(newtopic)
        url = '/read/'+str(nextId)+'/'
        nextId += 1
        return redirect(url)
           
# 1. <form> </form> : 서버로 전송하는 양식
# 2. action=: 전송 경로(주소) 지정. action='경로' -> URL에 '경로', title, body 내용이 포함되어 전송됨. (디폴트 Get 방식: http://127.0.0.1:5001/경로/?title=aaa&body=bbb) 
# 3. method="POST": Post 방식으로 전환(method="GET") (<form action="경로" method="POST">: 이렇게 전송되는 데이터는 웹소스보기(F12)에서 payload 탭에서 확인할 수 있음.)
# POST하기 3단계
# - from flask import request
# - @app.route('/test/', methods=["GET", "POST"]) : 라우터에 메소드 추가
# - method="POST" : 메소드를 포스트로 지정하기
# 4. <input>: 짧은 글 입력창. <input type='text'></input>
# 5. <textarea></textarea>: 긴 글 입력창
# 6. placeholder='예시 글'
# 7. name="입력글의 정체": 입력하는 글이 title인지, id인지, body인지 규정함. 
# 8. type="submit" : 입력 버튼(디폴트 버튼명: 제출)
# 9. value="Create1": 입력 버튼명

app.run(port=5001, debug=True)
