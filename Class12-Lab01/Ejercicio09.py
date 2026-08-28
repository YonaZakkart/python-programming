# Ejercicio 9: Lista de tuplas y calculo
puntos = [(1, 2), (4, 5), (0, 3), (-2, -1), (6, 0)]

distancias = []
print("Distancias al origen (0,0)")

# Calculamos la distancia de cada tupla usando el Teorema de pitagoras
for punto in puntos:
    x, y = punto
    distancia = (x**2 + y**2)**0.5
    distancias.append(distancia)
    print(f"Punto {punto}: {distancia:.2f}")

# Encontrar el índice de la distancia mínima para saber cuál punto es
indice_mas_cercano = distancias.index(min(distancias))
punto_mas_cercano = puntos[indice_mas_cercano]

print(f"\nEl punto mas cerca del origen es: {punto_mas_cercano} con una distancia de {min(distancias):.2f}")
