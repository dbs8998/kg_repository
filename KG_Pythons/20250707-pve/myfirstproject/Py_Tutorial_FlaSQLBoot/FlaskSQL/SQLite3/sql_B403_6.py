# 함수를 이용한 DB 관리

# DB 연결
import sqlite3
conn = sqlite3.connect(r"FlaskSQL\SQLite3\db\cam_1.db")
cur = conn.cursor()

# 테이블 생성은 어차피 없으면 만드는 거라 함수로 하지 않는 것이 편할 수도 있음. 일단 학습을 위해 만듦.
def create_table():
    global conn  # conn을 재할당하거나 변경하지 않으므로 삭제 가능. 간혹 그런 경우가 있어서 명시해봄.
    try:
        # employee_info table 삭제 후 생성 
        # 주: where, 백업 없는 DB 업데이트와 삭제는 권장하지 않음. 불행해질 수 있음.
        cur.execute("""DROP TABLE IF EXISTS employee_info""")
        cur.execute('''
            CREATE TABLE employee_info (
                no INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT(20) NOT NULL,
                age INTEGER CHECK (1 < age AND age < 120),
                level TEXT(2),
                mobile TEXT,
                email TEXT NOT NULL
            );
        ''')

        # # 일반적인 생성방법 
        # cur.execute('''
        #     CREATE TABLE IF NOT EXISTS employee_info (
        #         no INTEGER PRIMARY KEY AUTOINCREMENT,
        #         name TEXT(20) NOT NULL,
        #         age INTEGER CHECK (1 < age AND 120 > age),
        #         level TEXT(2),
        #         mobile TEXT
        #         email TEXT NOT NULL
        #     )
        # ''') # 명령어 하나면 ";" 삭제 가능하지만 쓰는 것이 좋음
        
        conn.commit()
        print("DB 테이블 생성 성공")
    except:
        print("DB 테이블 생성 실패")

## CRUD 함수 생성
# 1. Create (= INSERT)
def create_info(name, age, level, mobile, email):
    cur.execute("INSERT INTO employee_info (name, age, level, mobile, email) VALUES(?, ?, ?, ?, ?)", (name, age, level, mobile, email))

# 2. Read
# 전체 조회
def read_info_all():
    cur.execute("SELECT * FROM employee_info")
    return cur.fetchall()

# key로 조회
def read_info_no(no):
    cur.execute("SELECT * FROM employee_info WHERE no=?", (no,))
    return cur.fetchall()

# 이름으로 조회
def read_info_name(name):
    cur.execute("SELECT * FROM employee_info WHERE name=?", (name,))
    return cur.fetchall()

# 조건으로 조회
def read_info_condition(name, no):
    cur.execute("SELECT * FROM employee_info WHERE no > ? AND name = ?", (no, name))
    return cur.fetchall()

# 3. Update
def update_info(no, name, age, level, mobile, email):
    cur.execute("UPDATE employee_info SET name=?, age=?, level=?, mobile=?, email=?", (name, age, level, mobile, email))
    print(f"{no}번 행이 변경됨")

# 4. Delete
def delete_info(no):
    cur.execute("DELETE FROM employee_info WHERE no=?", (no,))
    print(f'{no}번 행 삭제됨')


## Part 2: 함수 사용
# 데이터 준비 (이부분을 IoT 정보로 바꿔주면 됨!!!)
data_list = [
    ('홍길동', 18, 'A', '010-1234-1234', '111@email.com'), 
    ('강감찬', 21, 'B', '010-2345 -2345', '222@email.com'), 
    ('신사임당', 34, 'o', '010-3456-3456', '333@email.com'), 
    ('박사랑', 19, 'AB', '010-4567-4567', '444@email.com'), 
    ('이순신', 27, 'A', '010-5678-5678', '555@email.com')]

# 테이블 생성(클래스로 만들어 쓸 게 아니라면 굳이 테이블 생성을 함수로 만들어 실행할 필요는 없음)
create_table()

# 데이터 추가
for data in data_list:
    name, age, level, mobile, email = data
    create_info(name, age, level, mobile, email)

# # 데이터 조회
# rows = read_info_all()
# for row in rows:
#     print(row)

# # 데이터 수정 (수정의 경우 "no"를 꼭 써야 함!!)
# update_info(0, 'Hawx', 27, 'X', '010-7777-7777', '777@email.com')
# print(read_info_no(0))

# # 데이터 삭제
# delete_info(3)
# print(read_info_no(3))

cur.close()
conn.close()
