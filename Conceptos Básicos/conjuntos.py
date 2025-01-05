''' Un conjunto es una estructura de datos que se utiliza para alamcenar 
una colección de datos desordenada de elementos únicos
'''
import time # Librería para usar la función sleep.
import os
cls="cls"
lista=[ 1,2,3,4,5,5]
conjunto=set(lista)
print(f"El conjunto sin elementos repetidos es: {conjunto}")
time.sleep(2) # Se retarda por 2 segundos.
os.system(cls) # Limpiar el buffer. 

print("** Método intersection() ** ") # Se utiliza para encontrar elementos comunes entre uno o mas conjuntos.
conjunto1={1,2,3,4} 
conjunto2={3,4,5,6}
conjunto3={4,5,6,6}
conjunto4={4,5,6,7,8}
intersectionC=conjunto1.intersection(conjunto2,conjunto3,conjunto4)
print(f"Los numeros que coinciden en los tres conjuntos son: {intersectionC}")
'''
En el emétodo intersection() se llevan como argumentos los conjuntos con los cuales se comparará 
el elemento al que se le aplicará el método
'''
time.sleep(1)
print("** Método union() **") # Se utiliza para concatenar dos conjuntos quitando los elementos repetidos.
unionC=conjunto1.union(conjunto4)
print(f"La unión del primer conjunto y el cuarto queda: {unionC}")
'''
En el emétodo union() se llevan como argumentos los conjuntos con los cuales se concatenará 
el elemento al que se le aplicará el método
'''

