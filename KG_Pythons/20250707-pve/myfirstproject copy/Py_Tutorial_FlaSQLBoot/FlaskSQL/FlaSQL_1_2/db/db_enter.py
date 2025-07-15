import sqlite3

db_loc = r'FlaskSQL\FlaSQL_1_2\db\employees.db'

conn = sqlite3.connect(db_loc)
cur = conn.cursor()

# DB에 입력
cur.execute("""
    INSERT INTO contact_details(name, mobile, email, address) VALUES
    ('Liam', '010-1234-1234', '111@111.com', '11 Dawning St. Suji'),
    ('David', '010-2345-2345', '222@222.com', '23 Stardust Way Qynnum'),
    ('Ayra', '010-3456-3456', '333@333.com', '13 Dark Way Gangnam')
    """)

# # DB에서 불러오기 (주: 위 "DB에 입력" 주석처리하고 불러올것!)
# cur.execute("""
#     SELECT * FROM contact_details
#     """)
## 불러온 Data 출력하기 1
# employee_info = cur.fetchall()
# print(employee_info)

## 불러온 Data 출력하기 2
# employee_info = cur.fetchall()
# for employee in employee_info:
#     print(employee)

conn.commit()
conn.close()