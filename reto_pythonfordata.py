#EJERCICIO 1 - FAMILIARIZARSE CON LA BBDD
#Descripción del ejercicio: El primer paso como analista de datos es conocer la estructura y la información
#básica de nuestra BBDD, Crea el esquema de northwind y observa con atención $%las tablas que tiene y cómo están relacionadas entre sí.
import sqlite3
import re
import pandas as pd

# Cargar el archivo SQL
sql_file = "northwind.sql"
with open(sql_file, "r", encoding="utf-8", errors="ignore") as f:
    sql_script = f.read()

#Crear una base de datos en memoria
con = sqlite3.connect(":memory:")  # usa "northwind.db" si quieres guardarla
cur = con.cursor()

# Limpiar comandos no compatibles con SQLite
clean_sql = "\n".join(
    line for line in sql_script.splitlines()
    if not line.strip().upper().startswith(("SET", "SELECT pg_catalog", "COMMENT", "ALTER"))
)

#Ejecutar el script para crear las tablas y cargar los datos
try:
    cur.executescript(clean_sql)
    print("Base de datos Northwind creada correctamente.")
except Exception as e:
    print("Error al crear la base de datos:", e)

#Ver qué tablas existen
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", con)
print("Tablas en la base de datos:")
print(tables)

#Ver las columnas de cada tabla
for table in tables["name"]:
    info = pd.read_sql_query(f"PRAGMA table_info({table});", con)
    print(f"Estructura de la tabla '{table}':")
    print(info)

#Ver relaciones aproximadas mediante claves foráneas
for table in tables["name"]:
    fks = pd.read_sql_query(f"PRAGMA foreign_key_list({table});", con)
    if len(fks) > 0:
        print(f"Relaciones en la tabla '{table}':")
        print(fks)
        
 # EJERCICIO 2 – PRIMERAS CONSULTAS

# 1. Empleados (id, nombre, apellido, ciudad, país)
empleados_df = pd.read_sql_query("""
SELECT employee_id AS id,
       first_name AS nombre,
       last_name AS apellido,
       city AS ciudad,
       country AS pais
FROM employees
ORDER BY employee_id;
""", con)
display(empleados_df)

# 2. Productos (id, proveedor, nombre, precio, stock, pedidas, descontinuado)
productos_df = pd.read_sql_query("""
SELECT product_id AS id_producto,
       supplier_id AS id_proveedor,
       product_name AS nombre_producto,
       unit_price AS precio_por_unidad,
       units_in_stock AS unidades_en_stock,
       units_on_order AS unidades_pedidas,
       discontinued AS descontinuado
FROM products
ORDER BY product_id;
""", con)
display(productos_df)

# 3. Productos descontinuados (nombre, stock restante)
prod_desc_df = pd.read_sql_query("""
SELECT product_name AS nombre_producto,
       units_in_stock AS stock_restante
FROM products
WHERE discontinued = 1
ORDER BY product_name;
""", con)
display(prod_desc_df)

# 4. Proveedores (id compañía, nombre, ciudad, país)
proveedores_df = pd.read_sql_query("""
SELECT supplier_id AS id_compania,
       company_name AS nombre_compania,
       city AS ciudad,
       country AS pais
FROM suppliers
ORDER BY supplier_id;
""", con)
display(proveedores_df)

# 5. Pedidos (número, id cliente, id transportista, fecha pedido, requerida, llegada)
pedidos_df = pd.read_sql_query("""
SELECT order_id AS num_pedido,
       customer_id AS id_cliente,
       ship_via AS id_transportista,
       order_date AS dia_pedido,
       required_date AS dia_requerido,
       shipped_date AS dia_llegada
FROM orders
ORDER BY order_id;
""", con)
display(pedidos_df)

# 6. Número total de pedidos
num_pedidos = pd.read_sql_query("SELECT COUNT(*) AS total_pedidos FROM orders;", con)
print("Número total de pedidos:", num_pedidos["total_pedidos"][0])

# 7. Clientes (id, nombre compañía, ciudad, país)
clientes_df = pd.read_sql_query("""
SELECT customer_id AS id_cliente,
       company_name AS nombre_compania,
       city AS ciudad,
       country AS pais
FROM customers
ORDER BY customer_id;
""", con)
print("Número total de clientes:", len(clientes_df))
display(clientes_df)

# 8. Empresas de transporte (id, nombre)
transportistas_df = pd.read_sql_query("""
SELECT shipper_id AS id_transportista,
       company_name AS nombre_compania
FROM shippers
ORDER BY shipper_id;
""", con)
display(transportistas_df)

# 9. Relaciones de reporte entre empleados (empleado -> manager)
reportes_df = pd.read_sql_query("""
SELECT e.employee_id AS empleado_id,
       e.first_name || ' ' || e.last_name AS empleado,
       e.reports_to AS reporta_a_id,
       m.first_name || ' ' || m.last_name AS manager
FROM employees e
LEFT JOIN employees m ON e.reports_to = m.employee_id
ORDER BY e.employee_id;
""", con)
display(reportes_df)       

# EJERCICIO 3 – ANÁLISIS DE LA EMPRESA

import matplotlib.pyplot as plt
import pandas as pd

# 1. Evolución de pedidos realizados a lo largo del tiempo
evol_pedidos_df = pd.read_sql_query("""
SELECT strftime('%Y', order_date) AS anio,
       strftime('%m', order_date) AS mes,
       COUNT(*) AS pedidos
FROM orders
WHERE order_date IS NOT NULL
GROUP BY anio, mes
ORDER BY anio, mes;
""", con)

evol_pedidos_df["periodo"] = pd.to_datetime(evol_pedidos_df["anio"] + "-" + evol_pedidos_df["mes"] + "-01")
plt.figure(figsize=(8,4))
plt.plot(evol_pedidos_df["periodo"], evol_pedidos_df["pedidos"], marker='o')
plt.title("Evolución mensual de pedidos")
plt.xlabel("Fecha")
plt.ylabel("Número de pedidos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Países con más ventas y distribución por continente
ventas_pais_df = pd.read_sql_query("""
SELECT c.country AS pais_cliente, COUNT(o.order_id) AS num_pedidos
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.country
ORDER BY num_pedidos DESC;
""", con)

continentes = {
    'Europe': ['Austria','Belgium','Denmark','Finland','France','Germany','Ireland','Italy','Norway','Poland','Portugal','Spain','Sweden','Switzerland','UK'],
    'America': ['Argentina','Brazil','Canada','Mexico','USA','Venezuela']
}

def map_continente(pais):
    for cont, lista in continentes.items():
        if pais in lista:
            return cont
    return "Other"

ventas_pais_df["continente"] = ventas_pais_df["pais_cliente"].apply(map_continente)
dist_por_cont_df = ventas_pais_df.groupby("continente", as_index=False)["num_pedidos"].sum()

plt.figure(figsize=(6,4))
plt.bar(dist_por_cont_df["continente"], dist_por_cont_df["num_pedidos"])
plt.title("Distribución de pedidos por continente")
plt.xlabel("Continente")
plt.ylabel("Número de pedidos")
plt.tight_layout()
plt.show()

# 3. Retrasos por compañía de transporte
retrasos_df = pd.read_sql_query("""
SELECT s.company_name AS transportista,
       julianday(o.shipped_date) - julianday(o.required_date) AS retraso_dias
FROM orders o
JOIN shippers s ON o.ship_via = s.shipper_id
WHERE o.shipped_date IS NOT NULL AND o.required_date IS NOT NULL;
""", con)

plt.figure(figsize=(7,4))
retrasos_df.boxplot(column="retraso_dias", by="transportista", showmeans=True)
plt.suptitle("")
plt.title("Retrasos de entrega por transportista (días)")
plt.ylabel("Días de retraso (negativo = adelantado)")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# 4. Distribución media del precio del pedido por país del cliente
precio_pedido_df = pd.read_sql_query("""
SELECT c.country AS pais_cliente,
       o.order_id,
       SUM(od.unit_price * od.quantity * (1 - od.discount)) AS total_pedido
FROM orders o
JOIN order_details od ON o.order_id = od.order_id
JOIN customers c ON c.customer_id = o.customer_id
GROUP BY c.country, o.order_id;
""", con)

precio_medio_pais_df = precio_pedido_df.groupby("pais_cliente", as_index=False)["total_pedido"].mean()
precio_medio_pais_df = precio_medio_pais_df.sort_values("total_pedido", ascending=False)

plt.figure(figsize=(8,4))
plt.bar(precio_medio_pais_df["pais_cliente"], precio_medio_pais_df["total_pedido"])
plt.title("Precio medio del pedido por país del cliente")
plt.xlabel("País")
plt.ylabel("Precio medio (€)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Porcentaje de clientes sin pedidos
clientes_sin_pedido_df = pd.read_sql_query("""
SELECT c.customer_id
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
WHERE o.order_id IS NULL;
""", con)
total_clientes = pd.read_sql_query("SELECT COUNT(*) AS total FROM customers;", con)["total"][0]
porcentaje_sin_pedido = round(len(clientes_sin_pedido_df) / total_clientes * 100, 2)
print("Porcentaje de clientes sin pedidos registrados:", porcentaje_sin_pedido, "%")

# 6. Productos más demandados y necesidad de re-stock
demanda_df = pd.read_sql_query("""
SELECT p.product_name AS producto,
       SUM(od.quantity) AS cantidad_vendida
FROM products p
LEFT JOIN order_details od ON od.product_id = p.product_id
GROUP BY p.product_name
ORDER BY cantidad_vendida DESC;
""", con)

plt.figure(figsize=(8,5))
plt.barh(demanda_df.head(15)["producto"][::-1], demanda_df.head(15)["cantidad_vendida"][::-1])
plt.title("Top 15 productos más demandados")
plt.xlabel("Unidades vendidas")
plt.ylabel("Producto")
plt.tight_layout()
plt.show()

restock_df = pd.read_sql_query("""
SELECT product_id, product_name, units_in_stock, units_on_order
FROM products
WHERE units_in_stock <= 20 AND (units_on_order = 0 OR units_on_order IS NULL)
ORDER BY units_in_stock ASC;
""", con)
display(restock_df)

# EJERCICIO 4 – QUERIES AVANZADAS

# 1. Última vez que se pidió un producto de cada categoría
ult_pedido_categoria_df = pd.read_sql_query("""
SELECT c.category_id,
       c.category_name,
       MAX(o.order_date) AS ultima_vez_pedido
FROM categories c
JOIN products p ON p.category_id = c.category_id
JOIN order_details od ON od.product_id = p.product_id
JOIN orders o ON o.order_id = od.order_id
GROUP BY c.category_id, c.category_name
ORDER BY c.category_id;
""", con)
display(ult_pedido_categoria_df)

# 2. Productos que nunca se hayan vendido por su precio original
productos_no_precio_original_df = pd.read_sql_query("""
SELECT DISTINCT p.product_id,
       p.product_name
FROM products p
JOIN order_details od ON od.product_id = p.product_id
WHERE ROUND(od.unit_price, 2) != ROUND(p.unit_price, 2)
ORDER BY p.product_id;
""", con)
display(productos_no_precio_original_df)

# 3. Productos con categoría "Confections"
confections_df = pd.read_sql_query("""
SELECT p.product_id,
       p.product_name,
       p.category_id
FROM products p
JOIN categories c ON c.category_id = p.category_id
WHERE c.category_name = 'Confections'
ORDER BY p.product_id;
""", con)
display(confections_df)

# 4. Proveedores cuyos productos están todos descontinuados
proveedores_prescindibles_df = pd.read_sql_query("""
WITH prod_status AS (
    SELECT supplier_id,
           SUM(CASE WHEN discontinued = 0 THEN 1 ELSE 0 END) AS productos_activos,
           COUNT(*) AS total_productos
    FROM products
    GROUP BY supplier_id
)
SELECT s.supplier_id,
       s.company_name,
       ps.total_productos,
       ps.productos_activos
FROM suppliers s
JOIN prod_status ps ON ps.supplier_id = s.supplier_id
WHERE ps.productos_activos = 0
ORDER BY s.supplier_id;
""", con)
display(proveedores_prescindibles_df)

# 5. Clientes que compraron más de 30 artículos "Chai" en un único pedido
chai_clientes_df = pd.read_sql_query("""
SELECT o.customer_id,
       c.company_name,
       od.order_id,
       SUM(od.quantity) AS cantidad_chai
FROM order_details od
JOIN products p ON p.product_id = od.product_id
JOIN orders o ON o.order_id = od.order_id
JOIN customers c ON c.customer_id = o.customer_id
WHERE p.product_name = 'Chai'
GROUP BY o.customer_id, c.company_name, od.order_id
HAVING SUM(od.quantity) > 30
ORDER BY cantidad_chai DESC;
""", con)
display(chai_clientes_df)

# 6. Clientes con suma total de carga (freight) > 1000
clientes_flete_gt_1000_df = pd.read_sql_query("""
SELECT c.customer_id,
       c.company_name,
       SUM(o.freight) AS suma_total_flete
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.company_name
HAVING SUM(o.freight) > 1000
ORDER BY suma_total_flete DESC;
""", con)
display(clientes_flete_gt_1000_df)

# 7. Ciudades con 5 o más empleadas
ciudades_5_mas_empleados_df = pd.read_sql_query("""
SELECT city,
       COUNT(*) AS num_empleados
FROM employees
GROUP BY city
HAVING COUNT(*) >= 5
ORDER BY num_empleados DESC, city;
""", con)
display(ciudades_5_mas_empleados_df)

