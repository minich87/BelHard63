SELECT * FROM categories ORDER BY name DESC;

SELECT name FROM categories WHERE name LIKE 'Lap___';

SELECT name FROM categories WHERE name LIKE '%mart%';

SELECT categories.name, products.title FROM categories
    JOIN products ON categories.id = products.category_id
    WHERE products.description IS NULL;

SELECT * FROM categories
    JOIN products ON categories.id = products.category_id
    JOIN order_items ON products.id = order_items.product_id
    JOIN orders ON order_items.id = orders.id
    WHERE products.title LIKE '%pple%';
