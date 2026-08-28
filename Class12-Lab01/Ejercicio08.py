# Ejercicio 8: Slicing en strings
frase = "Universidad de Oriente - El Salvador"

# 'Universidad' (0 a 11), 'El Salvador' (-11 hasta el final)
print(f"Extraer solo 'Universidad': {frase[:11]}")
print(f"Extraer solo 'El Salvador': {frase[-11:]}")
print(f"Frase completa al reves: {frase[::-1]}")
print(f"Cada tercera letra: {frase[::3]}")
