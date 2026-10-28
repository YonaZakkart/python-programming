# COLA (FIFO): Sistema de turnos - Banco Los Manguitos-SV

Cola = []          # Cola global donde se guardan los clientes en espera
numero_turno = 1   # Contador global para generar turnos consecutivos


def registrar_cliente(nombre):
    """ENQUEUE: agrega un cliente al final de la cola con su turno."""
    global numero_turno

    # Formato del turno: T + número con mínimo 3 dígitos (ej. T001)
    turno = f"T{numero_turno:03d}"
    cliente = [turno, nombre]   # Cada cliente es una lista [turno, nombre]
    Cola.append(cliente)
    numero_turno += 1           # Preparamos el siguiente turno

    print("\nCliente registrado correctamente.")
    print("Turno asignado:", turno)
    print("Cliente:", nombre)


def ver_siguiente():
    """PEEK: muestra el próximo cliente sin sacarlo de la cola."""
    if Cola:
        siguiente = Cola[0]
        print("\nPróximo cliente:")
        print("Turno del cliente:", siguiente[0])
        print("Cliente siguiente:", siguiente[1])
    else:
        print("No hay clientes en la cola.")


def atender_cliente():
    """DEQUEUE: llama y retira al primer cliente de la cola."""
    if Cola:
        cliente = Cola.pop(0)
        print("--- Llamamos al cliente ---")
        print("Turno:", cliente[0])
        print("Cliente:", cliente[1])
    else:
        print("\nNo hay clientes que atender. =)")


def mostrar_cola():
    """Muestra todos los clientes en espera, el total y el último turno."""
    if not Cola:
        print("No hay clientes esperando.")
        print("\nCantidad de clientes que esperan:", len(Cola))
        return

    for cliente in Cola:
        print(cliente[0], "-", cliente[1])

    # SIZE: cuántos clientes esperan
    print("\nCantidad de clientes que esperan:", len(Cola))

    # REAR: turno del último cliente
    print("Último turno:", Cola[-1][0])


def mostrar_menu():
    print("\n" + "=" * 30)
    print("Banco Los Manguitos")
    print("--- Menú de Turnos ---")
    print("1. Registrar clientes")
    print("2. Ver próximos clientes")
    print("3. Llamar al cliente")
    print("4. Mostrar todos los clientes")
    print("5. Salir")
    print("=" * 30)


# El menú solo se ejecuta si corremos este archivo directamente
if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (número): ")

        if opcion == "1":
            nombre = input("Ingrese su nombre: ")
            registrar_cliente(nombre)
        elif opcion == "2":
            ver_siguiente()
        elif opcion == "3":
            atender_cliente()
        elif opcion == "4":
            mostrar_cola()
        elif opcion == "5":
            print("\nSistema finalizado")
            break
        else:
            print("\nLa opción seleccionada no existe")
