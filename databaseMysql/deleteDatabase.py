from conexion import *
from readDatabase import *
class Remove:
    def __init__(self,conexion,cursor):
        self.conexion=conexion
        self.cursor=cursor
    def eliminar(self):
        try:
            lector = Read(self.conexion, self.cursor)
            lector.imprimir()
            id=input("Ingrese el registro que desea eliminar: ")
            id = int(id)

            check_query = "SELECT COUNT(*) FROM Empleado WHERE Id = %s"
            self.cursor.execute(check_query, (id,))
            result = self.cursor.fetchone()

            if result[0] == 0:
                print(f"No existe un registro con el Id {id}.")
                return
            
            deleteQ="Delete from Empleado where Id = %s"
            # print(deleteQ)
            self.cursor.execute(deleteQ,(id,))
            self.conexion.commit()
            print("El registro se ha elminado con exito")
        except ValueError:
            print("Favor de ingresar un número valido.")

