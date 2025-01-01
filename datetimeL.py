import datetime # Librería para poder sacar la zona horaría del sistema.
all= dir(datetime); # Función para poder ver todas las funciones que incluye una librería, pasandole como parámetro la librería.
print(f"Lo disponible es: {all}")
# Sacar la fecha completa inlcuyendo la hora.
fecha=datetime.datetime.now()
print(f"La fecha es: {fecha}")
# Formateo:
# Hora en formato 00 - 23: %H
# Minutos 00 - 59: %M
# Segundos 00 - 59: %S
# Día de la semana en texto completo [Monday, Tuesday, etc]: %A
# Mes del año en texto completo [January, February, etc]: %B
# PM o AM: %p 
# Mes como numero [1-12]: %m
# Año en cuatro digitos [2000]: %Y
# Día del mes como numero [01 - 31]: %d
hora=datetime.datetime.now()
print(f"La hora es: {hora}")
format=hora.strftime("%I:%M -> %p")
print(f"La hora formateada es: {format}")
# Formato en 24 horas:
format24=hora.strftime("%H:%M -> %p")
print(f"La hora formateada en 24hrs es: {format24}")
# Definir día de la semana.
dayW=datetime.datetime.now()
dayWeek=dayW.strftime("%A")
print(f"EL día de la semana es {dayWeek}")
# Definir el mes del año.
month=datetime.datetime.now()
YearMonth=month.strftime("%Y/%B(%m)/%d")
print(f"La fecha del día de hoy es: {YearMonth}")
# Definición de fecha.
date=datetime.datetime.now()
d=date.strftime("A %d de %B del año %Y día %A a las %I:%M con %S Segundos")
print(f"La fecha es: {d}")  