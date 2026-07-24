import pandas as pd
df = pd.read_csv("ventas_raw.csv")

df["Categoria"] = df["Categoria"].fillna("Sin Categoria")
df["Facturacion_total"] = df["Precio_Unidad"] * df["Cantidad_Vendida"]
top_3 = df.groupby("Producto")["Facturacion_total"].sum().reset_index().sort_values(by="Facturacion_total", ascending=False).head (3)
filtro_tecno = df[(df["Categoria"] == "Tecnología") & (df["Stock_Disponible"] < 15)]

print("📊 Top 3 productos con mayor facturación total:")
print(top_3)

print("\n📦 Productos de la categoría 'Tecnología' con stock disponible menor a 15:")
print(filtro_tecno[["Producto", "Stock_Disponible", "Categoria"]])
df.to_csv("ventas_limpias.csv", index=False)
top_3.to_csv("top_3_productos.csv", index=False)    
print("\n✅ Archivo 'ventas_limpias.csv' generado correctamente con datos limpios.")
print("\n✅ Archivo 'top_3_productos.csv' generado correctamente.")