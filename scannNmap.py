# ******* Para usar la librería nmap debe de ejecutar este comando en la consola 
# estando en la dirección del script:
# pip install python-nmap ********
import nmap
# Crear un objeto de PortScanner.
nm = nmap.PortScanner()
# Escanear la red con el prefijo 24 indicando el rango.
nm.scan("192.168.1.0/24") # Poner la dirección IP de la red a la que esté conectado.
# Indicar el rango de direcciones que desea escanear 24 siendo el máximo.  
# Mostrar todos los hosts detectados en la red.
print(nm.scaninfo())  # Información del escaneo
print(nm.all_hosts())
# Mostrar los métodos disponibles en el módulo nmap.
# print(dir(nmap))
