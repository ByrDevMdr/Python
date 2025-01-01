import os
ruta = "../../Escritorio" # '.' -> Representa que se buscará en el diredtorio actual. 
directory = "Prueba"
# Buscar directorio específico
directorios = [entrada.name for entrada in os.scandir(ruta) if entrada.is_dir() and entrada.name == directory]
if directorios:
    print(f"Directorio encontrado: {directorios[0]}")
    os.chdir(f"../../Escritorio/{directory}")
    # os.system(f"cd ../../Escritorio/{directory}")
    print(f"Ahora estás en: {os.getcwd()}")  # Verifica la nueva ubicación

else:
    print(f"El directorio '{directory}' no se encontró.")
