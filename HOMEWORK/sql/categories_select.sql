import sqlite3

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

cur.execute('''
    SELECT * FROM categories ORDER BY name DESC;
''')

cur.execute('''
    SELECT name FROM categories WHERE name LIKE 'Lap___';
''')

cur.execute('''
    SELECT name FROM categories WHERE name LIKE '%mart%';
''')

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
