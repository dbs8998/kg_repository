# DB 클래스로 만들기
import sqlite3

class myDB():
    def __init__(self, table_name):
        self.table_name = table_name
    
        # DB 연결 및 커서 생성
        db_path = f"FlaskSQL/SQLite3/db/{self.table_name}.db"
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()

        # 테이블 생성
        self.cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                NO INTEGER PRIMARY KEY AUTOINCREMENT,
                NAME TEXT(20) NOT NULL,
                AGE INTEGER CHECK (1 < AGE AND AGE < 120),
                BTYPE TEXT(2),
                BIRTH TEXT
            )            
        """)

    def __del__(self):
        self.cur.close()
        self.conn.close()
    
    ## CRUD 함수 생성
    # 1. Create (= Insert)
    def create_row(self, name, age, btype, birth):
        self.cur.execute(f"INSERT INTO {self.table_name} (name, age, btype, birth) VALUES(?, ?, ?, ?)", (name, age, btype, birth))
        self.conn.commit()
    
    # 2. Read
    # 2.1 전체 조회
    def read_all(self):
        self.cur.execute(f"SELECT * FROM {self.table_name}")
        return self.cur.fetchall()
    # 2.2 행번호로 조회
    def read_no(self, no):
        self.cur.execute(f"SELECT * FROM {self.table_name} WHERE NO=?", (no,))
        return self.cur.fetchall()
    # 2.3 이름으로 조회
    def read_name(self, name):
        self.cur.execute(f"SELECT * FROM {self.table_name} WHERE NAME=?", (name,))
        return self.cur.fetchall()
    
    # 3. Update
    def update_row(self, no, name, age, btype, birth):
        self.cur.execute("UPDATE INFO SET NAME=?, AGE=?, BTYPE=?, BIRTH=? WHERE NO=?", (name, age, btype, birth, no))
        print(f"{no}번 행이 변경됨.")
        self.conn.commit()
        
    # 4. Delete
    def delete_row(self, no):
        self.cur.execute(f"DELETE FROM {self.table_name} WHERE NO=?", (no,))
        print(f"{no}번 행이 삭제됨.")
        self.conn.commit()
        
if __name__ == "__main__":
    runDB = myDB(table_name="info")

    # data_list = [('홍길동', 18, 'A', '1678-09-10'), ('강감찬', 21, 'B', '948-09-23'), ('신사임당', 34, 'O', '1504-07-26'), ('박사랑', 19, 'AB', '2002-01-11'), ('이순신', 27, 'A', '1545-09-28')]
    
    # for data in data_list:
    #     name, age, btype, birth = data
    #     runDB.create_row(name, age, btype, birth)

    rows = runDB.read_all()
    for row in rows:
        print(row)
    
    del runDB
