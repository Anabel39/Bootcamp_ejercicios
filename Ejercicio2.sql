/*EJERCICIO 2*/
/*Crea una base de datos llamada "MiBaseDeDatos".*/
CREATE DATABASE MiBaseDeDatos;
/*Crea una tabla llamada "Usuarios" con las columnas: "id" (entero, clave primaria), "nombre" (texto) y "edad" (entero).*/
CREATE TABLE IF NOT EXISTS usuarios (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR (255),
  edad INT
)
/*Inserta dos registros en la tabla "Usuarios".*/
INSERT INTO usuarios (nombre, edad,)
VALUES ('Annie', 30), ('Antonio', 25,)
/*Actualiza la edad de un usuario en la tabla "Usuarios".*/
UPDATE usuarios
SET edad = 29
WHERE id = 1
/*Elimina un usuario de la tabla "Usuarios".*/
DELETE FROM usuarios
WHERE id = 1
/*Crea una tabla llamada "Ciudades" con las columnas: "id" (entero, clave primaria), "nombre" (texto) y "pais" (texto).*/
CREATE TABLE IF NOT EXISTS ciudades (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR (255),
  pais VARCHAR (255)
)
/*Inserta al menos tres registros en la tabla "Ciudades".*/
INSERT INTO ciudades (nombre, pais)
VALUES ('Valencia','España'), ('París','Francia'), ('Toulouse','Francia'),('Venecia','Italia')
/*Crea una foreign key en la tabla "Usuarios" que se relacione con la columna "id" de la tabla "Ciudades".*/
ALTER TABLE usuarios
 ADD COLUMN ciudad_id INT,
 ADD CONSTRAINT fk_ciudad FOREIGN KEY(ciudad_id) REFERENCES ciudades(id)
/*Realiza una consulta que muestre los nombres de los usuarios junto con el nombre de su ciudad y país (utiliza un LEFT JOIN).*/
SELECT u.nombre AS nombre_usuario, c.nombre AS nombre_ciudad, c.pais AS pais
FROM usuarios u
LEFT JOIN ciudades c
ON u.ciudad_id = c.id
/*Realiza una consulta que muestre solo los usuarios que tienen una ciudad asociada (utiliza un INNER JOIN).*/
UPDATE usuarios
SET ciudad_id= 2 /*para luego poder comprobar que se ha unido bien*/
SELECT u.nombre AS nombre_usuario, c.nombre AS nombre_ciudad, c.pais AS pais
FROM usuarios u
INNER JOIN ciudades c ON u.ciudad_id = c.id