CREATE DATABASE expertsystem;
USE expertsystem;
CREATE TABLE Users(
    login VARCHAR (255),
    UNIQUE (login),
    password TINYTEXT,
    name TEXT(512),
    surname TEXT(512),
    patronymic TEXT(512),
    university TEXT(512)
);