/*EJERCICIO 3*/
/*Crea una tabla llamada "Productos" con las columnas: "id" (entero, clave primaria), "nombre" (texto) y "precio" (numérico).*/
 CREATE TABLE IF NOT EXISTS productos (
 id SERIAL PRIMARY KEY,
 nombre VARCHAR (255) NOT NULL,
 precio NUMERIC NOT NULL
 )
 /*Inserta al menos cinco registros en la tabla "Productos".*/
 INSERT INTO productos (nombre,precio)
 VALUES ('acondicionador', 7.50),
        ('cepillo del pelo', 2.75),
		('pintauñas', 2),
		('champú', 5.25),
		('crema de dia', 3.80),
		('esponja', 1),
		('coletero', 3)
 /*Actualiza el precio de un producto en la tabla "Productos".*/
 UPDATE productos
 SET precio = 2.5
 WHERE productos.id = 7
 /*Elimina un producto de la tabla "Productos".*/
 DELETE FROM productos
 WHERE productos.id = 7
 /*Realiza una consulta que muestre los nombres de los usuarios junto con los
nombres de los productos que han comprado (utiliza un INNER JOIN con la tabla "Productos").*/
SELECT clientes.nombre AS nombre, productos.nombre AS nombre_producto
    FROM clientes
    INNER JOIN pedidos ON clientes.id = clientes.id
    INNER JOIN productos ON productos.nombre = pedidos.producto;
   