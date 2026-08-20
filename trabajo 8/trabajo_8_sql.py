import pandas as pd
import sqlite3

# 1. Creamos datos de prueba
datos = {
    "Producto": ["Televisor", "Aire Acondicionado", "Heladera", "Lavarropas"],
    "Categoria": ["Electro", "Climatizacion", "Electro", "Electro"],
    "Precio": [350000, 500000, 600000, 280000]
}

df = pd.DataFrame(datos)

# 2. Nos conectamos a una base de datos en memoria (SQLite)
conexion = sqlite3.connect(":memory:")

# 3. Guardamos el DataFrame como una TABLA en SQL llamada "productos"
df.to_sql("productos", conexion, index=False)

# 4. Hacemos nuestra primera consulta SQL pura
query = """
    SELECT Producto, Precio 
    FROM productos 
    WHERE Categoria = 'Electro' 
    ORDER BY Precio DESC
"""

# 5. Leemos el resultado de SQL directamente a Pandas
resultado = pd.read_sql_query(query, conexion)

print("--- RESULTADO DE LA CONSULTA SQL ---")
print(resultado)