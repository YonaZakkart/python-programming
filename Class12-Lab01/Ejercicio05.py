# Ejercicio 5: Registro de estudiante universitario
nombre_estudiante = "Robert Sanchez"# str
edad_estudiante = 22            # int
promedio_estudiante = 9.2         # float
es_becado = True               # bool

print("Ficha del Estudiante")
print(f"Nombre: {nombre_estudiante}")
print(f"Edad: {edad_estudiante} anios")
print(f"Promedio actual: {promedio_estudiante}")
print(f"Posee Beca?: {es_becado}")

# Calculo: Cuanto le falta para la nota máxima (10.0)
puntos_faltantes = 10.0 - promedio_estudiante
print(f"\nCalculo: A {nombre_estudiante} le faltan {puntos_faltantes:.1f} puntos llegar al 10")