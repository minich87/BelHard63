import sqlite3


conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()


cur.executemany('''
INSERT INTO users(name, email) VALUES(?, ?);
''', (('Alex', 'a.ivanov@mail.com'),
      ('Ann', 'ann87@gmail.com'),
      ('Nick', 'Nixs@tut.by'),
      ('Maksim', 'Max_lite@gmail.com'),
      ('Vasya', 'v.smirnoff@gmail.com')))
conn.commit()
