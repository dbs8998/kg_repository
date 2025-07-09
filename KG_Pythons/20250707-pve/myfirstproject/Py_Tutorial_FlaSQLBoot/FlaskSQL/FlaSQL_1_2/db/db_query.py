import sqlite3

db_loc = r'FlaskSQL\FlaSQL_1\db\employees.db'
conn = sqlite3.connect(db_loc)
cur = conn.cursor()

cur.execute("""
    SELECT * FROM contact_details        
    """)

employee_info = cur.fetchall()
for employee in employee_info:
    print(employee)

conn.commit()
conn.close()