--script that creates a table called first_table in the current database in your MySQL server
USE hbtn_test_db_4;
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);