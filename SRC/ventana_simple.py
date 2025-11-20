import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Aviso", "Boton presionado")

ventana = tk.Tk()
ventana.title("Ventana simple")

label = tk.Label(ventana, text="Hola,mundo")
label.pack(pady=10)

boton = tk.Button(ventana, text="Haz clic", command=mostrar_mensaje)
boton.pack(pady=10)

ventana.mainloop()