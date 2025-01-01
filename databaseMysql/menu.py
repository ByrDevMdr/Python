from readDatabase import Read
from agregarDatabase import Add
from deleteDatabase import Remove
from updateDatabase import Update
class Menu:
    def __init__(self, conexion, cursor):
        self.conexion = conexion
        self.cursor = cursor

    def showMenu(self):
        while True:
            print("\nMenú Principal:")
            print("1. Mostrar contenido de la tabla 'Empleado'")
            print("2. Agregar un empleado a la tabla.")
            print("3. Eliminar un registro de la tabla.")
            print("4. Actualizar un registro de la tabla.")
            print("0. Salir")
            choice = input("Elige una opción: ")
            if choice == "1":
                lector = Read(self.conexion, self.cursor)
                lector.imprimir()
            elif choice == "2":
                agregar = Add(self.conexion,self.cursor)
                agregar.agregar()
            elif choice == "3":
                eliminar = Remove(self.conexion,self.cursor)
                eliminar.eliminar()
            elif choice == "4":
                actualizar = Update(self.conexion,self.cursor)
                actualizar.actualizar()
            elif choice == "0":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
