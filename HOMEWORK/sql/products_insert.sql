import psycopg2


conn = psycopg2.connect('postgresql://minich:12345@localhost:5432/bh63')
with conn:
    with conn.cursor() as cur:
        cur.executemany('''
            INSERT INTO products(title, description, category_id) VALUES (%s, %s, %s);
            ''', (('ASUS TUF Gaming', 'Intel Core i7 11800H', 1),
                  ('Apple Macbook Pro 14', 'Apple M1 Pro', 1),
                  ('HP Victus', 'AMD Ryzen 5 5600H', 1),
                  ('Lenovo Legion 5','Intel Core i7 11800H', 1),
                  ('Xiaomi 12T Pro', 'Qualcomm Snapdragon 8+ Gen1', 2),
                  ('Apple iPhone 14', 'Apple A15 Bionic', 2),
                  ('Samsung Galaxy S22', 'Exynos 2200', 2),
                  ('Apple Watch SE 40', 'iOS', 3),
                  ('Apple Watch SE Nike', 'iOS', 3),
                  ('Samsung Galaxy Watch 4', 'Android', 3),
                  ('Honor Pad 8', 'Qualcomm Snapdragon 680', 4),
                  ('Apple iPad mini', 'Apple A15 Bionic', 4),
                  ('Apple iPad Air', 'Apple M1', 4),
                  ('Xiaomi Redmi', 'MediaTek Helio G99', 4),
                  ('Xiaomi Pad 5', '', 4)))
        conn.commit()
conn.close()
