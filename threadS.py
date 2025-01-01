import subprocess
# Comando para listar directorios
cmd = "dir"  # dir para windows / ls para linux o macOs
# Ejecuta el comando
result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
# print(result.returncode)
# print(result.stdout.split)
# print(result.stdout) (el stdout sirve para formatear la salida)
if result.returncode == 0:
    # Procesa la salida para buscar un directorio
    outLines = result.stdout.splitlines()
    directoryName = "pictures"  # Filtrado del nombre del directrio que se busca.
    found = False
    for line in outLines:
        if directoryName in line:
            found = True
            print(f"Directorio encontrado: {directoryName}")
            cmdCd = f"cd {directoryName} && dir"  # Cambia 'dir' por 'ls' en Linux/macOS
            cmdResult = subprocess.run(cmdCd, shell=True, capture_output=True, text=True)
            print("Contenido del directorio:")
            print(cmdResult.stdout)
            break

    if not found:
        print(f"El directorio '{directoryName}' no se encontró.")
else:
    print("Error al ejecutar el comando:")
    print(result.stderr)
