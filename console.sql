CREATE DATABASE expertsystem;
USE expertsystem;
CREATE TABLE Questions(
    id int UNIQUE,
    text TINYTEXT,
    tags JSON,
    weights JSON
);
INSERT INTO Questions VALUES (2, '', '[  ]', '{

  }');

SELECT * FROM Questions;