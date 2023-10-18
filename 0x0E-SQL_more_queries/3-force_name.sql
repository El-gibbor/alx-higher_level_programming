-- creates a table in MYSQL server with the below fields
-- name field cant be NULL

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);