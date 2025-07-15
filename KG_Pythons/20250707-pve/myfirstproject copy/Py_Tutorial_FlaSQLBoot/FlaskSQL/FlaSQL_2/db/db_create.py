import sqlite3

def create_db():
    conn = sqlite3.connect(r'FlaskSQL\FlaSQL_2\db\employees.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            position TEXT NOT NULL,
            department TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    
if __name__=="__main__":
    create_db()