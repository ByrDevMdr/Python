import time
import os
cls="cls"
def recorrer():
    for clave,valor in colores.items():
        print(f"El contenido de {clave} -> {valor}")
# Creación de diccionario: llave -> valor.
colores={'red':'rojo','green':'verde','blue':'azul'}
print("Diccionario original: ")
recorrer()
time.sleep(3)
os.system(cls)

print("Acceder a un elemento por su llave.")
# Acceder a un elemento por medio de su llave.
print(colores['red']) # Salida: rojo.
time.sleep(2)
os.system(cls)

print("Agregar un nuevo valor: ")
# Agregar un nuevo elemento al diccionario.
colores['yellow'] = 'amarillo'
recorrer()
time.sleep(3)
os.system(cls)


print("Modifica un valor.")
# Modificar un valor del diccionario.
colores['red'] = 'Rojo'
recorrer()
time.sleep(3)
os.system(cls)

print("** Elimina un valor del diccionario **")
# Eliminar un elemento del diccionario.
del colores['blue']
recorrer()
time.sleep(3)
os.system(cls)

print("** Verificar si una llave está en el diccionario. **")
# Verificar si una clave está en el diccionario.
print('red' in colores) # Salida True.
print('blue' in colores) # Salida False.
