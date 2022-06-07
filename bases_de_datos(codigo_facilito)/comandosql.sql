#INSERT INTO usuarios(
#	nombre,apellido,fecha_nacimiento,telefono)
#   VALUES("Lucas","Moy","1998-04-04 10:00:00","123123123"); 
#DELETE FROM usuarios WHERE id=1;



#UPDATE usuarios SET nombre ="PEPE", 
#apellido="Angelini" where id = "1";

#Select * from usuarios;
#SELECT id, nombre, apellido FROM usuarios;

#SELECT * FROM usuarios WHERE id  = 1;

#SELECT nombre, apellido FROM usuarios WHERE id = 1;

#SELECT *FROM usuarios WHERE nombre LIKE "Luc%";

#select count(*) FROM usuarios WHERE apellido="MOY" AND nombre = "Lucas"

#WHERE funciona igual para el SELECT, DELETE, UPDATE

#CREATE TABLE publicaciones (
#	id int(11) NOT NULL AUTO_INCREMENT,
#    author_id int(11) NOT NULL,
#    titulo VARCHAR(150) NOT NULL,
#    texto TEXT NOT NULL,
#    PRIMARY KEY (id),#indica que el id es la primary key
#    FOREIGN KEY (author_id) REFERENCES usuarios(id) #indica que el author id es la foreign key, que hace 
#    #referencia a la columna de id de la tabla usuarios
#);

#INSERT INTO publicaciones (
#	author_id,titulo,texto)
#    VALUES(3,"Prueba de publicacion", "Texto de prueba");

#SELECT p.*, CONCAT(u.usuarios," ", u.apellido) as autor
#FROM publicaciones p, usuarios u 
#WHERE p.author_id = u.id;	#SE PUEDE OPTIMIZAR ESTO CON LOS JOINS que son igual que los setts de pyhton

#SQL PARA Estadisticas
#COUNT(*)cuenta la cantidad de filas
#MAX(*)Devuelve el maximo puntaje
#MIN(*)Devuelve el minimo puntaje
#AVG(*)Devuelve el promedio
#SUM(*)Devuelve una sumatoria de precios

#CREATE TABLE productos (
# id int(11) not null auto_increment,
# nombre varchar(100),
# precio DOUBLE,
# PRIMARY KEY (id)
#);

#SELECT * FROM productos; #agregamos datos desde la tabla perse
#select AVG(precio) FROM productos;

#SUBCONSULTAS
#SELECT * FROM publicaciones where author_id in(1,2,3);## idea de la subconsulta es obtener los datos de manera dinamica
#SELECT * FROM publicaciones where author_id in( ##coincidir el author_id con lo que esta aca en parentesis
#	select id from usuarios where nombre like "L%"
#);

#CONCATENAR CONSULTAS
SELECT * FROM usuarios WHERE nombre LIKE "L%"#NO PONER PUNTO Y COMA
UNION
SELECT * FROM usuarios WHERE nombre LIKE "P%"
UNION
SELECT * FROM usuarios WHERE nombre LIKE "R%";

#GROUP BY
select * from usuarios group by apellido;#traera los un unico dato de cada apellido diferente