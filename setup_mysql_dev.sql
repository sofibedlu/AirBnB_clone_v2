-- creating a db 'hbnb_dev_db' if not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- selecting the database
USE hbnb_dev_db;
-- creating a user 'hbnb_dev'
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- granting privilages
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost' WITH GRANT OPTION;
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- reloading the grant table
FLUSH PRIVILEGES;
