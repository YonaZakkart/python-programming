print("SIMULADOR DE CONDUCCIÓN")
velocidad = int(input("Ingrese la velocidad inicial de su auto (en km/h): "))
print("Controles: 'a' (Acelerar), 'f' (Frenar), 's' (Soltar pedal), 'q' (Salir)")

while True:
    accion = input("\nAcción (a/f/s/q): ").strip().lower()
    estado = ""

    if accion == "q":
        print("Apagando motor. Simulación terminada.")
        break
    elif accion == "a":
        velocidad += 10
        estado = "Acelerando"
    elif accion == "f":
        velocidad -= 20
        estado = "Frenando"
    elif accion == "s":
        velocidad -= 2
        estado = "En marcha"
    else:
        print("Comando inválido. Intente de nuevo.")
        continue

    # Validar los límites de velocidad (0 a 180)
    if velocidad > 180:
        velocidad = 180
        estado += " (¡LÍMITE ALCANZADO!)"
    elif velocidad <= 0:
        velocidad = 0
        estado = "Detenido por completo"

    print(f"--> Tablero | Velocidad: {velocidad} km/h | Estado: {estado}")
