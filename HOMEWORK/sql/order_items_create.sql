import psycopg2


conn = psycopg2.connect('postgresql://minich:12345@localhost:5432/bh63')
with conn:
    with conn.cursor() as cur:
        cur.execute('''
            CREATE TABLE IF NOT EXISTS order_items(
                id SERIAL PRIMARY KEY,
                order_id SERIAL NOT NULL,
                product_id SERIAL NOT NULL,
                FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE NO ACTION,
                FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
            );
        ''')
        conn.commit()
conn.close()
