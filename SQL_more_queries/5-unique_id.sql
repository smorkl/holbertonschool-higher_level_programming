-- The script creates the table unique_id on the MySQL server with two variables id INT and name VARCHAR, ensuring that the value of id is unique --

CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
)