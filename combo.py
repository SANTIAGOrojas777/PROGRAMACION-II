import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#Crear la ventana principal

ventana=tk.Tk()
ventana.title("Ejemplo Combobox")
ventana.geometry("300x200")

#Etiquetas

etiqueta=tk.Label(ventana, text="Seleccionar especialidad:")
etiqueta.grid(row=0, column=0, pady=10, padx=10, sticky="w")

#Crear Combobox

opciones=["Cardiología", "Neurología", "Pediatría", "Dermatología"]
combo=ttk.Combobox(ventana, values=opciones, state="readonly")
combo.current(0)
combo.grid(row=0, column=1, padx=10, pady=10)

#Funcion mostrar la seleccion

def mostrar():
    seleccion=combo.get()
    tk.messagebox.showinfo("Selección", f"Has elegido: {seleccion}")
    
#Boton para confirmar la seleccion

boton=tk.Button(ventana, text="Aceptar", command=lambda:mostrar())
boton.grid(row=1, column=0, columnspan=2, pady=15)

ventana.mainloop()