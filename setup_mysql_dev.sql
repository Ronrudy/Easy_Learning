-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS el_dev_db;
CREATE USER IF NOT EXISTS 'el_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON `el_dev_db`.* TO 'el_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'el_dev'@'localhost';
FLUSH PRIVILEGES;
