# Flask + SQLite3 + Bootstrap
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = r'FlaskSQL\FlaSQL_2\db\employees.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/add', methods=['POST'])
def add_employee():
    name = request.form['name']
    email = request.form['email']
    position = request.form['position']
    department = request.form['department']

    conn = get_db()
    cur = conn.cursor()
    cur.execute('INSERT INTO employees (name, email, position, department) VALUES (?, ?, ?, ?)',
              (name, email, position, department))
    conn.commit()
    conn.close()
    
    return redirect(url_for('home_page'))

@app.route('/display')
def display_employees():
    conn = get_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM employees')
    employees = cur.fetchall()
    conn.close()
    return render_template('display.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True)
