CREATE TABLE Results(
    login TINYTEXT,
    weights JSON,
    time DATETIME,
    UNIQUE (time)
);
