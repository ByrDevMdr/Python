from conexion import *
class Add:
    def __init__(self,conexion,cursor):
        self.conexion = conexion
        self.cursor = cursor
    def agregar(self):
        nombre = input("Ingrese el nombre del empleado: ").strip()
        apellido = input("Ingrese el apellido del empleado: ").strip()
        salario = float(input("Ingrese el salario del empleado: "))
        if not nombre or not apellido:
            print("El nombre y el apellido no pueden estar vacíos.")
            return
        insert_query = """
        Insert into Empleado (Nombre, Apellido, Salario)
        values (%s, %s, %s)
        """
        self.cursor.execute(insert_query, (nombre, apellido, salario))
        self.conexion.commit()  # Confirmar los cambios

        print("✔ Empleado agregado exitosamente.")