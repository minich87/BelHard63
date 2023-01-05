import psycopg2


conn = psycopg2.connect('postgresql://minich:12345@localhost:5432/bh63')
with conn:
    with conn.cursor() as cur:
        cur.executemany('''
            INSERT INTO order_items(order_id, product_id) VALUES (?, ?);
            ''', ((1, 1),
                   (1, 1),
                   (1, 2),
                   (1, 2),
                   (2, 3),
                   (3, 3),
                   (4, 3),
                   (1, 4),
                   (3, 5),
                   (4, 6),
                   (1, 7),
                   (2, 7),
                   (1, 8),
                   (3, 8),
                   (1, 9),
                   (3, 10),
                   (2, 11),
                   (4, 11),
                   (2, 12),
                   (1, 13),
                   (3, 13),
                   (4, 14),
                   (1, 15)))
        conn.commit()
conn.close()
