from datetime import datetime

# arbol de destinos
class NodoDestino:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []

def agregar_hijo(padre, hijo):
    padre.hijos.append(hijo)

def mostrar_arbol(nodo, nivel=0):
    print("   " * nivel + "- " + nodo.nombre)
    for hijo in nodo.hijos:
        mostrar_arbol(hijo, nivel + 1)

def buscar_destino(nodo, nombre):
    if nodo.nombre.lower() == nombre.lower():
        return nodo
    for hijo in nodo.hijos:
        encontrado = buscar_destino(hijo, nombre)
        if encontrado:
            return encontrado
    return None

def construir_arbol():
    raiz = NodoDestino("Terminal Central")
    oriental = NodoDestino("Zona Oriental")
    central = NodoDestino("Zona Central")
    occidental = NodoDestino("Zona Occidental")

    agregar_hijo(raiz, oriental)
    agregar_hijo(raiz, central)
    agregar_hijo(raiz, occidental)

    agregar_hijo(oriental, NodoDestino("San Miguel"))
    agregar_hijo(oriental, NodoDestino("La Union"))
    agregar_hijo(oriental, NodoDestino("Usulutan"))

    agregar_hijo(central, NodoDestino("San Salvador"))
    agregar_hijo(central, NodoDestino("La Libertad"))

    agregar_hijo(occidental, NodoDestino("Santa Ana"))
    agregar_hijo(occidental, NodoDestino("Ahuachapan"))

    return raiz

# ESTRUCTURAS
cola_pasajeros = []          # FIFO
pila_salidas = []            # LIFO
contador_pasajero = 1
arbol = construir_arbol()

# OPERACIONES COLA 
def registrar_pasajero():
    global contador_pasajero
    nombre = input("Nombre del pasajero: ").strip()
    if not nombre:
        print("Error: el nombre no puede estar vacío.")
        return
    destino = input("Destino: ").strip()
    if not destino:
        print("Error: el destino no puede estar vacío.")
        return
    if buscar_destino(arbol, destino) is None:
        print("Error: destino inexistente.")
        return

    codigo = f"P{contador_pasajero:03d}"
    pasajero = {"codigo": codigo, "nombre": nombre, "destino": destino}
    cola_pasajeros.append(pasajero)   # se agrega al final
    contador_pasajero += 1
    print(f"Pasajero registrado: {codigo} - {nombre} → {destino}")

def atender_pasajero():
    if not cola_pasajeros:
        print("No hay pasajeros en espera.")
        return
    atendido = cola_pasajeros.pop(0)  # se retira el primero (FIFO)
    print("\nPASAJERO ATENDIDO")
    print(f"Turno: {atendido['codigo']}")
    print(f"Nombre: {atendido['nombre']}")
    print(f"Destino: {atendido['destino']}")
    print(f"Total en espera: {len(cola_pasajeros)}")

def mostrar_cola():
    if not cola_pasajeros:
        print("No hay pasajeros en espera.")
        return
    print("\nPASAJEROS EN ESPERA")
    for p in cola_pasajeros:
        print(f"{p['codigo']} {p['nombre']} {p['destino']}")
    print(f"Total: {len(cola_pasajeros)}")

# ---------- OPERACIONES PILA (LIFO) ----------
def registrar_salida():
    codigo = input("Código del bus: ").strip()
    if not codigo:
        print("Error: el código no puede estar vacío.")
        return
    destino = input("Destino del bus: ").strip()
    if not destino:
        print("Error: el destino no puede estar vacío.")
        return
    if buscar_destino(arbol, destino) is None:
        print("Error: destino inexistente.")
        return

    # Mejora 1: fecha y hora de la salida
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    salida = {
        "codigo": codigo,
        "destino": destino,
        "fecha_hora": fecha_hora
    }
    pila_salidas.append(salida)   # se agrega al final (cima)
    print(f"Salida registrada: {codigo} → {destino} ({fecha_hora})")

def deshacer_salida():
    if not pila_salidas:
        print("No hay salidas registradas para deshacer.")
        return
    retirada = pila_salidas.pop()  # se retira la última (LIFO)
    print(f"Salida deshecha: {retirada['codigo']} → {retirada['destino']} ({retirada['fecha_hora']})")

def mostrar_salidas():
    if not pila_salidas:
        print("No hay salidas registradas.")
        return
    print("\nSALIDAS REGISTRADAS (de más antigua a más reciente):")
    for s in pila_salidas:
        print(f"{s['codigo']} → {s['destino']}  [{s['fecha_hora']}]")
    print(f"Última salida (cima): {pila_salidas[-1]['codigo']}")

# Mejora 2: consultar la cima sin retirar
def consultar_cima():
    if not pila_salidas:
        print("La pila de salidas está vacia")
        return
    cima = pila_salidas[-1]
    print("\nCIMA DE LA PILA:")
    print(f"Codigo: {cima['codigo']}")
    print(f"Destino: {cima['destino']}")
    print(f"Fecha/Hora: {cima['fecha_hora']}")

# menú
def menu():
    while True:
        print("\n~TERMINAL DE BUSES~")
        print("1. Registrar pasajero (cola)")
        print("2. Atender pasajero")
        print("3. Mostrar cola de espera")
        print("4. Registrar salida de bus (pila)")
        print("5. Deshacer última salida")
        print("6. Mostrar salidas registradas")
        print("7. Consultar cima de la pila")
        print("8. Mostrar árbol de destinos")
        print("9. Buscar destino")
        print("0. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            registrar_pasajero()
        elif opcion == "2":
            atender_pasajero()
        elif opcion == "3":
            mostrar_cola()
        elif opcion == "4":
            registrar_salida()
        elif opcion == "5":
            deshacer_salida()
        elif opcion == "6":
            mostrar_salidas()
        elif opcion == "7":
            consultar_cima()
        elif opcion == "8":
            print("\nÁrbol de destinos:")
            mostrar_arbol(arbol)
        elif opcion == "9":
            nombre = input("Destino a buscar: ").strip()
            if not nombre:
                print("Error: el nombre no puede estar vacío")
            else:
                resultado = buscar_destino(arbol, nombre)
                if resultado:
                    print(f"Destino encontrado: {resultado.nombre}")
                else:
                    print("Destino no encontrado")
        elif opcion == "0":
            print("Programa finalizado")
            break
        else:
            print("Opción no valida")

if __name__ == "__main__":
    menu()