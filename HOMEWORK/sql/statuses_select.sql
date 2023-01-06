import psycopg2


conn = psycopg2.connect('postgresql://minich:12345@localhost:5432/bh63')
with conn:
    with conn.cursor() as cur:
        cur.execute('''SELECT name FROM statuses;''')

        cur.execute('''
            SELECT COUNT(*) FROM statuses
            WHERE name = 'active' OR name = 'registr.';
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
conn.close()
