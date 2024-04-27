import sqlite3
from datetime import date

conn = sqlite3.connect('sqlite_db.db')


cursor = conn.cursor()

new_data = [
    ('lenin', 4400, date(2024, 9, 16), 'paid', None),
 
]

cursor.executemany('''
    INSERT INTO tax_record (company, amount, payment_date, status, due_date)
    VALUES (?, ?, ?, ?, ?)
''', new_data)
conn.commit()
conn.close()
