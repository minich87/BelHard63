import psycopg2


conn = psycopg2.connect('postgresql://minich:12345@localhost:5432/bh63')
with conn:
    with conn.cursor() as cur:
        cur.execute('''
            CREATE TABLE IF NOT EXISTS orders(
                id SERIAL PRIMARY KEY,
                user_id SERIAL NOT NULL,
                status_id SERIAL NOT NULL,
                 FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
                    FOREIGN KEY (status_id) REFERENCES statuses(id) ON DELETE NO ACTION
            );
            ''')
        conn.commit()
conn.close()
