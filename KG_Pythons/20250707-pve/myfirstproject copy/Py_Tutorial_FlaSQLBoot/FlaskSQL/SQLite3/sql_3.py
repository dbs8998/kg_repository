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

# 데이터 파라미터 리스트
data = [('John', 30), ('Jane', 24), ('Mike', 40), ('Hawx', 17)]

try:
    # 데이터 여러 개 삽입
    cur.executemany("INSERT INTO users (name, age) VALUES (?, ?)", data)
    # 커밋
    conn.commit()

    # 데이터 선택하여 보기
    cur.execute('SELECT * FROM users')
    rows = cur.fetchall()
    for row in rows:
        print(row)
except Exception as e:
    conn.rollback()
    print(e)
finally:
    cur.close()
    conn.close()
    