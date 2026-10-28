# ÁRBOL BINARIO: Nodos, recorrido preorden, conteo y altura

# Cada nodo guarda su valor y referencias a sus dos posibles hijos
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None   # hijo izquierdo (vacío al inicio)
        self.derecha = None     # hijo derecho (vacío al inicio)


# Creamos los nodos que luego conectaremos para formar el árbol
n1 = Nodo(1)
n2 = Nodo(2)
n3 = Nodo(3)
n4 = Nodo(4)
n5 = Nodo(5)
n6 = Nodo(6)
n7 = Nodo(7)
n8 = Nodo(8)
n9 = Nodo(9)
n10 = Nodo(10)

# Enlazamos los nodos indicando hijo izquierdo y derecho
n1.izquierda = n2
n1.derecha = n3

n2.izquierda = n4
n2.derecha = n5

n5.izquierda = n8

n3.izquierda = n6
n3.derecha = n7

n7.izquierda = n9
# Este enlace reemplaza al anterior: n7 queda apuntando a n10 (n9 se pierde)
n7.izquierda = n10

# La raíz es el nodo desde donde empiezan los recorridos
raiz = n1


def recorrer_preorden(nodo):
    """Preorden: Raíz -> Izquierda -> Derecha."""
    # Caso base: rama vacía, no hay nada que visitar
    if nodo is None:
        return
    # 1) Visitamos el nodo actual (se agrega espacio para separar los números)
    print(nodo.valor, end=" ")
    # 2) Recorremos el subárbol izquierdo
    recorrer_preorden(nodo.izquierda)
    # 3) Recorremos el subárbol derecho
    recorrer_preorden(nodo.derecha)


def contar_nodos(nodo):
    """Cuenta todos los nodos del árbol de forma recursiva."""
    # Una rama vacía aporta 0 nodos
    if nodo is None:
        return 0
    # 1 (el nodo actual) + nodos de la izquierda + nodos de la derecha
    return 1 + contar_nodos(nodo.izquierda) + contar_nodos(nodo.derecha)


def altura(nodo):
    """Calcula la altura: cantidad de niveles de la rama más larga."""
    # Una rama vacía tiene altura 0
    if nodo is None:
        return 0
    altura_izq = altura(nodo.izquierda)
    altura_der = altura(nodo.derecha)
    # Sumamos el nodo actual a la rama más alta
    return 1 + max(altura_izq, altura_der)


# Mostramos resultados
print("Información del Árbol")

print("\nRecorrido del Árbol:")
recorrer_preorden(raiz)
print()

print("\nCantidad total de nodos:", contar_nodos(raiz))
print("Altura del Árbol:", altura(raiz))
