import sqlite3

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()


cur.executemany('''
INSERT INTO statuses(name) VALUES(?);
''', (('active'',), ('deactive',), ('on_registration',)))
conn.commit()

