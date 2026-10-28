# PILA (LIFO) = Last In, First Out (el último en entrar es el primero en salir)

# Historial de acciones en una red social
# Una lista de Python funciona como pila si solo usamos append() y pop()
pila = []

# PUSH (apilar): append() agrega el elemento al final de la lista (tope de la pila)
pila.append("Iniciar sesión")
pila.append("Consultar el perfil")
pila.append("Ver amigos en común")
pila.append("Hola k ase?")

print("Pila actual:")
print(pila)

# POP (desapilar): pop() retira y devuelve el ÚLTIMO elemento (el tope)
# Esto simula la acción de "deshacer"
accion = pila.pop()

print("\nAcción retirada:")
print(accion)

# Mostramos cómo quedó la pila después de retirar el tope
print("\nPila después de retirar la última acción:")
print(pila)
