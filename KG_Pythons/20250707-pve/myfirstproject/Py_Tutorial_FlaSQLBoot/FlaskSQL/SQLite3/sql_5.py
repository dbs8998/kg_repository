# 커서가 있는 행부터 여러 행 가져오기: fetchmany()
# 커서가 있는 행부터 모든 행 가져오기: fetchall()
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
cur = conn.cursor()

try:
    # 테이블의 모든 행 선택
    cur.execute("SELECT * FROM users")
    rows = cur.fetchmany(3)

    # 출력
    for row in rows:
        print(row)

    print("----------")
    # 커서가 있는 행 이후 모든 행 가져오기
    rowAll = cur.fetchall()
    for row in rowAll:
        print(row)
    
except Exception as e:
    print(e)
finally:
    cur.close()
    conn.close()