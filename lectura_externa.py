import sys
import subprocess

# Intentamos importar matplotlib, y si falla, la instalamos automáticamente
try:
    import matplotlib.pyplot as plt
    print("✅ Matplotlib ya está listo para usarse.")
except ImportError:
    print("⚙️ Instalando matplotlib directamente en el Python activo...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
    import matplotlib.pyplot as plt
    print("✅ Matplotlib se instaló y cargó correctamente.")

import pandas as pd

# 1. Cargar datos
df = pd.read_csv("ventas_sucursal.csv")
df["Total_Venta"] = df["Precio_Unitario"] * df["Cantidad"]
ventas_por_sucursal = df.groupby("Sucursal")["Total_Venta"].sum().reset_index()

# 2. Armar el gráfico
plt.figure(figsize=(8, 5))
plt.bar(ventas_por_sucursal["Sucursal"], ventas_por_sucursal["Total_Venta"], color=['#2563eb', '#f97316', '#10b981'])

plt.title("Facturación Total por Sucursal", fontsize=14, fontweight='bold')
plt.xlabel("Sucursal", fontsize=11)
plt.ylabel("Total Facturado ($)", fontsize=11)

plt.savefig("grafico_facturacion.png")
print("📊 ¡GRÁFICO GENERADO! Revisá 'grafico_facturacion.png' en la carpeta.")