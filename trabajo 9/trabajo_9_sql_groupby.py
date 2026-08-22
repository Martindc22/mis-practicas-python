import pandas as pd
import sqlite3

# 1. Datos de ventas
datos = {
    "Producto": ["Televisor", "Aire Acondicionado", "Heladera", "Lavarropas", "Microondas"],
    "Categoria": ["Electro", "Climatizacion", "Electro", "Electro", "Electro"],
    "Precio": [350000, 500000, 600000, 280000, 150000]
}

df = pd.DataFrame(datos)

# 2. Conexión a SQLite
conexion = sqlite3.connect(":memory:")
df.to_sql("productos", conexion, index=False)

# 3. Consulta SQL con GROUP BY y SUM
query_agrupada = """
    SELECT 
        Categoria, 
        COUNT(Producto) AS Cantidad_Productos,
        SUM(Precio) AS Total_Facturado
    FROM productos
    GROUP BY Categoria
    ORDER BY Total_Facturado DESC
"""

# 4. Leemos y mostramos el resultado
resultado = pd.read_sql_query(query_agrupada, conexion)
print("--- RESUMEN POR CATEGORIA (SQL) ---")
print(resultado)