import sqlite3


conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

cur.execute('''
    SELECT name FROM statuses;
''')

cur.execute('''
    SELECT COUNT(*) FROM statuses
    WHERE name = 'active' OR name = 'on_registration';
''')

cur.execute('''
    SELECT users.name FROM statuses
    JOIN orders ON statuses.id = orders.status_id
    JOIN users ON orders.user_id = users.id
    WHERE statuses.name = 'deactive';
''')

cur.execute('''
    SELECT COUNT(*) FROM statuses
    JOIN orders ON statuses.id = orders.status_id
    JOIN users ON orders.user_id = users.id
    WHERE statuses.name = 'active';
''')