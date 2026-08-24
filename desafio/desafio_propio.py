import pandas as pd 
import sqlite3


datos = {
    "productos" : ["remera", "pantalon", "campera", "zapatillas", "gorra"],
    "categorias" : ["ropa", "ropa", "ropa", "calzado", "accesorio"],
    "precios" : [1500, 2500, 5000, 8000, 700],
    "stock" : [10, None, 5, 2, 15],
}

df = pd.DataFrame(datos)
df["stock"] = df["stock"].fillna(0)

conexion = sqlite3.connect(":memory:")

df.to_sql("tienda", conexion, index=False)

query = """
    SELECT productos, precios, stock 
    FROM tienda 
    WHERE categorias = 'ropa' AND stock > 0
    ORDER BY precios DESC
"""
resultado = pd.read_sql_query(query, conexion)


print("\n---PRODUCTOS DE ROPA DISPONIBLES---")


print(resultado)
