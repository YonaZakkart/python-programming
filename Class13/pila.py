pila = []

pila.append("Iniciar sesion") # append() para agregar elemento

pila.append("Consultar el perfil")
pila.append("Ver amigos en comun")
pila.append("ola k ase? :v")

# Desapilar un elemento
accion = pila.pop()
print("\nAccion retirada: ", accion)

print("\nPenultima accion retirada: ", pila)