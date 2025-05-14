from database import connect_db
from prettytable import PrettyTable

from datetime import datetime



def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_time_range(time_str):
    return '-' in time_str and len(time_str.split('-')) == 2





def add_shift(name, date, shift_type):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO shifts (employee_name, shift_date, shift_type) VALUES (?, ?, ?)",
                   (name, date, shift_type))
    conn.commit()
    conn.close()

def view_shifts():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM shifts")
    results = cursor.fetchall()
    conn.close()

    table = PrettyTable(["ID", "Name", "Date", "Type"])
    for row in results:
        table.add_row(row)
    print(table)
