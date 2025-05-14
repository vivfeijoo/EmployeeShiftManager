import sqlite3

def connect_db():
    return sqlite3.connect("shifts.db")

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS shifts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_name TEXT NOT NULL,
            shift_date TEXT NOT NULL,
            shift_type TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
