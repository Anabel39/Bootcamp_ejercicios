/* EJERCICIO 1*/
/*Crear una tabla llamada "Clientes" con las columnas: id (entero, clave primaria),
nombre (texto) y email (texto). */
CREATE TABLE IF NOT EXISTS public.clientes (
  id SERIAL PRIMARY KEY,
  name VARCHAR (255),
  email VARCHAR (255) )

 /*Insertar un nuevo cliente en la tabla "Clientes" con id=1, nombre="Juan" y
email="juan@example.com". */
INSERT INTO public.clientes (name, email)
VALUES ('Juan', 'juan@ecample.com')

 /*Actualizar el email del cliente con id=1 a "juan@gmail.com" */
 UPDATE public.clientes
 SET email = 'juan@gmail.com'
 WHERE id = 1;

 /* Eliminar el cliente con id=1 de la tabla "Clientes" */
 DELETE FROM public.clientes
 WHERE id= 1
  
 /* Crear una tabla llamada "Pedidos" con las columnas: id (entero, clave primaria),
cliente_id (entero, clave externa referenciando a la tabla "Clientes"), producto
(texto) y cantidad (entero). */
CREATE TABLE IF NOT EXISTS public.pedidos (
  id SERIAL PRIMARY KEY,
  producto VARCHAR (255),
  cantidad INT,
  client_id SERIAL, 
  CONSTRAINT FK_id_clientes FOREIGN KEY (client_id) REFERENCES public.clientes(id) 

 /* Insertar un nuevo pedido en la tabla "Pedidos" con id=1, cliente_id=1,
producto="Camiseta" y cantidad=2.=> Pongo id 2 ya que al eliminar al primero en ej previo ya no vuelve a usarse ese nº de serial */
INSERT INTO public.pedidos (producto, cantidad, client_id)
VALUES ('camiseta', 2, 2)

 /* Actualizar la cantidad del pedido con id=1 a 3.=> Pongo id 2 ya que al eliminar al primero en ej previo ya no vuelve a usarse ese nº de serial */
 UPDATE public.pedidos
 SET cantidad = 3
 WHERE id= 2
 /* Eliminar el pedido con id=1 de la tabla "Pedidos". => Pongo id 2 ya que al eliminar al primero en ej previo ya no vuelve a usarse ese nº de serial */
 DELETE FROM public.pedidos
 WHERE id= 2 
 
 /*Crear una tabla llamada "Productos" con las columnas: id (entero, clave
primaria), nombre (texto) y precio (decimal).*/
CREATE TABLE IF NOT EXISTS public.productos (
  id SERIAL PRIMARY KEY, 
  nomnbre VARCHAR (255),
  precio DECIMAL
)
/* Insertar varios productos en la tabla "Productos" con diferentes valores */
INSERT INTO public.productos (nombre, precio)
VALUES ('camiseta', 12.50),

/*Consultar todos los clientes de la tabla "Clientes".*/
SELECT* FROM public.clientes

/* Consultar todos los pedidos de la tabla "Pedidos" junto con los nombres de los
clientes correspondientes. */
SELECT * FROM  public.pedidos
LEFT JOIN public.clientes ON public.clientes.id = public.pedidos.client_id;

/*Consultar los productos de la tabla "Productos" cuyo precio sea mayor a $50.*/
SELECT* FROM public.productos
WHERE precio > 50
/*Consultar los pedidos de la tabla "Pedidos" que tengan una cantidad mayor o
igual a 5. */
SELECT* FROM public.pedidos
WHERE cantidad >= 5
/*Consultar los clientes de la tabla "Clientes" cuyo nombre empiece con la letra
"A".*/
SELECT * FROM public.clientes
WHERE name ILIKE 'A%'
 /* Realizar una consulta que muestre el nombre del cliente y el total de pedidos
realizados por cada cliente. */
SELECT public.clientes.name, COUNT(public.pedidos.id) AS total_pedidos
FROM public.clientes
LEFT JOIN public.pedidos ON public.clientes.id = public.pedidos.client_id
GROUP BY public.clientes.name;
 /* Realizar una consulta que muestre el nombre del producto y la cantidad total de
pedidos de ese producto. */
SELECT public.productos.nombre, SUM(public.pedidos.cantidad) AS total_pedidos
FROM public.productos
LEFT JOIN public.pedidos ON public.productos.id = public.pedidos.id
GROUP BY public.productos.nombre;
/* Agregar una columna llamada "fecha" a la tabla "Pedidos" de tipo fecha.*/
ALTER TABLE public.pedidos
ADD COLUMN fecha DATE 
/*Agregar una clave externa a la tabla "Pedidos" que haga referencia a la tabla
"Productos" en la columna "producto".*/
ALTER TABLE public.pedidos
ADD COLUMN producto_id INT,
ADD CONSTRAINT FK_id_productos FOREIGN KEY (producto) REFERENCES public.productos(id)