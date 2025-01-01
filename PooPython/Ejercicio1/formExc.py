from mainEx1 import *
print ("Hola")
name=input("Ingrese su nombre, por favor: ")
print(f"Se usted bienvenido, {name}")
edad=int(input(f"{name}, qué edad tiene? ")) # El argumento antes del input indica qué tipo de dato es el que se recibe.
opcion=input('Ingrese el numero de la opción a realizar:/n 1- Imprimir nombre. /n 2- Imprimir "Hola mundo". /n 3- Imprimir ')
# Crear una instancia de la clase Persona
frm = Form(name, edad, opcion)
frm.validarEdad()
frm.bif()
# print(f"{edad}")
# if edad == 19:
#     print("Usted tiene 19 años!")
# elif edad < 19:
#     print("Usted es menor de 19 años.")
# else:
#     print("Usted es mayor de 19 años.")