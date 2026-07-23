import pandas as pd 
import matplotlib.pyplot as plt

# Dataset Base de Electrodomesticos
datos = {
"ID": [1, 2, 3, 4, 5, 6, 7],
    "Producto": ["Aire Split 3000FC", "Heladera No Frost 400L", "Cocina de Pie 4H", 
                 "Microondas 25L Digital", "Smart TV 55 4K UHD", "Lavarropas Inverter 8kg", "Aire Split 5000FC"],
    "Categoria": ["Climatización", "Refrigeración", "Cocción", "Electro Pequeño", "Electrónica", "Lavado", "Climatización"],
    "Precio": [850000, 1350000, 420000, 210000, 680000, 920000, 1150000],
    "Stock": [12, 5, 25, 30, 7, 4, 8],
    "Ventas_Mes": [15, 8, 18, 40, 12, 9, 10],
    "Sucursal": ["Tucumán", "Córdoba", "Tucumán", "Salta", "Córdoba", "Tucumán", "Salta"]
}

df = pd.DataFrame(datos)
print("--- TABLA ORIGINAL ---")
print(df)

df["Facturacion"] = df["Precio"] * df["Ventas_Mes"]
print(df[["Precio", "Ventas_Mes", "Facturacion"]])

stock_critico = df[df["Stock"] <10]
print("--- Alerta: de Stock critico (Stock menos 10)---")
print(stock_critico[["Producto", "Stock"]])

total_facturado_global = df["Facturacion"].sum()
print(f"total globla del mes ${total_facturado_global}")
# Agrupar por sucursal y sumar la facturacion 
facturacion_sucursal = df.groupby("Sucursal")["Facturacion"].sum().reset_index()
print("\n--- 1. FACTURACION TOTAL POR SUCURSAL ---")
print(facturacion_sucursal)
# 2 Agrupar por categoria y sacar el Promedio de Ventsas_mes
promedio_ventas_categoria = df.groupby("Categoria")["Ventas_Mes"].mean().reset_index()
print("\n--- 2. PROMEDIO DE UNIDADES VENDIDAS POR CATEGORÍA ---")
print(promedio_ventas_categoria)
# 3 Exportar el resumen de sucursales a un csv
facturacion_sucursal.to_csv("facturacion_sucursales.csv", index=False)
print("\n✅ Archivo 'facturacion_sucursales.csv' generado con éxito.")

# ---ejercicio 3: visualizacion ---
# 1. Agrupamos la suma total de unidades vendidas por categoria 
unidades_categoria = df.groupby("Categoria")["Ventas_Mes"].sum().reset_index()

# 2. configurar y armar el grafico 
plt.figure(figsize=(9, 5))
plt.bar(unidades_categoria["Categoria"], unidades_categoria["Ventas_Mes"], color='#10b981'  )

# titulos y estilos 
plt.title("Total de Unidades Vendidas por Categoría", fontsize=13, fontweight='bold')
plt.xlabel("Categoría de Producto", fontsize=10)
plt.ylabel("Unidades Vendidas", fontsize=10)
plt.tight_layout()  # Ajusta espacios para que no se corten los textos

# 3. Guardar la imagen
plt.savefig("ventas_categoria.png")
print("\n📊 ¡Gráfico 'ventas_categoria.png' generado y guardado con éxito!")