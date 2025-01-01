import mysql.connector

def conectar():
    """
    Establece la conexión con la base de datos y devolver el objeto de conexión.
    """
    try:
        conexion = mysql.connector.connect(
            user="root", # Acá poner el usuario.
            password="", # Acá poner la contraseña (si no tiene dejarlo vacio).
            host="localhost", # Acá poner el servidor (por su dirección o nombre).
            database="Python", # Acá poner el nombre de la base de datos a la que nos conectaremos.
            port="3306" # Poner el puerto por el que trabaja mysql (3306)
        )
        print("Conexión exitosa a la base de datos.")
        return conexion
    except mysql.connector.Error as err:
        print(f"Error al conectar con la base de datos: {err}")
        return None

def obtener_cursor(conexion):
    """
    Crea y devuelve un cursor a partir de la conexión dada.
    """
    if conexion:
        return conexion.cursor()
    else:
        print("Conexión inválida. No se puede crear el cursor.")
        return None
