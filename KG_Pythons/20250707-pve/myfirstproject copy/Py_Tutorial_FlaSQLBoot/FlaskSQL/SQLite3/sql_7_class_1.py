# https://www.youtube.com/watch?v=xqKjhucbQiA 
# Python에서는 DAO, DTO, VO가 별로 필요 없음.
# DAO(Data Access Object) : DB에 접근하는 기능
# DTO(Data Transfer Object) : 레이어 간 데이터 전송 정의
# VO(Value Object): 값을 표현하는 클래스

import sqlite3

class InfoVO:
    def __init__(self, no=None, name=None, age=None, btype=None, birth=None):
        self.no = no
        self.name = name
        self.age = age
        self.btype = btype
        self.birth = birth
    
    def __str__(self): # 쓰기 편한 변수로 변환
        return f"InfoVO(no={self.no}, name={self.name}, age={self.age}, btype={self.btype}, birth={self.birth})" # 미완성 여부 확인
    
# DAO: DB 접근/조작 기능 클래스
class InfoDAO:
    def __init__(self, conn):
        self.conn = conn
        self.cur = conn.cursor()
    
    def create(self, vo):
        self.cur.execute("INSERT INTO info (NAME, AGE, BTYPE, BIRTH) VALUES (?, ?, ?, ?)", (vo.name, vo.age, vo.btype, vo.birth))
        self.conn.commit()
        print("새 행 추가됨")
        
    def read_all(self):
        self.cur.execute("SELECT * FROM info")
        rows = self.cur.fetchall()
        result = []
        for row in rows:
            vo = InfoVO(*row)
            result.append(vo)
        return result
    
    def read_by_no(self, no):
        self.cur.execute("SELECT * FROM info WHERE NO=?", (no,))
        row = self.cur.fetchone()
        if row:
            vo = InfoVO(*row)
            return vo
        else:
            return None
    
    def read_by_name(self, name):
        self.cur.execute("SELECT * FROM info WHERE NAME=?", (name,))
        rows = self.cur.fetchall()
        result = []
        for row in rows:
            vo = InfoVO(*row)
            result.append(vo)
        return result
        
    def update(self, vo):
        self.cur.execute("UPDATE INFO SET NAME=?, AGE=?, BTYPE=?, BIRTH=? WHERE NO=?", (vo.name, vo.age, vo.btype, vo.birth, vo.no))
        self.conn.commit()
        print(f"{vo.no}번 행이 업데이트됨.")

    def delete(self, no):
        self.cur.execute("DELETE FROM info WHERE NO=?", (no,))
        self.conn.commit()
        print(f"{no}번 행 삭제됨.")
    
# DB 연결
conn = sqlite3.connect("FlaskSQL/SQLite3/db/info.db")

# cursor 생성
cur = conn.cursor()

# 테이블 생성
cur.execute("""DROP TABLE IF EXISTS info""")
cur.execute("""
    CREATE TABLE info (
        NO INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT(20) NOT NULL,
        AGE INTEGER CHECK (1 < AGE AND AGE < 120),
        BTYPE TEXT(2),
        BIRTH TEXT
    )            
""")

dao = InfoDAO(conn)

# 데이터 추가
dao.create(InfoVO(-1, 'John', 30, 'A', '1993-01-01')) # 이름 등 사용자에게 입력받은 정보

# 데이터 조회
rows = dao.read_all()
for row in rows:
    print(row)

# 데이터 수정
dao.update(InfoVO(1, "Jane", 25, '8', '1998-02-01'))

# 수정된 데이터 조회
rows = dao.read_by_name('Jane')
for row in rows:
    print(row)
    
# 데이터 삭제
dao.delete(1)

# 삭제된 데이터 조회
print(dao.read_by_no(1))

# 닫기
cur.close()
conn.close()
