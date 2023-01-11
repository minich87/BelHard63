SELECT COUNT (*) FROM orders WHERE status_id = 1;

SELECT COUNT (*) FROM orders
    JOIN users ON orders.user_id = users.id
    WHERE users.email LIKE '%@gmail.com';

SELECT COUNT (*) FROM orders
    JOIN statuses ON orders.status_id = statuses.id
    WHERE statuses.name = 'on_registration';

SELECT COUNT (*) FROM orders
    JOIN order_items ON orders.id = order_items.order_id
    JOIN products ON order_items.product_id = products.id
    WHERE orders.status_id = 1 AND products.category_id = 4;
