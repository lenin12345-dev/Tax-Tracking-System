import sqlite3

conn = sqlite3.connect('sqlite_db.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tax_record (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        company TEXT NOT NULL,
        amount REAL NOT NULL,
        payment_date DATE,
        status TEXT,
        due_date DATE
    )
''')

conn.commit()
conn.close()
