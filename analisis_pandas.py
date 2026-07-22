import pandas as pd

# 1. Creamos un diccionario con información de productos
datos_ventas = {
    "Producto": ["Aire Acondicionado Split", "Heladera Inverter", "Cocina Volcán", "Microondas 20L"],
    "Categoria": ["Climatización", "Refrigeración", "Cocción", "Electro Pequeño"],
    "Precio_Lista": [850000, 1200000, 450000, 180000],
    "Stock": [15, 8, 20, 35],
    "Ventas_Mes": [12, 5, 14, 28]
}

# 2. Convertimos ese diccionario en un "DataFrame" (la tabla mágica de Pandas)
df = pd.DataFrame(datos_ventas)

# 3. Mostramos la tabla completa
print("--- TABLA COMPLETA DE INVENTARIO ---")
print(df)
print("\n" + "="*50 + "\n")

# 4. Agregamos una columna calculada de ingresos totales
df["Total_Recaudado"] = df["Precio_Lista"] * df["Ventas_Mes"]

print("--- TABLA CON RECAUDACIÓN TOTAL ---")
print(df[["Producto", "Ventas_Mes", "Total_Recaudado"]])
print("\n" + "="*50 + "\n")

# 5. Filtrar productos con stock crítico (menos de 10 unidades)
stock_critico = df[df["Stock"] < 10]
print("--- ALERTA: STOCK CRÍTICO (MENOS DE 10) ---")
print(stock_critico[["Producto", "Stock"]])

# 6. Métricas Rápidas (Agregaciones)
total_recaudado_local = df["Total_Recaudado"].sum()
producto_mas_vendido = df.loc[df["Ventas_Mes"].idxmax(), "Producto"]
promedio_ventas = df["Ventas_Mes"].mean()

print("--- RESUMEN EJECUTIVO DE VENTAS ---")
print(f"💰 Recaudación Total del Mes: ${total_recaudado_local:,.2f}")
print(f"🏆 Producto estrella (más vendido): {producto_mas_vendido}")
print(f"📊 Promedio de ventas por producto: {promedio_ventas:.1f} unidades")

# 7. Exportar los resultados a un archivo CSV
df.to_csv("reporte_ventas_mes.csv", index=False)
print("\n✅ Reporte exportado con éxito a 'reporte_ventas_mes.csv'")