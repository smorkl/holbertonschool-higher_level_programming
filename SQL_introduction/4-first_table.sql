--script that creates a table called first_table in the current database in your MySQL server--
CREATE TABLE IF NOT EXISTS first_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);