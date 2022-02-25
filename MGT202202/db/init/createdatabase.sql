CREATE DATABASE testdb;
USE testdb;

CREATE TABLE user(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    password VARCHAR(255)
);

INSERT INTO user(name,password) VALUES('imoto','imotopassword');
INSERT INTO user(name,password) VALUES('yamada','yamadapassword');
INSERT INTO user(name,password) VALUES('suzuki','suzukipassword');
INSERT INTO user(name,password) VALUES('sasaki','sasakipassword');

GRANT ALL ON testdb.* TO test;
