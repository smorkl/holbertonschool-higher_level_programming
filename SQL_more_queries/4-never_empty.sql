-- the script  create the table id_not_null on your MySQL server con 2 variables id INT and name VARCHAR --

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
)