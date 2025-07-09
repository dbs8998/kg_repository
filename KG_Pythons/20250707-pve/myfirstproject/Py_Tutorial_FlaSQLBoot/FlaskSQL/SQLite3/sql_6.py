# 함수를 이용한 DB 관리

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

# INFO Table 삭제 후 생성 
# (참고: 테이블명, 컬럼명 등은 대소문자 구분 안 함. PostgreSQL은 함.)
cur.execute("""DROP TABLE IF EXISTS info""")
cur.execute('''
    CREATE TABLE info (
        NO INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT(20) NOT NULL,
        AGE INTEGER CHECK (1 < AGE AND AGE < 120),
        BTYPE TEXT(2),
        BIRTH TEXT
    );
''')

## 아래처럼 해도 좋음
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS info (
#         NO INTEGER PRIMARY KEY AUTOINCREMENT,
#         NAME TEXT(20) NOT NULL,
#         AGE INTEGER CHECK (1 < AGE AND AGE < 120),
#         BTYPE TEXT(2),
#         BIRTH TEXT
#     )            
# ''')

## CRUD 함수 생성
# C: CREATE (= INSERT)
def c_info(name, age, btype, birth):
    cur.execute("INSERT INTO info (NAME, AGE, BTYPE, BIRTH) VALUES(?, ?, ?, ?)", (name, age, btype, birth))
    conn.commit()
    print("새 정보가 추가됨")
    
## R: READ 
# 전체 조회
def r_info_all():
    cur.execute("SELECT * FROM INFO")
    return cur.fetchall()

# key로 조회
def r_info_no(no):
    cur.execute("SELECT * FROM INFO WHERE NO=?", (no,))
    return cur.fetchall()

# 이름으로 조회
def r_info_name(name):
    cur.execute("SELECT * FROM INFO WHERE NAME=?", (name,))
    return cur.fetchall()

# 조건으로 조회
def r_info_condition(name, no):
    cur.execute("SELECT * FROM info WHERE no > ? AND name = ?", (no, name))
    return cur.fetchall()

# U: UPDATE
def u_info(no, name, age, btype, birth):
    cur.execute("UPDATE info SET NAME=?, AGE=?, BTYPE=?, BIRTH=? WHERE NO=?", (name, age, btype, birth, no))
    print(f"{no}번 행이 변경됨.")
# 주: '?' 순서대로임!! 함수의 인자 순서가 아님. 함수 사용 시에는 인자 순서대로이므로 주의할 것.

# D: DELETE
def d_info(no):
    cur.execute("DELETE FROM info WHERE NO=?", (no,))
    print(f"{no}번 행이 삭제됨.")
    
## 함수 사용
data_list = [('홍길동', 18, 'A', '1678-09-10'), ('강감찬', 21, 'B', '948-09-23'), ('신사임당', 34, 'O', '1504-07-26'), ('박사랑', 19, 'AB', '2002-01-11'), ('이순신', 27, 'A', '1545-09-28')]

# 데이터 추가
for data in data_list:
    name, age, btype, birth = data
    c_info(name, age, btype, birth)

# 데이터 조회
rows = r_info_all()
for row in rows:
    print(row)

# # 데이터 수정
# u_info(3, 'Hawx', 25, 'X', '2000-01-01')
# print(r_info_name("Hawx"))

# # 데이터 삭제
# d_info(3)
# print(r_info_no(3))

cur.close()
conn.close()

##################################
## SELECT 필수 구문 ###############
'''
"SELECT * FROM table_name"
"SELECT * FROM table_name WHERE id > ? AND name = ?", (1, '이순신')
"SELECT * FROM table_name ORDER BY id DESC"
"SELECT * FROM table_name LIMIT 2" # 처음 2개만 가져오기
"SELECT * FROM table_name LIMIT 1, 3" # 2~3번째 행 (2번, 3번 인덱스 행)  
"SELECT id, title FROM table_name" # id, title 열 모두
'''
