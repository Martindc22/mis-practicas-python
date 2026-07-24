import pandas as pd

# Datos simulados con imperfecciones reales (valores nulos, diferencias de formato)
datos_raw = {
    "ID_Transaccion": [101, 102, 103, 104, 105, 106, 107, 108],
    "Producto": ["Smart TV 50", "Aire Acondicionado", "Heladera MT17", "Silla Gamer", "Teclado Mecanico", "Smart TV 50", "Placa de Video", "Aire Acondicionado"],
    "Categoria": ["Tecnología", "Climatización", "Electro", None, "Tecnología", "Tecnología", None, "Climatización"],
    "Precio_Unidad": [450000, 680000, 890000, 120000, 45000, 450000, 320000, 680000],
    "Cantidad_Vendida": [3, 1, 2, 5, 12, 2, 4, 3],
    "Stock_Disponible": [8, 20, 5, 14, 9, 8, 3, 20]
}

df_raw = pd.DataFrame(datos_raw)
df_raw.to_csv("ventas_raw.csv", index=False)
print("📦 Archivo 'ventas_raw.csv' generado correctamente con datos sucios.")