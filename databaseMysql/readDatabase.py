from conexion import *
class Read:
    def __init__(self, conexion, cursor):
        self.conexion = conexion  # Guarda la conexión como atributo
        self.cursor = cursor      # Guarda el cursor como atributo

    def imprimir(self):
        try:
            # Imprimir el contenido de la tabla
            showTableEmp = "Select * From Empleado"
            self.cursor.execute(showTableEmp)
            # Obtener los resultados de la consulta
            content = self.cursor.fetchall()
            if content:
                print("Contenido de la tabla 'Empleado':")
                for cont in content:
                    print(cont)
            else:
                print("La tabla 'Empleado' está vacía.")
        except Exception as e:
            print(f"Error al leer los datos: {e}")
