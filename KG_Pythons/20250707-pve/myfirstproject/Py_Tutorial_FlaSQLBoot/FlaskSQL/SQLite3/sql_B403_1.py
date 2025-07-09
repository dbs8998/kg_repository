import sqlite3

# DB 연결
conn = sqlite3.connect(f'FlaskSQL\SQLite3\db\cam_1.db')

# 커서 생성
cur = conn.cursor()

# 테이블 작업(생성)
# ID,Path,Post_id,Weight_cam
cur.execute('''
    CREATE TABLE IF NOT EXISTS cam_table (
        ID TEXT PRIMARY KEY,
        Path INTEGER NOT NULL,
        Post_id TEXT NOT NULL,
        Weight_cam INTEGER
    )
''')

# 커밋(저장하기)
conn.commit()
# DDL(create, alter, drop)은 다른 sql에서는 일반적으로 transaction과 무관하나 sqlite에서는 transaction에 포함된 작업이므로 커밋해줌.

## DB 내용 보기
# - 데이터 선택
cur.execute("SELECT * FROM users")
# - 내용 불러와서 출력하기
rows = cur.fetchall()
for row in rows:
    print(row)
    
# 커서/연결 닫기
cur.close()
conn.close()