# Ejercicio 6: Manipulacion de listas
materias = ["Programacion Estructurada", "Estructura de Datos", "Programacion Orientada a Eventos", "Machine Learning", "Configuracion de Redes"]

print(f"a) Lista completa: {materias}")

# b) Agregar 2 materias
materias.append("Sistemas Operativos")
materias.append("Disenio web")
print(f"b) Lista con nuevas materias: {materias}")

# c) Insertar en posición 2
materias.insert(2, "Calculo Diferencial")
print(f"c) Materia insertada en pos 2: {materias}")

# d) Eliminar la ultima materia 
materias.remove(materias[-1])
print(f"d) Lista sin la última materia: {materias}")

# e) Numero total de materias
print(f"e) Numero total de materias: {len(materias)}")