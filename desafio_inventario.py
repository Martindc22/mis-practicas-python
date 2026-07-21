# Un diccionario con el producto y su stock actual
inventario = {
    "Heladera Inelro MT17": 3,
    "Aire BGH Inverter 3000": 15,
    "Smart TV Motorola 50": 45,
    "Cava de Vinos": 1
}

for producto, cantidad in inventario.items():
    # aca adentro metes tu misma logica del if/elif/else
    if cantidad < 5:
        print(f"{producto} stock creitico (quedan {cantidad})")
    elif cantidad <= 20:
        print(f"{producto} stock aceptable (quedan {cantidad})")  
    else:
        print(f"{producto} stock excelente (quedan {cantidad})")      

