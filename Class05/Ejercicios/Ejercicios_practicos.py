
# Ejercicio 1: Impresion de un texto
# En una cadena multilinea utilizando comillas triples (""")
# para conservar la estructura del texto de forma ordenada.
text = """If we could see tomorrow, what are your plans?
No one can live in sorrow, ask all your friends
Times that you took in stride they're back in demand
I was the one who's washing blood off your hands"""
print(text)


# Ejercicio 2: Creación de una matriz 3x3 de ceros
# Usando listas anidadas (3 filas x 3 columnas).
# Cada sublista interna representa una fila con tres ceros.
matriz_ceros = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
# Imprimimos la matriz de forma estructurada mediante un bucle for
print("\nMatriz 3x3 de ceros:")
for fila in matriz_ceros:
    print(fila)



# Ejercicio 3: Impresión de símbolos (\ y /)
# La barra invertida (\) en pyhon es un carácter de escape.
# Para imprimirla usamos una doble barra invertida (\\).
barra_invertida = "\\"
barra_normal = "/"

print("\nSimbolos impresos:")
print(f"Barra invertida: {barra_invertida}")
print(f"Barra normal: {barra_normal}")
print(f"Ambos juntos: {barra_invertida} {barra_normal}")