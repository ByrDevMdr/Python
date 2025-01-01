from person import Persona as p
# Se establece el nombre de las variables a pasar como argumentos.
nombre=input("¿Cuál es su nombre?: ")
edad =int(input("¿Qué edad tiene?: "))
residencia=input("¿Dónde vive?: ")
# Se crea una instancia de la clase.
person=p(nombre,edad,residencia)
# Se mandan a llamar las funciones corresponcientes del módulo.
person.caracteristicas()
# person.confirmN()
person.confirmNMatch()
person.confirmEdad()
# print("Lo que hay disponible es: )
print(dir(p))