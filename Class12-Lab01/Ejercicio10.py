# Ejercicio 10: conjuntos en 
ing_software = {"Programacion", "Redes", "Base de Datos", "Gestion de servidores", "Arquitectura en la nube", "Mecanica"}
ing_sistemas = {"Programación", "Redes", "Base de Datos", "Sistemas Operativos", "Física", "Hardware"}
ing_datos = {"Programación", "Estadística", "Base de Datos", "Machine Learning", "Big Data", "Minería"}

# Materias comunes (Intersección)
comunes = ing_software & ing_sistemas & ing_datos
print(f"Materias comunes entre todas: {comunes}")

# Materias exclusivas de Software (Diferencia)
exclusivas_sw = ing_software - (ing_sistemas | ing_datos)
print(f"Materias exclusivas de Software: {exclusivas_sw}")

# Unión de todas las materias
todas_materias = ing_software | ing_sistemas | ing_datos
print(f"Union de todas las materias: {todas_materias}")

# Mostrar total de materias únicas
print(f"Total de materias unicas: {len(todas_materias)}")
