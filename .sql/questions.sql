CREATE TABLE Questions(
   id INT UNIQUE AUTO_INCREMENT,
   text TINYTEXT,
   tags JSON,
   weights JSON
);
