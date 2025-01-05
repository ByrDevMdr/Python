import os

user = os.environ.get("USERNAME") or os.environ.get("USER") or "Unknown"
print(f"Bienvenido, {user}")

set1 = ['2', '4', '6', '8']
set2 = ['4', '8', '10', '12']

def recorrer1():
    for i, valor in enumerate(set1):
        print(f"El valor del índice {i} es: {valor}")

def recorrer2():
    for i, valor in enumerate(set2):
        print(f"El valor del índice {i} es: {valor}")

while True:
    try:
        opcion = int(input("¿Qué desea realizar? \n\t 1. Intersectar. \n\t 2. Unir. \n\t 3. Salir\n")) #Se agrega opcion para salir y se convierte a int
        if opcion == 1:
            # Intersección
            interseccion = list(set(set1) & set(set2)) #Se realiza la interseccion convirtiendo las listas en sets
            print("Intersección:", interseccion)
            receorrer1() #Se llama a la funcion para recorrer set1
        elif opcion == 2:
            # Unión
            union = list(set(set1) | set(set2)) #Se realiza la union convirtiendo las listas en sets
            print("Unión:", union)
            recorrer2() #Se llama a la funcion para recorrer set2
        elif opcion == 3:
            print("Saliendo del programa.")
            break #Se rompe el bucle while para salir del programa
        else:
            print("Opción no válida. Por favor, ingrese 1, 2 o 3.")
    except ValueError:
        print("Error: Por favor, ingrese un número entero.")