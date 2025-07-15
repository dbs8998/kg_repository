import sqlite3

def create_db():
    db_loc = 'FlaskSQL/FlaSQL_1_2/db/employees.db'

    conn = sqlite3.connect(db_loc)
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE contact_details (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            mobile TEXT,
            email TEXT,
            address TEXT
        )        
    ''')

    conn.commit()
    conn.close()

if __name__=="__main__":
    create_db()