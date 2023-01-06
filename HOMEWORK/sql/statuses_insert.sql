import psycopg2

conn = psycopg2.connect('postgresql://minich:12345@localhost:5432/bh63')
with conn:
    with conn.cursor() as cur:
        cur.executemany('''INSERT INTO statuses(name) VALUES(%s);
            ''', (('active',), ('deactive',), ('registr.',)))
        conn.commit()
conn.close()
