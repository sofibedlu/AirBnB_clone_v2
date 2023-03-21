-- setting up mysql for AirBnB_console_v2
-- creating a db 'hbnb_dev_db' if not exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- selecting the database
USE hbnb_test_db;
-- creating a user 'hbnb_test'
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- granting privilages
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost' WITH GRANT OPTION;
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- reloading the grant table
FLUSH PRIVILEGES;
