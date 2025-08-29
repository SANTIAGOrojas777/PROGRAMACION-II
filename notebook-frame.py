import tkinter as tk
from tkinter import messagebox, ttk

#CREACION DE LA VENTANA PRINCIPAL
ventanaPrincipal=tk.Tk()
ventanaPrincipal.title("Libro de Pacientes y Doctores")
ventanaPrincipal.geometry("400x600")

#SE CREA EL NOTEBOOK
pestañas=ttk.Notebook(ventanaPrincipal)

#SE CREAN LAS PESTAÑAS
framePacientes=ttk.Frame(pestañas)
frameDoctores=ttk.Frame(pestañas)

#SE AGREGAN PESTAÑAS AL NOTEBOOK
pestañas.add(framePacientes, text="Pacientes")
pestañas.add(frameDoctores, text="Doctores")

#MOSTRAR LAS PESTAÑAS EN LA VENTANA
pestañas.pack(expand=True, fill="both")

#NOMBRE
labelNombreP=tk.Label(framePacientes, text="Nombre Completo:")
labelNombreP.grid(row=0, column=0, sticky="w", pady=5, padx=5)
NombreEntryP=tk.Entry(framePacientes)
NombreEntryP.grid(row=0, column=1, sticky="w", pady=5, padx=5)

#FECHA DE NACIMIENTO
labelFechaP=tk.Label(framePacientes, text="Fecha de Nacimiento:")
labelFechaP.grid(row=1, column=0, sticky="w", pady=5, padx=5)
FechaEntryP=tk.Entry(framePacientes)
FechaEntryP.grid(row=1, column=1, sticky="w", pady=5, padx=5)

#EDAD
labelEdadP=tk.Label(framePacientes, text="Edad:")
labelEdadP.grid(row=2, column=0, sticky="w", pady=5, padx=5)
EdadEntryP=tk.Entry(framePacientes, state="readonly")
EdadEntryP.grid(row=2, column=1, sticky="w", pady=5, padx=5)

#GENERO
labelGenero=tk.Label(framePacientes, text="Género:")
labelGenero.grid(row=3, column=0, sticky="w", pady=5, padx=5)
genero=tk.StringVar()
genero.set("Masculino")
radioMasculino=ttk.Radiobutton(framePacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, sticky="w", padx=5)
radioFemenino=ttk.Radiobutton(framePacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=3, column=2, sticky="w", padx=5)

#GRUPO SANGUINEO
labelGrupoSanguineo=tk.Label(framePacientes, text="Grupo Sanguíneo:")
labelGrupoSanguineo.grid(row=4, column=0, sticky="w", padx=5, pady=5)
GrupoSanguineoEntry=tk.Entry(framePacientes)
GrupoSanguineoEntry.grid(row=4, column=1, sticky="w", pady=5, padx=5)

#TIPO DE SEGURO
labelTipoSeguro=tk.Label(framePacientes, text="Tipo de Seguro:")
labelTipoSeguro.grid(row=5, column=0, sticky="w", padx=5, pady=5)
tipoSeguro=tk.StringVar()
tipoSeguro.set("Público")
comboTipoSeguro=ttk.Combobox(framePacientes, values=["Público", "Privado", "Ninguno"], textvariable=tipoSeguro)
comboTipoSeguro.grid(row=5, column=1, sticky="w", pady=5, padx=5)

#CENTRO MEDICO
labelCentroMedico=tk.Label(framePacientes, text="Centro de Salud:")
labelCentroMedico.grid(row=6, column=0, sticky="w", padx=5, pady=5)
centroMedico=tk.StringVar()
centroMedico.set("Hospital Central")
comboCentroMedico=ttk.Combobox(framePacientes, values=["Hospital Central", "Clínica Norte", "Centro Sur"], textvariable=centroMedico)
comboCentroMedico.grid(row=6, column=1, sticky="w", pady=5, padx=5)

ventanaPrincipal.mainloop()