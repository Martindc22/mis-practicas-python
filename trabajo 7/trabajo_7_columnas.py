import pandas as pd

# Datos de ventas
datos = {
    "Producto": ["Televisor", "Aire Acondicionado", "Heladera", "Lavarropas"],
    "Precio_Unitario": [350000, 500000, 600000, 280000],
    "Cantidad": [3, 2, 1, 4]
}

df = pd.DataFrame(datos)

# 1. Crear columna de Total Facturado (Precio x Cantidad)
df["Total_Facturado"] = df["Precio_Unitario"] * df["Cantidad"]

# 2. Aplicar un condicional (Categorizar ventas)
# Si vende más de $800.000 es "Venta Alta", sino "Venta Normal"
df[" Categoria_Venta"] = df["Total_Facturado"].apply(lambda x: "Venta Alta" if x >= 800000 else "Venta Normal")

print(df)