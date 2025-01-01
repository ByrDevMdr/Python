list0=[19,10,22,11]
list1=[12,19,20,78]
list2=[1,2,3,4]
list3=["java","python","ruby","perl"]
print("Impresión de las listas y ordenamiento de estas.")
print(list0) # Imprimirá la lista completa.
list0.sort() # La función sort, ordeará la lista de menor a mayor.
print(list0)
list0.sort(reverse=True) # La función sort, también puede ordenar al revés la lista que se le presente, esto poniendo el prámetro reverse en True.
print(list0)
# Otra forma de ordenar una lista con la función sorted.
Lista_S=sorted(list0,reverse=True) # False sirve solo para indicar que lo ordené de forma ascendente.s
print(Lista_S)

# Manipulación de ls segunda lista.
print("\nManipulación de la segunda lista.")

list1.append(2009) # La función append, agregará el elemento que se le pase como parámetro al final de la lista.
print(list1)
list1.insert(2,16) # La función insert, agregará el elemneto que se le pase como segundo parámetro, al índice que se le indique.
print(list1)

print("\nManipulación de la tercer lista.")
 
list2.extend([5,6]) # La función extend, sirve para agregar n cantidad de elementos a una lista al final.
print(list2) 
# La funación remove, elimina el primer elemento de la lista que coincida con el parámetro dado.
# valueRemove=int(input("Ingrese el numero que desea remover: "))
# list2.remove(valueRemove) # La función remove sirve para quitar un elemento de una lista. Dicho elemento, se pasa como parámetro y tiene la primer coincidencia n la lista se eliminará.
# print(list2)
# La función pop elimina el valor de un índice proporicionado como parámetro.
# item=list2.pop(1) # La función pop, elimina un elemento dada su posición o su índice como parámetro.
# print(item) # La función pop es capaz de devolver el elemento que se le indicó para eliminar.
# print(list2)
# La función clear elimina todos los elementos de una lista.
# list.clear()
# print(list)  # []
print(list2.index(4)) # La función index devuelve el valor dado el índice como parámetro.
# La función print devuelve el numero de veces que un elemento aparace en un arreglo.
print(list2.count(6))
# La función copy devuelve una versión de la lista original.
new_list2=list2.copy()
print(new_list2)
# La función len, devuelve el número de elementos que tiene una lista.
print(len(new_list2))
# La función max, devuelve el elemento con el mayor valor de la lista.
print(max(new_list2))
# La función min, devuelve el elemento con el valor más pequelo de la lista.
print(min(new_list2))
# La función sum, suma todos los elementos de una lista.
print(sum(new_list2))
# La función enum, devuelve un conjunto de valores enumerando una lista. REcibirá dos parámetros, uno que indica la lista y otro que indica el comienzo de la indexación.
for index,value in enumerate(new_list2,1):
    print(index,value)
# La función zip, adjunta dos listas en una salida a manera de tuplas.
listaUnidas=zip(list1,list3)
print(list(listaUnidas))
