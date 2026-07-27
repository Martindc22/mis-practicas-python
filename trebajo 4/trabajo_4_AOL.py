import pandas as df

df = df.read_csv("ventas_semanales.csv")

df["Ganancia"] = df["Precio_Venta"] * df["Cantidad"]
df["Costo_total"] = df["Costo_Unitario"] * df["Cantidad"]
df["Ganancia"] = df["Ganancia"] - df["Costo_total"]     

Alerta = df[(df["Cantidad"] < 15) & (df["Categoria"] == "Tecnologia")]
                             
                      
print("Productos con stock disponible (menos de 15 unidades en la categoría Tecnología):")
print(Alerta)

top_categoria = df.groupby("Categoria")["Ganancia"] .sum() .reset_index() .sort_values(by = "Ganancia", ascending=False) .head(2)


print("\n top 2 categorias con mayor ganancias: $")
print(top_categoria)

Alerta.to_csv("alerta_stock_tegnologia.csv", index=False)
print("\n📦 Archivo 'alerta_stock_tegnologia.csv' generado listo para trabajar.")



