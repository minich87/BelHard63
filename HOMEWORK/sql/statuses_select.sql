SELECT name FROM statuses;

SELECT COUNT(*) FROM statuses WHERE name = 'active' OR name = 'registr.';

SELECT users.name FROM statuses
    JOIN orders ON statuses.id = orders.status_id
    JOIN users ON orders.user_id = users.id
    WHERE statuses.name = 'deactive';

SELECT COUNT(*) FROM statuses
    JOIN orders ON statuses.id = orders.status_id
    JOIN users ON orders.user_id = users.id
    WHERE statuses.name = 'active';
