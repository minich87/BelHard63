import psycopg2

conn = psycopg2.connect('postgress://minich:12345@localhost:5432/bh63')
with conn:
    with conn.cursor() as cur:
        cur.execute('''SELECT * FROM categories ORDER BY name DESC;''')

        cur.execute('''SELECT name FROM categories WHERE name LIKE 'Lap___';''')

        cur.execute('''SELECT name FROM categories WHERE name LIKE '%mart%';''')

        cur.execute('''
            SELECT categories.name, products.title FROM categories
            JOIN products ON categories.id = products.category_id
             WHERE products.description IS NULL;
        ''')

        cur.execute('''
            SELECT * FROM categories
            JOIN products ON categories.id = products.category_id
            JOIN order_items ON products.id = order_items.product_id
            JOIN orders ON order_items.id = orders.id
            WHERE products.title LIKE '%pple%';
        ''')
conn.close()
