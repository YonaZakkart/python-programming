# pila = []

def push(pila, elemento):  # Creando funcion llamada push
    pila.append(elemento)


def pop(pila): #creamos pop prara retirar elementos
    return pila.pop()

#Creamos una pila vacia
pila = []
push(pila,"A")
push(pila,"B")
push(pila,"C")

print("Elemenatos de la pila: ", pila)

elemento = pop(pila)
print("Elemenatos de la pila: ", pila)
