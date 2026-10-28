# PILA (LIFO). Operaciones push() y pop() como funciones
def push(pila, elemento):
    # Apila un elemento: lo agrega al final de la lista
    pila.append(elemento)


def pop(pila):
    # Desapila: retira y devuelve el elemento del tope
    return pila.pop()


# Creamos una pila vacía
pila = []

# Apilamos A, B y C usando nuestra función push
push(pila, "A")
push(pila, "B")
push(pila, "C")

# Mostramos la pila completa
print("Elementos de la pila:", pila)

# Retiramos el tope con pop: debe salir el último que entró
elemento = pop(pila)
print("El último elemento es:", elemento)

# Mostramos cómo quedó la pila
print("Pila final:", pila)
