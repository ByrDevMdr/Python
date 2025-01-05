lista=[1,2,3,4,5]
longitud=len(lista)
print(f"El tamaño de la lista es: {longitud}")
for i in range(longitud):
    print(f"El elemento del indice {i} es: {lista[i]}")
print("Segunda forma de enumerar elementos.")
for indice,elemento in enumerate(lista):
    print(f"El elemento en el índice {indice} es: {elemento}")