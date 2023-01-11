SELECT title, description FROM products WHERE description like '%Intel%';

SELECT * FROM products
    JOIN categories ON products.category_id = categories.id
    WHERE categories.id BETWEEN 2 AND 3;

SELECT * FROM products
    JOIN categories ON products.category_id = categories.id
    WHERE categories.name = 'Tablet';

SELECT title FROM products
    JOIN order_items ON products.id = order_items.product_id
    JOIN orders ON order_items.order_id = orders.id
    JOIN users ON orders.user_id = users.id
    WHERE users.name = 'Ann';

SELECT title FROM products
    JOIN categories ON products.category_id = categories.id
    JOIN order_items ON products.id = order_items.product_id
    JOIN orders ON order_items.order_id = orders.id
    JOIN users ON orders.user_id = users.id
    WHERE users.name = 'Alex' AND categories.name = 'Smartwatch';
