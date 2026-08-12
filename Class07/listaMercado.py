# Crear una lista de compras de frutas a comprar en el mercado por unidad.
#Que incluya 2 manzana, banana, uva, manzana

frutas = ["manzana", "manzana", "banana", "uva", "manzana"]
print(frutas)

#acceder por indice a banana
print(frutas[2]) #banana

#recibe un mensaje de agregar a la lista de frutas pera y que solo traiga una manzana
frutas.append("pera")
print(frutas)

frutas.remove("manzana")
print(frutas)