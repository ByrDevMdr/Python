from menu import Menu
from conexion import conectar, obtener_cursor

# Establecer conexión y obtener cursor
conexion = conectar()
cursor = obtener_cursor(conexion)

if cursor:
    # Mostrar bases de datos
    cursor.execute("SHOW DATABASES")
    print("Bases de datos disponibles:")
    for db in cursor:
        print(f"- {db[0]}")

    # Verificar si la tabla 'Empleado' existe
    checkTableQuery = """
    SELECT COUNT(*) 
    FROM information_schema.tables 
    WHERE table_schema = DATABASE() AND table_name = 'Empleado';
    """
    cursor.execute(checkTableQuery)
    table_exists = cursor.fetchone()[0]

    # Crear la tabla si no existe
    if table_exists:
        print("✔ La tabla 'Empleado' ya existe en la base de datos.")
    else:
        print("Creación de tabla:")
        createTableQuery = """
        Create table Empleado (
            Id INT AUTO_INCREMENT PRIMARY KEY,
            Nombre VARCHAR(20),
            Apellido VARCHAR(25),
            Salario DECIMAL(10,2)
        );
        """
        cursor.execute(createTableQuery)
        print("✔ Tabla 'Empleado' creada con éxito.")

    # Crear el menú y pasar la conexión y el cursor
    menu = Menu(conexion, cursor)
    menu.showMenu()

    # Cerrar conexión y cursor
    cursor.close()
    conexion.close()
    print("Conexión cerrada.")
else:
    print("No se pudo establecer la conexión o el cursor.")

# flag=cursor.fetchone()[0]
# # Creación de tabla con condicioante.
# print("Creación de tabla: ")
# # Se mete el comando en una variable que despúes se meterá como argumento para la ejecución.
# crateTable="create table if not exists Empleado(Id int auto_increment primary key, Nombre varchar(20),Apellido varchar(25),Salario decimal(10,2))"#
# # Se llama al cursor y se mete el comando como argumento.
# cursor.execute(crateTable)
# print("Tabla creada con éxito")

