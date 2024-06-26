-- Script to list all tables of a specified database

-- Check if the user provided a database name argument
-- You need to replace the variable `@database_name` with the actual database name passed as an argument

SET @database_name = 'Tables_in_mysql'; 
-- Generate the SQL command to show all tables in the specified database
SELECT CONCAT('SHOW TABLES IN `', @database_name, '`;') AS sql_command;
