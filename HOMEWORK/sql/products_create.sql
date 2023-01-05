import psycopg2


conn = psycopg2.connect('postgresql://minich:12345@localhost:5432/bh63')
with conn:
    with conn.cursor() as cur:
        cur.execute('''
            CREATE TABLE IF NOT EXISTS products(
                id SERIAL PRIMARY KEY,
                title VARCHAR(36) NOT NULL,
                description VARCHAR(140),
                category_id SERIAL NOT NULL,
                FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE RESTRICT
        );
        ''')
        conn.commit()
conn.close()
