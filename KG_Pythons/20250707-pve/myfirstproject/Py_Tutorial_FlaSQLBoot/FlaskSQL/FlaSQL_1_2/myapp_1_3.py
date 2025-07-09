# 길이가 정해지지 않은 테이블 구현

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
db_locale = r'FlaskSQL\FlaSQL_1_2\db\employees.db'

@app.route('/')
@app.route('/home')
def home_page():
    employee_data = query_contact_details()
    return render_template('home3.html', employee_data=employee_data)

def query_contact_details():
    conn = sqlite3.connect(db_locale)
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM contact_details
        """)
    employee_data = cur.fetchall()
    return employee_data

if __name__=='__main__':
    app.run()