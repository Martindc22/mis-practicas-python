import pandas as pd
import numpy as np  # Numpy para generar los valores faltantes (np.nan)

datos = {
    "Cliente": ["Martín", "Laura", "Carlos", "Sofia", "Diego"],
    "Edad": [30, np.nan, 25, 40, np.nan],         
    "Monto_Gasto": [500000, 300000, np.nan, 200000, 150000], 
    "Ciudad": ["Tucumán", "Córdoba", "Buenos Aires", None, "Tucumán"] 
}

df = pd.DataFrame(datos)

# 1. Contamos cuántos nulos hay por columna
print("--- CONTEO DE NULOS ---")
print(df.isna().sum())

# 2. Rellenamos la columna 'Ciudad' con "Sin Especificar"
df["Ciudad"] = df["Ciudad"].fillna("Sin Especificar")

# 3. Rellenamos la columna 'Monto_Gasto' con 0
df["Monto_Gasto"] = df["Monto_Gasto"].fillna(0)

print("\n--- DATOS LIMPIOS ---")
print(df)

promedio_edad = df["Edad"].mean()
df["Edad"] = df["Edad"].fillna(promedio_edad)
df["Edad"] = df["Edad"].round(1)  # Redondeamos a un decimal

print("\n--- DATOS FINALES --- (con promedio de edad)")
print(df)