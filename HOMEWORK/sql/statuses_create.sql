import sqlite3


conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()


cur.execute('''
CREATE TABLE IF NOT EXISTS statuses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(10) NOT NULL UNIQUE
);
''')
conn.commit()
