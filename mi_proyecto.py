vendedor = "martin"
cantidad = 5
precio = 600000
total_ventas = cantidad * precio
if cantidad > 10:
    comision = total_ventas * 0.15
else:
    comision =total_ventas * 0.05
print(f"La comision que te corresponde a {vendedor} es de {comision} ") 
