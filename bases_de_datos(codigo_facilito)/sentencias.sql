/*  
    ¿Que tipo de entidades? autores
    Nombre: autores


Nombre 
Genero
Fecha de nacimiento
País de origen

columna y tipo de dato 
*/

DROP DATABASE IF EXISTS libreria_cf;
CREATE DATABASE IF NOT EXISTS libreria_cf;

USE libreria_cf;

CREATE TABLE IF NOT EXISTS autores(
    autor_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    nombres VARCHAR(25),
    apellidos VARCHAR(25),
    genero ENUM("M","F"),
    fecha_nacimiento DATE,
    fecha_creacion DATETIME DEFAULT current_timestamp
);

CREATE TABLE libros(
    libro_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    autor_id INT UNSIGNED NOT NULL,
    titulo VARCHAR(50) NOT NULL,
    descripcion VARCHAR(250),
    fecha_creacion DATETIME DEFAULT current_timestamp,
    FOREIGN KEY (autor_id) REFERENCES autores(autor_id)
);

INSERT INTO autores(id,nombres,apellidos,genero,fecha_nacimiento,pais_origen)
VALUES(1,"Test autor","Test autor","M","2018-01-30","Mexico" ),
    (2,"Leo","Messi","M","1986-01-30","Argentina" ),
    (3,"Cristiano","Ronaldo","M","1985-01-30","Portugal" ),
    (4,"Neymar","Jr","M","1993-01-30","Brasil" ),
    (5,"Kylian","Mbappe","M","1998-01-30","Francia" );

SELECT autor_id, titulo FROM libros WHERE titulo LIKE "H%" OR titulo LIKE "L%" OR titulo LIKE "E%"
 
SELECT titulo FROM libros WHERE titulo REGEXP "^[HLE]"

SELECT CONCAT(nombre," ", apellido) AS nombre_completo, "" AS email FROM autores
UNION
SELECT CONCAT(nombre," ", apellido) AS nombre_completo, email FROM usuarios;
