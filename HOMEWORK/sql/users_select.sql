SELECT name FROM users WHERE email LIKE '%.by';

SELECT * FROM users WHERE id > 2;

SELECT * FROM users WHERE name IN ('Ann', 'Nick');

SELECT * FROM users
    JOIN orders ON users.id = orders.user_id
    WHERE orders.status_id = 1 AND orders.status_id = 3;

SELECT COUNT(*) FROM users
    INNER JOIN orders ON users.id = orders.user_id
    INNER JOIN statuses ON orders.status_id = statuses.id
    WHERE statuses.name = 'active';

