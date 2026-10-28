# GUÍA : Funciones en Python

# Ejercicio 1: función sin parámetros
# def saludar():
#     print("¡Hola! Estudiantes")
# saludar()


# Ejercicio 2: función con parámetros que retorna un valor
def suma(a, b):
    return a + b


resultado = suma(5, 3)
print(resultado)  # 8

# Ejercicio 3: función con un parámetro
# Nota: redefine la función saludar() de arriba, ahora recibe un nombre


def saludar(nombre):
    print("Hola", nombre)


# Solicitamos los nombres al usuario
nombre1 = input("Ingrese su primer nombre: ")
nombre2 = input("Ingrese suu segundo nombre: ")

# Enviamos esos datos a la función
saludar(nombre1)
saludar(nombre2)
