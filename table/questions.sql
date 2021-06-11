CREATE DATABASE expertsystem;

USE expertsystem;

CREATE TABLE Questions(
   id INT UNIQUE,
   text TINYTEXT,
   tags JSON,
   weights JSON
);
