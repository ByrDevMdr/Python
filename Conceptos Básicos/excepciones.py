lista=[1,2,3]
print("** Expeción de indice. **")
try:
    elemento = lista[5]
except IndexError:
    print("\t Error: Índice fuera de rango.")
    
print("** Exepción de tipo de dato. **")
try:
    numero=int("Byron")
except ValueError:
    print("\t Error: Tipo de dato incorrecto.")

print("** Exepción para un archvio no encontrado. **")
try:
    with open("FileNotExist.txt","r") as archivo: # Abrir un archivo.
        contenido=archivo.read()
except FileNotFoundError:
    print("\t Error: Archivo no encontrado.")

print("** Excepción de operación no permitida. **")
try: 
    resultado= "Byron" + 5
except TypeError:
    print("\t Error: Operación no permitida.")

print("** Exepción de una librería incorrecta. **")
try:
    import LibreríaNull
except ImportError:
    print("\t Error: Librería invalida.")
