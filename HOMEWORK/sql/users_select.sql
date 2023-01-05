import sqlite3


conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()


cur.execute('''
    SELECT name FROM users WHERE email LIKE '%.by';
''')

cur.execute('''
    SELECT * FROM users WHERE id > 2;
''')

cur.execute('''
    SELECT * FROM users WHERE name IN ('Ann', 'Nick');
''')

cur.execute('''
    SELECT * FROM users
    JOIN orders ON users.id = orders.user_id
    WHERE orders.status_id = 1 AND orders.status_id = 3;
''')

cur.execute('''
    SELECT COUNT(*) FROM users
    INNER JOIN orders ON users.id = orders.user_id
    INNER JOIN statuses ON orders.status_id = statuses.id
    WHERE statuses.name = 'active';
''')
