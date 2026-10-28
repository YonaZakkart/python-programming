# ÁRBOL BINARIO: Aplicación - categorías de productos de una tienda
class Nodo:
    def __init__(self, valor):
        # Dato que representa este nodo
        self.valor = valor
        # Al inicio el nodo no tiene hijos
        self.izquierdo = None
        self.derecho = None


# PRODUCTOS es la raíz del árbol
raiz = Nodo("PRODUCTOS")

# Categorías principales (hijos de la raíz)
raiz.izquierdo = Nodo("TECNOLOGÍA")
raiz.derecho = Nodo("HOGAR")

# Subcategorías de TECNOLOGÍA
raiz.izquierdo.izquierdo = Nodo("LAPTOPS")
raiz.izquierdo.derecho = Nodo("CELULARES")

# Subcategorías de HOGAR
raiz.derecho.izquierdo = Nodo("COCINA")
raiz.derecho.derecho = Nodo("MUEBLES")

# Mostramos la raíz
print("--- MOSTRAR RAÍZ ---")
print("Raíz del árbol:", raiz.valor)

# Mostramos las categorías conectadas a la raíz
print("\n--- MOSTRAR HIJOS (CATEGORÍAS) ---")
print("Izquierdo:", raiz.izquierdo.valor)
print("Derecho:", raiz.derecho.valor)


def es_hoja(nodo):
    """Un nodo es hoja si no tiene hijo izquierdo ni derecho."""
    return nodo.izquierdo is None and nodo.derecho is None


# Probamos con una hoja LAPTOPS y con un nodo que sí tiene hijos
print("\n--- EVALUACIÓN DE HOJAS ---")
print("¿LAPTOPS es hoja?:", es_hoja(raiz.izquierdo.izquierdo))   # True
print("¿TECNOLOGÍA es hoja?:", es_hoja(raiz.izquierdo))          # False
