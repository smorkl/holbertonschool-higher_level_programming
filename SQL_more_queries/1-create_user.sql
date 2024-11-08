-- the script create new user in localhost with  password--

CREATE USER 'user_0d_1'@'localhost' IDENTIFIED WITH mysql_native_password BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_1'@'localhost';