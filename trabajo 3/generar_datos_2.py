import pandas as pd

datos_semana = {
    "ID": [201, 202, 203, 204, 205, 206, 207, 208],
    "Fecha": ["2026-07-18", "2026-07-19", "2026-07-20", "2026-07-21", "2026-07-21", "2026-07-22", "2026-07-23", "2026-07-24"],
    "Producto": ["Aire Split Inverter", "Heladera MT17", "Smart TV 50", "Aire Split Inverter", "Celular Galaxy", "Heladera MT17", "Smart TV 50", "Celular Galaxy"],
    "Categoria": ["Climatizacion", "Electro", "Tecnologia", "Climatizacion", "Tecnologia", "Electro", "Tecnologia", "Tecnologia"],
    "Precio_Venta": [650000, 890000, 480000, 650000, 320000, 890000, 480000, 320000],
    "Costo_Unitario": [420000, 610000, 310000, 420000, 200000, 610000, 310000, 200000],
    "Cantidad": [2, 1, 3, 1, 4, 2, 2, 5]
}

df_semana = pd.DataFrame(datos_semana)
df_semana.to_csv("ventas_semanales.csv", index=False)
print("📦 Archivo 'ventas_semanales.csv' generado listo para trabajar.")
