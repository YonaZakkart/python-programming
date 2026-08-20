# Ejercicio 2: Ubicación de dispositivos
# Una empresa de tecnología registra la ubicación de sus dispositivos mediante
# coordenadas.
# Cada dispositivo debe almacenar:
# Código del dispositivo
# Nombre
# Ubicación (X, Y)
# Estado
# Crea tres tuplas:
# dispositivo1 = (...)
dispositivo1 = ("PC010", "Servidor", (34, -87), "Activo")
# dispositivo2 = (...)
dispositivo2 = ("PC322", "Almacen", (244, 590), "Activo")
# dispositivo3 = (...)
dispositivo3 = ("PC567", "Gestion", (38, -23), "Inactivo")

# El programa debe mostrar:
# Código: PC001
# Nombre: Servidor principal
# Coordenada X: 150
# Coordenada Y: 300
# Estado: Activo
print(
    "\nCodigo: ", dispositivo1[0],
    "\nNombre: ", dispositivo1[1],
    "\ncoordenada X: ", dispositivo1[2][0],
    "\nCoordenada Y: ", dispositivo1[2][1],
    "\nEstado: ", dispositivo1[3],
)

# Crea una tupla llamada dispositivos que contenga las tres tuplas anteriores:
dispositivos = (dispositivo1, dispositivo2, dispositivo3)
# Luego muestra únicamente la coordenada Y del segundo dispositivo utilizando
# los índices correspondientes
print("Coordenada Y del dispositivo 2: ", dispositivos[1][2][1])


# Adicional, ahora que dispositivos contiene las 3 tuplas se pueden imprimir con un bucle for
# Aunque no lo pidio, pero asi se muestran todos :)
for dispositivo in dispositivos:
    print(
        "\nCodigo: ", dispositivo[0],
        "\nNombre: ", dispositivo[1],
        "\ncoordenada X: ", dispositivo[2][0],
        "\nCoordenada Y: ", dispositivo[2][1],
        "\nEstado: ", dispositivo[3],
    )