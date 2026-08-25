# Supongamos que estamos desarrollando un sistema para una empresa
# Tenemos un producto:
producto = {
    "codigo": "P001",
    "nombre": "Teclado inalambrico",
    "precio": 49.99,
    "stock": 20,
    "disponible": True
}

# Podemos consultar el nombre del produto
print("\nNombre :", producto["nombre"])

# Cambiar la disponibilidad y el stock a 0
producto["stock"] = 0
producto["disponible"] = None
# Imprimir
print("\nNombre :", producto["nombre"],
      "\nPrecio :", producto["precio"],
      "\nStock :", producto["stock"],
      "\nDisponibilidad: ", producto["disponible"])
