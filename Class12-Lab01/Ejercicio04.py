# Ejercicio 4: Declaracion de tipos de datos
edad = 21            # int
promedio = 8.5       # float
nombre = "Yona"      # str
activo = True        # bool

# type() para mostrar la clase de cada variable
print(f"Variable: edad = {edad}, Tipo: {type(edad)}")
print(f"Variable: promedio = {promedio}, Tipo: {type(promedio)}")
print(f"Variable: nombre = \"{nombre}\", Tipo: {type(nombre)}")
print(f"Variable: activo = {activo}, Tipo: {type(activo)}")

# concatenación y suma matematica
nueva_edad = edad + 1
print(f"\nEl proximo anio, el alumno {nombre} tendra {nueva_edad} anios.")
