# Ejercicio 3: Impresión de símbolos especiales (\ y /)

# La barra invertida \ es un caracter de escape, por e so se duplica '\\'
barra_invertida = "\\"
barra_normal = "/"

print("Símbolos de barras:")
# f-strings para insertar variables dentro de la cadena
print(f"Barra invertida: {barra_invertida}")
print(f"Barra normal: {barra_normal}")
print(f"Ambos símbolos juntos: {barra_invertida} {barra_normal}")