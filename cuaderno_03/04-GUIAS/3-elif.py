# elif evalúa otra condición cuando la anterior no se cumplió

nota = 4

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Aprobado")
elif nota >= 5 and nota <= 6:   # nota entre 5 y 6
    print("Repo")
else:
    print("Reprobado")
