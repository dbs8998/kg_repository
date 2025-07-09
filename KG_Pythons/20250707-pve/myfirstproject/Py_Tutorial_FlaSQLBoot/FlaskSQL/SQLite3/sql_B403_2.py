import sqlite3

# DB 연결
conn = sqlite3.connect(f'FlaskSQL\SQLite3\db\cam_1.db')

# 커서 생성
cur = conn.cursor()

# 테이블 작업(생성)
cur.execute('''
    CREATE TABLE IF NOT EXISTS cam_table (
        ID TEXT PRIMARY KEY NOT NULL,
        Path INTEGER NOT NULL,
        Post_id TEXT NOT NULL,
        Weight_cam INTEGER
    );        
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    );
''')

try:
    # users에 데이터 삽입
    cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 20))
    cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Bob', 26))
    cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Charlie', 30))

    # cam_table에 데이터 삽입
    cur.execute("INSERT INTO cam_table (ID, Path, Post_id) VALUES (?, ?, ?)", ('TD_21', 3, '286'))

    # 저장
    conn.commit()
    
    # DB 내용 보기
    cur.execute("SELECT * FROM users")
    rows2 = cur.fetchall()
    for row2 in rows2:
        print(row2)
    
    cur.execute("SELECT * FROM cam_table")
    rows1 = cur.fetchall()
    for row1 in rows1:
        print(row1)
    
except Exception as e:
    conn.rollback()
    print(e)

finally:
    # 종료
    cur.close()
    conn.close()