import sqlite3


conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()


cur.executemany('''
INSERT INTO orders(user_id, status_id) VALUES (?, ?);
''', ((1, 1),
      (2, 2),
      (3, 1),
      (4, 1),
      (5, 3)))
conn.commit()
