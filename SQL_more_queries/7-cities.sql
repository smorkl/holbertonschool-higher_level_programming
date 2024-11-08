-- This script creates a database and an associated table with variables that meet certain requirements id INT (starts at 1, primary key), state_id INT (not NULL), name VARCHAR (256), and the key state_id is associated with the table state_id

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa 
CREATE TABLES IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256)
    FOREIGN KEY (state_id) REFERENCES states(id)
)