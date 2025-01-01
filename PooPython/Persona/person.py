class Persona:
    def __init__(self,nombre,edad,residencia):
        self.nombre=nombre
        self.edad=edad
        self.residencia=residencia
    def caracteristicas(self):
        print(f"Hola, {self.nombre}, usted tiene {self.edad} y vive en {self.residencia}")
        # Uso de condiconales
    def confirmN(self):
        if self.nombre == "Byron" or self.nombre=="admin":
            print ("Usted es administrador, bienvenido")
        elif self.nombre == "Javier" or self.nombre=="Emp":
            print ("Usted es un emploeado")
        else:
            print("Usted no tiene acceso a este sistema")
            # Uso de match
    def confirmNMatch(self):
        match self.nombre:
            case "Byron" | "admin":
                print("Usted es administrador, bienvenido")
            case "Javier" | "Emp":
                print("Usted es un empleado")
            case _:
                print("Usted no tiene acceso a este sistema")
    def confirmEdad(self):
        match self.edad:
            case edad if 0 <= edad <= 17:
                print("Usted es menor de edad")
            case edad if 18 <= edad <= 29:
                print("Usted es un adulto joven")
            case edad if 30 <= edad <= 64:
                print("Usted es un adulto")
            case edad if edad >= 65:
                print("Usted es un adulto mayor")
            case _:
                print("Edad no válida")