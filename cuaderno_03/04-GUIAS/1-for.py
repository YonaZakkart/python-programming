#Ciclo for
clientes = ['Yona', 'Carlos', 'Robert', 'Jose']

# Recorremos la lista: en cada vuelta "cliente" toma un nombre distinto
# (corregido: antes imprimía el texto "cliente"; ahora imprime la variable)
for cliente in clientes:
    print(cliente)


# for con range(): repite una cantidad determinada de veces
for i in range(5):
    print("Hola")
