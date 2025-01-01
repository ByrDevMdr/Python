# cadena="Byron"
# for i in cadena:
#     if i == "a":
#         print("Tiene una letra a")
#     else: 
#         print("No tiene una letra \"a\"")
contraseña=False

for i in input("Introduce una contraseña que tenga un arroba, un asterisco y una almohadilla: "):
    if i== "#" and "@" and "*":
        contraseña=True

if contraseña==True:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")