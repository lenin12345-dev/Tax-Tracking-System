import sqlite3
from datetime import date

conn = sqlite3.connect('sqlite_db.db')

cursor = conn.cursor()

row = 44
dueDate = date(2024, 6, 15)

cursor.execute('''
    UPDATE tax_record
    SET due_date = ?
    WHERE id = ?
''', (dueDate, row))


conn.commit()
conn.close()
