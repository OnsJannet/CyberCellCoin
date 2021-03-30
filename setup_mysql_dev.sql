-- Creats a MySQL server with a user test_dev
CREATE DATABASE IF NOT EXISTS CCC;
CREATE USER IF NOT EXISTS 'cybercell'@'localhost' IDENTIFIED BY 'CyberCellCoin_dev_2021';
GRANT ALL PRIVILEGES ON CCC.* TO 'cybercell'@'localhost';
GRANT SELECT ON performance_schema.* TO 'cybercell'@'localhost';
FLUSH PRIVILEGES;

--set up tables in database to work properly
CREATE TABLE users(name varchar(30), email varchar(30), username varchar(20), password varchar(68));
CREATE TABLE blockchain(number varchar(30), hash varchar(68), previous varchar(68), data varchar(100), nonce varchar(30));
-- root user should do this
GRANT ALL PRIVILEGES ON CCC.* TO 'cybercell'@'localhost';