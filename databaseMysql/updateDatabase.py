from conexion import *
from readDatabase import *
class Update:
    def __init__(self,conexion,cursor):
        self.conexion=conexion
        self.cursor=cursor
    def actualizar(self):
        try:
            lector=Read(self.conexion,self.cursor)
            lector.imprimir()
            id=input("Ingrese el registro que quiere actualizar: ")
            id=int(id)
        
            checkQ = "Select count(*) from Empleado where Id = %s"
            self.cursor.execute(checkQ, (id,))
            result = self.cursor.fetchone()

            if result[0] == 0:
                print(f"No existe un registro con el Id {id}.")
                return
            
            # Solicitar nuevos valores
            nombreN = input("Ingrese el nuevo nombre: ")
            apellidoN = input("Ingrese el nuevo apellido: ")
            salarioN = input("Ingrese el nuevo salario: ")

            # Validar que el salario sea un número
            try:
                salarioN = float(salarioN)
            except ValueError:
                print("El salario debe ser un número válido.")
                return

            # Actualizar el registro
            updateQ = """
                Update Empleado 
                set Nombre = %s, Apellido = %s, Salario = %s 
                where Id = %s   
            """
            self.cursor.execute(updateQ, (nombreN, apellidoN, salarioN, id))
            self.conexion.commit()  # Confirmar los cambios

            print(f"El registro con Id {id} ha sido actualizado con éxito.")

        except ValueError:
            print("Por favor, ingrese un número válido para el Id.")