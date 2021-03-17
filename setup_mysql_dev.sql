-- Creats a MySQL server with a user test_dev
CREATE DATABASE IF NOT EXISTS cybercellcoin_dev;
CREATE USER IF NOT EXISTS 'cybercell'@'localhost' IDENTIFIED BY 'CyberCellCoin_dev_2021';
GRANT ALL PRIVILEGES ON cybercellcoin_dev.* TO 'cybercell'@'localhost';
GRANT SELECT ON performance_schema.* TO 'cybercell'@'localhost';
FLUSH PRIVILEGES;