# main.py
from mainProg import Persona

# Solicitar el nombre, edad y altura del usuario
nombre = input("¿Qué tal, cuál es tu nombre?: ")
edad = int(input("¿Cuál es tu edad?: "))
altura = float(input("¿Cuál es tu altura (en metros)?: "))

# Crear una instancia de la clase Persona
persona = Persona(nombre, edad, altura)

# Llamar a los métodos de la clase Persona
persona.caracteristicas()
persona.validateEdad()
