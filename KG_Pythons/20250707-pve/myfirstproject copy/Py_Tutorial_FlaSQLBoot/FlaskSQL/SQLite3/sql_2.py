import os
import sqlite3

# # DB 연결(절대경로)
# conn = sqlite3.connect(r'C:\Users\dbstj\workplace\kg_repository\KG_Pythons\20250707-pve\myfirstproject\Py_Tutorial_FlaSQLBoot\FlaskSQL\SQLite3\db\test1.db')

# 현재 스크립트 경로를 기준으로 경로 고정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'db', 'test1.db')

# 폴더 없으면 생성
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# 연결
conn = sqlite3.connect(db_path)

# 커서 생성
cur = conn.cursor()

# 테이블 작업(생성)
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL    
    )
''')

try:
    # 데이터 삽입
    cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 20))
    cur.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Bob', 26))
    cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Charlie", 30))
    # 커밋
    conn.commit()
    
    # DB 내용 보기
    cur.execute("SELECT * FROM users")    
    rows = cur.fetchall()
    for row in rows:
        print(row)

# 문제 발생 시 롤백
except Exception as e:
    conn.rollback()
    print(e)
finally:
    # 커서/연결 닫기
    cur.close()
    conn.close()

