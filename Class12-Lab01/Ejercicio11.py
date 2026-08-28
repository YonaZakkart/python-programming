# Ejercicio 11: CRUD en una lista
modulos = ["Autenticación", "Usuarios", "Productos", "Reportes", "Notificaciones"]

print(f"a) Lista inicial: {modulos}")

modulos.append("Pagos")
print(f"b) Agregando 'Pagos': {modulos}")

modulos.insert(2, "Dashboard")
print(f"c) Insertando 'Dashboard' en pos 2: {modulos}")

# En la lista actual "Productos" está en el índice 3
indice_productos = modulos.index("Productos")
modulos[indice_productos] = "Inventario"
print(f"d) Cambiando Productos por Inventario: {modulos}")

modulos.remove("Notificaciones")
print(f"e) Eliminando Notificaciones: {modulos}")

print(f"f) Total de módulos en el sistema: {len(modulos)}")
print(f"g) Lista final de módulos: {modulos}")
