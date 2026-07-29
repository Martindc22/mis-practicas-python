import pandas as pd

# Tabla 1: Ventas
data_ventas = {
    "ID_Venta": [101, 102, 103, 104],
    "ID_Cliente": [1, 2, 1, 3],
    "Producto": ["Smart TV", "Celular", "Heladera", "Lavarropas"],
    "Monto": [500000, 300000, 700000, 450000]
}
df_ventas = pd.DataFrame(data_ventas)

# Tabla 2: Clientes
data_clientes = {
    "ID_Cliente": [1, 2, 3],
    "Nombre": ["Martín Gómez", "Laura Soria", "Carlos Pérez"],
    "Ciudad": ["Tucumán", "Córdoba", "Buenos Aires"]
}
df_clientes = pd.DataFrame(data_clientes)

df_completo = pd.merge(df_ventas, df_clientes, on="ID_Cliente", how="inner")

print(df_completo)

ventas_tucuman = df_completo[df_completo["Ciudad"] == "Tucumán"]
print("\nVentas realizadas en Tucumán:")
print(ventas_tucuman)

total_facturado_ciudad = df_completo.groupby("Ciudad")["Monto"].sum().reset_index()
print("\nTotal facturado por ciudad:")

print(total_facturado_ciudad)

compra_cliente = df_completo.groupby("Nombre")["Monto"].sum().reset_index()
print("\nTotal facturado por cliente:")
print(compra_cliente)

venta_vip = df_completo[df_completo["Monto"] > 400000]
print("\nVentas VIP (Monto > 400000):") 
print(venta_vip)

venta_vip.to_csv("ventas_vip.csv", index=False )




