-- This script sets up a database called hbtn_0d_usa with a state table that has two columns: id, which is a unique auto-incrementing primary key, and name, which stores a state name

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
use hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256)
)
