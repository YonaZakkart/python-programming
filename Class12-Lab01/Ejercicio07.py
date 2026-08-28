# Ejercicio 7: Slicing en listas
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sabado", "Domingo"]

print(f"a) Primeros 3 días: {dias[:3]}")
print(f"b) Ultimos 2 dias: {dias[-2:]}")
print(f"c) Dias laborales: {dias[:5]}")
print(f"d) Fin de semana: {dias[5:]}")
print(f"e) Todos los días en orden inverso: {dias[::-1]}")
print(f"f) Un día sí y otro no: {dias[::2]}")