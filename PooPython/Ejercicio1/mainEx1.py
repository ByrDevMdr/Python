class Form:
    def __init__(self,name,age,opcion):
        self.Name = name
        self.Age =age
        self.Opc = opcion
    # ***** Función range(): range(10) -> Díez numeros en total; *****
    # ***** Función range(): range(0,9) -> Números del cero al nueve; *****
    # ***** Función range(): range(0,11,2) -> Rango del cero al díez de dos en dos; *****
    # ***** Función range(): range(10,0,-1) -> Rango descendente del 10 al 0; *****
    def validarEdad(self):
        if self.Age >= 18:
            print("Usted es mayor de edad.")
        elif range(12,17):
            print("Usted es un adolescente")
        elif range(6,11):
            print("Usted es un niño.")
        elif range(0,5):
            print("USted es un bebé")
        elif range(19,27):
            print("Usted es un adulto joven.")
    def bif(self):
        print(f"Usted ha elegido la opción {self.Opc}")