import psycopg2


conn = psycopg2.connect('postgresql://minich:12345@localhost:5432/bh63')
with conn:
    with conn.cursor() as cur:
        cur.execute('''
            SELECT products.title FROM order_items
            JOIN products ON order_items.product_id = products.id
            JOIN orders ON order_items.order_id = orders.id
            JOIN statuses ON orders.status_id = statuses.id
            WHERE statuses.name = 'deactive';
        ''')

        cur.execute('''
            SELECT COUNT(*) FROM order_items
            JOIN products ON order_items.product_id = products.id
            JOIN orders ON order_items.order_id = orders.id
            JOIN statuses ON orders.status_id = statuses.id
            WHERE products.description LIKE '%Apple%' AND statuses.name = 'active';
        ''')

        cur.execute('''
            SELECT categories.name, COUNT(order_items.product_id) FROM order_items
            JOIN products ON order_items.product_id = products.id
            JOIN categories ON products.category_id = categories.id
            JOIN orders ON order_items.order_id = orders.id
            JOIN statuses ON orders.status_id = statuses.id
            WHERE statuses.name = 'active' GROUP BY categories.name;
        ''')

        cur.execute('''
            SELECT categories.name FROM order_items
            JOIN products ON order_items.product_id = products.id
            JOIN categories ON products.category_id = categories.id
            JOIN orders ON order_items.order_id = orders.id
            JOIN statuses ON orders.status_id = statuses.id
            WHERE products.description LIKE '%Apple%' AND statuses.name = 'deactive';
        ''')
conn.close
