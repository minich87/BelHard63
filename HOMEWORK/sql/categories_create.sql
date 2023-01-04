import sqlite3


conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()


cur.execute('''
CREATE TABLE IF NOT EXISTS categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(24) NOT NULL UNIQUE
);
''')
conn.commit()
