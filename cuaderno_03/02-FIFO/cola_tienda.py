# COLA (FIFO): Operaciones básicas en la Tienda de Don Juancito

# Cola vacía: la tienda recién está abriendo
colaTienda = []

# ENQUEUE: agregar clientes al final de la cola
colaTienda.append('Cliente 1: Yona')
colaTienda.append('Cliente 2: Carlos')
colaTienda.append('Cliente 3: Robert')

print("Clientes de la Tienda Rosita:", colaTienda)

# PEEK / FRONT: ver el primero de la cola SIN eliminarlo
print("Primer cliente en la cola (Peek):", colaTienda[0])

# SIZE: cantidad de elementos en la cola
print("Cantidad de clientes en la cola (Size):", len(colaTienda))

# DEQUEUE: atender (eliminar) al primer cliente -> pop(0)
print("Cliente atendido (DEQUEUE):", colaTienda.pop(0))

# Mostramos quiénes siguen esperando
print("Clientes que siguen en la cola:", colaTienda)

# REAR: ver quién está al final de la cola sin eliminarlo
print("Último cliente en la cola (Rear):", colaTienda[-1])

# Atendemos a los clientes que quedan (siempre el primero de la cola)
print("Cliente atendido (DEQUEUE):", colaTienda.pop(0))
print("Cliente atendido (DEQUEUE):", colaTienda.pop(0))

# IS EMPTY: comprobamos si todavía hay clientes
if not colaTienda:
    print("La cola está vacía (Is Empty): True")
else:
    print("La cola está vacía (Is Empty): False")
