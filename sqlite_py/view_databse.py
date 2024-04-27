import sqlite3

conn = sqlite3.connect('sqlite_db.db')
cursor = conn.cursor()


cursor.execute('SELECT * FROM tax_record')

records = cursor.fetchall()


for record in records:
    print(record)


conn.close()
