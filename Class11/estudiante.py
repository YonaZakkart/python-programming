# Crear un nuevo diccionario

estudiante = {
    "nombre": "Robert",
    "edad": 21,
    "cursos": ["Python", "Estructura de Datos"]
}
# Acceder a elementos
print("\nNombre :", estudiante["nombre"],
      "\nEdad :", estudiante["edad"],
      "\nMaterias :", estudiante["cursos"])

# Modificar edad
estudiante["edad"] = 22
# Ver cambios al imprimir
print("\nNombre :", estudiante["nombre"],
      "\nEdad :", estudiante["edad"],
      "\nMaterias :", estudiante["cursos"])

# Agregar nueva carrera
estudiante["carrera"] = "Ing. Software"
# Ver cambios al imprimir
print("\nNombres :", estudiante["nombre"],
      "\nEdad :", estudiante["edad"],
      "\nCarrera :", estudiante["carrera"],
      "\nMaterias :", estudiante["cursos"])

# Eliminar la edad, con metodo del
del estudiante["edad"]
# Ver cambios al imprimir
print("\nNombres :", estudiante["nombre"],
      "\nEdad :", estudiante["edad"],
      "\nCarrera :", estudiante["carrera"],
      "\nMaterias :", estudiante["cursos"])

# Eliminar la edad, con metodo pop
estudiante.pop("ciudad")  # si no se especifica, elimina el ultimo
# Ver cambios al imprimir
print("\nNombres :", estudiante["nombre"],
      "\nEdad :", estudiante["edad"],
      "\nCarrera :", estudiante["carrera"],
      "\nMaterias :", estudiante["cursos"])
