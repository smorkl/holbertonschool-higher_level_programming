-- This script will list all records in the second_table table of the hbtn_0c_0 database on your MySQL server and it has to be only the ones that match rows with value --

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;