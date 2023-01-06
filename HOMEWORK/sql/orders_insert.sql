import psycopg2


conn = psycopg2.connect('postgresql://minich:12345@localhost:5432/bh63')
with conn:
    with conn.cursor() as cur:
        cur.executemany('''
        INSERT INTO orders(user_id, status_id) VALUES (%s, %s);
        ''', ((1, 1),
              (2, 2),
              (3, 1),
              (4, 1),
              (5, 3)))
        conn.commit()
conn.close()
