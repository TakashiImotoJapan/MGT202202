CREATE DATABASE testdb;
USE testdb;

CREATE TABLE user(
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255),
    password VARCHAR(255)
);

INSERT INTO user(username,password) VALUES('imoto','imotopassword');
INSERT INTO user(username,password) VALUES('yamada','yamadapassword');
INSERT INTO user(username,password) VALUES('suzuki','suzukipassword');
INSERT INTO user(username,password) VALUES('sasaki','sasakipassword');

GRANT ALL ON testdb.* TO test;
