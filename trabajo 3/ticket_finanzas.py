import pandas as pd
df = pd.read_csv("ventas_semanales.csv")

df["Facturacion"]= df["Precio_Venta"] * df["Cantidad"]
df["Costo_total"] = df["Costo_Unitario"] * df["Cantidad"]
df["Ganancia"] = df["Facturacion"] - df["Costo_total"]
Fecha_venta20 = df[df["Fecha"] >= "2026-07-20"]

Rentabilidad_categoria = df.groupby("Categoria")["Ganancia"].sum() .reset_index() .sort_values(by="Ganancia", ascending=False)

print("Venta desde el 20 de julio de 2020:")
print(Fecha_venta20[["Fecha", "Producto", "Ganancia"]])

print("\nRentabilidad por categoría:")
print(Rentabilidad_categoria)

