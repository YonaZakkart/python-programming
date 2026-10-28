# PILA (LIFO): Creación básica con append()
# Creamos una pila vacía
pila = []

# Apilamos tres elementos: A, B, C (C queda en el tope)
pila.append("A")
pila.append("B")
pila.append("C")

# Seguimos apilando: ahora el tope es "D"
pila.append("E")
pila.append("D")

# Mostramos el contenido completo de la pila
print(pila)
