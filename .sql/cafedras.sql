CREATE TABLE Cafedras(
    id INT UNIQUE AUTO_INCREMENT,
    title TEXT,
    university TEXT(1024),
    firstData MEDIUMTEXT,
    secondData MEDIUMTEXT,
    weights JSON
);
