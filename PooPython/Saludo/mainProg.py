# persona.py
class Persona:
    def __init__(self, nombre, edad, altura):
        self.Nombre = nombre
        self.Edad = edad
        self.Altura = altura
    
    def caracteristicas(self):
        print(f"Hola, {self.Nombre}, usted tiene {self.Edad} años y mide {self.Altura:.2f} metros")
    
    def validateEdad(self):
        if self.Edad <= 17:
            print("Usted es menor de edad")
        elif 18 <= self.Edad <= 29:
            print("Usted es un adulto joven")
        elif self.Edad >= 30:
            print("Usted es un adulto mayor")
