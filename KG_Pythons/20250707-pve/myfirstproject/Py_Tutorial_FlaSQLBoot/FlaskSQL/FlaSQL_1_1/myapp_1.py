# Flask + SQLite3
from flask import Flask, render_template, request, redirect, url_for
import sqlite3, os

app = Flask(__name__)

def get_db():

    # 현재 스크립트 경로를 기준으로 경로 고정
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, 'db', 'db_test1.db')

    # 폴더 없으면 생성
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # 연결
    conn = sqlite3.connect(db_path)
    return conn

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            task TEXT
        )        
    ''')
    conn.commit()
    cur.close()
    conn.close()

@app.route('/')
def index():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=8081)
