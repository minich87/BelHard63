CREATE TABLE IF NOT EXISTS products(
    id SERIAL PRIMARY KEY,
    title VARCHAR(36) NOT NULL,
    description VARCHAR(140),
    category_id SERIAL NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE RESTRICT
);
