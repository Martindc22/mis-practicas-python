import pandas as pd
import sqlite3

# 1. Datos iniciales con un precio faltante (None)
datos = {
    "Producto": ["TV 50", "Heladera No Frost", "Lavarropas", "Aire Split", "Cocina"],
    "Categoria": ["Electro", "Electro", "Electro", "Climatizacion", "Electro"],
    "Precio": [450000, 850000, None, 600000, 380000]
}

df = pd.DataFrame(datos)

# 2. Rellenamos el precio faltante con el promedio
promedio_precio = df["Precio"].mean()
df["Precio"] = df["Precio"].fillna(promedio_precio)

# 3. Guardamos la tabla limpia en SQLite
conexion = sqlite3.connect(":memory:")
df.to_sql("inventario", conexion, index=False)

# 4. Consulta SQL: Productos de 'Electro' con Precio > 400.000 ordenados DESC
query = """
    SELECT Producto, Precio 
    FROM inventario 
    WHERE Categoria = 'Electro' AND Precio > 400000
    ORDER BY Precio DESC
"""

resultado = pd.read_sql_query(query, conexion)

print("--- PRODUCTOS SELECCIONADOS (SQL) ---")
print(resultado)