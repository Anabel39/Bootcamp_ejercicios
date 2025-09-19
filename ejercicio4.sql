/*EJERCICIO 4*/
/*Crea una tabla llamada "Pedidos" con las columnas: "id" (entero, clave primaria), "id_usuario" (entero, clave foránea de la tabla 
"Usuarios") y "id_producto" (entero, clave foránea de la tabla "Productos").*/
CREATE TABLE IF NOT EXISTS pedidos (
  id SERIAL PRIMARY KEY, 
  id_usuario INT FOREIGN KEY(id_usuario) REFERENCES usuarios(id),
  id_producto INT CONSTRAINT fk_id_producto FOREIGN KEY (id_producto) REFERENCES productos(id),
  )
/*Inserta al menos tres registros en la tabla "Pedidos" que relacionen usuarios con productos.*/
INSERT TO pedidos (id_usuario, id_producto)
VALUES (1,1), (2,2), (3,4)

/*Realiza una consulta que muestre los nombres de los usuarios y los nombres de los productos que han comprado, incluidos aquellos 
que no han realizado ningún pedido (utiliza LEFT JOIN y COALESCE). */
SELECT 
    COALESCE(u.nombre, 'Sin usuario') AS nombre_usuario,
    COALESCE(p.nombre, 'Sin producto') AS nombre_producto
FROM Usuarios u
LEFT JOIN Pedidos pe ON u.id = pe.id_usuario
LEFT JOIN Productos p ON pe.id_producto = p.id; 

/*Realiza una consulta que muestre los nombres de los usuarios que han realizado un pedido, pero también los que no han realizado 
ningún pedido (utiliza LEFT JOIN). */
SELECT 
    u.nombre AS nombre_usuario
FROM Usuarios u
LEFT JOIN Pedidos pe ON u.id = pe.id_usuario;

/*Agrega una nueva columna llamada "cantidad" a la tabla "Pedidos" y actualiza los registros existentes con un valor (utiliza ALTER 
TABLE y UPDATE)*/
ALTER TABLE Pedidos ADD COLUMN cantidad INT;
UPDATE Pedidos SET cantidad = 1;