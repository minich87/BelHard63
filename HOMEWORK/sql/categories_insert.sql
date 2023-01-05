import sqlite3

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()


cur.executemany('''
INSERT INTO categories(name) VALUES(?);
''', (('Laptop',), ('Smartphone',), ('Smartwatch',), ('Tablet',)))
conn.commit()
