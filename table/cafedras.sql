CREATE DATABASE expertsystem;

USE expertsystem;

CREATE TABLE Cafedras(
    id INT UNIQUE,
    title TEXT,
    university TEXT(1024),
    firstData MEDIUMTEXT,
    secondData MEDIUMTEXT,
    weights JSON
);
