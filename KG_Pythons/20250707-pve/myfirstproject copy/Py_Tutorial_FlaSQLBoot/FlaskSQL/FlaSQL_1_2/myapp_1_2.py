from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
db_locale = r'FlaskSQL\FlaSQL_1_2\db\employees.db'

@app.route('/')
@app.route('/home')
def home_page():
    # txt1 = "메시지 from Flask 파일(myapp_1_2.py) to html 파일(home2.html)"
    # return render_template('home2.html', employee_data=txt1)
    txt2 = query_contact_details()
    return render_template('home2.html', employee_data=txt2)

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