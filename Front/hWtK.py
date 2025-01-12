import tkinter as tk
from tkinter import messagebox

def centrer(ventana):
    ventana.update_idletasks()  # Importante para obtener las dimensiones correctas
    ancho_ventana = ventana.winfo_width()
    alto_ventana = ventana.winfo_height()
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    y = (alto_pantalla // 2) - (alto_ventana // 2)
    ventana.geometry(f"+{x}+{y}")

ventana = tk.Tk()
ventana.title("Programa elaborado por Byron Medrano")
ventana.geometry("300x200")
centrer(ventana)

def showMessage():
    messagebox.showinfo("Saludo", "¡Hola desde la ventana principal!")

boton = tk.Button(ventana, text="Saludar", command=showMessage)
boton.pack(pady=20)  # Añade un espacio vertical alrededor del botón

ventana.mainloop()