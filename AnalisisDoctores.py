#IMPORTACION DE LIBRERIAS
import tkinter as tk
from tkinter import messagebox, ttk
import tkinter.font as font

#FUNCIONES DEL SISTEMA
"""pacientes"""
"""doctores"""
#FUNCION PARA GUARDAR EN ARCHIVO
def guardarArchivoDoctor():
    with open("doctoresRegistro.txt", "w", encoding="utf-8") as archivo:
        for doctor in doctores_data:
            archivo.write(f"""{doctor["Nombre"]}|{doctor["Especialidad"]}|{doctor["Años_Experiencia"]}|{doctor["Sexo"]}|{doctor["Lugar_Trabajo"]}\n""")
            
#FUNCION PARA LEER DESDE ARCHIVO
def cargarDesdeArchivoDoctor():
    try:
        with open("doctoresRegistro.txt", "r", encoding="utf-8") as archivo:
            doctores_data.clear()
            for linea in archivo:
                datos=linea.strip().split("|")
                if len(datos)==5:
                    doctor={
                        "Nombre":datos[0],
                        "Especialidad":datos[1],
                        "Años_Experiencia":datos[2],
                        "Sexo":datos[3],
                        "Lugar_Trabajo":datos[4]
                    }
                    doctores_data.append(doctor)
        cargarTreeviewDoctor()
    except FileNotFoundError:
        open("doctoresRegistro.txt", "w", encoding="utf-8").close()

"lista de doctores vacia"
doctores_data=[]

#FUNCION PARA GUARDAR DOCTORES
def registrarDoctor():
    doctor={
        "Nombre":doctorNombreEntry.get(),
        "Especialidad":doctorEspecialidadVar.get(),
        "Años_Experiencia":doctorExperienciaSpin.get(),
        "Sexo":doctorSexoVar.get(),
        "Lugar_Trabajo":doctorHospitalVar.get()
    }
    doctores_data.append(doctor)
    guardarArchivoDoctor()
    cargarTreeviewDoctor()
    
#FUNCION PARA CARGAR TREEVIEW DOCTORES
def cargarTreeviewDoctor():
    for doctor in treeviewDoctor.get_children():
        treeviewDoctor.delete(doctor)
    for i, item in enumerate(doctores_data):
        treeviewDoctor.insert(
            "", "end", iid=str(i),
            values=(
                item["Nombre"],
                item["Especialidad"],
                item["Años_Experiencia"],
                item["Sexo"],
                item["Lugar_Trabajo"],
                
            )
        )

#CREACION DE VENTANA PRINCIPAL
ventanaPrincipal=tk.Tk()
ventanaPrincipal.title("REGISTRO HOSPITALARIO")
ventanaPrincipal.geometry("800x600")

#CREACION DEL NOTEBOOK
pestañas=ttk.Notebook(ventanaPrincipal)

#CREACION DE PESTAÑAS
framePacientes=tk.Frame(pestañas, bg="silver")
frameDoctores=tk.Frame(pestañas, bg="silver")

#SE AGREGAN PESTAÑAS AL NOTEBOOK
pestañas.add(framePacientes, text="PACIENTES")
pestañas.add(frameDoctores, text="DOCTORES")

#MOSTRAR LAS PESTAÑAS EN LA VENTANA
pestañas.pack(expand=True, fill="both")

#ESTRUCTURAS DE LABEL
estructuraTitulos=font.Font(family="Times New Roman", size=18, weight="bold")
estructuraDatos=font.Font(family="Times New Roman", size=12, weight="bold")

"""PACIENTES"""
#TITULO
pacienteTituloLabel=tk.Label(framePacientes, text="REGISTRO PACIENTES", font=estructuraTitulos, bg="silver")
pacienteTituloLabel.grid(row=0, column=1, sticky="w")
vacio=tk.Label(framePacientes, text="                proximamente...            ", bg="silver")
vacio.grid(row=1, column=0, sticky="w")

#En otra ocasion hare el formulario de pacientes aunque no sea tarea

"""DOCTORES"""
#TITULO
doctorTituloLabel=tk.Label(frameDoctores, text="REGISTRO DOCTORES", font=estructuraTitulos, bg="silver")
doctorTituloLabel.grid(row=0, column=1, sticky="w")

#NOMBRE
doctorNombreLabel=tk.Label(frameDoctores, text="Nombre:", font=estructuraDatos, bg="silver")
doctorNombreLabel.grid(row=1, column=0, padx=5, pady=5, sticky="w")
doctorNombreEntry=tk.Entry(frameDoctores)
doctorNombreEntry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

#ESPECIALIDAD
doctorEspecialidadLabel=tk.Label(frameDoctores, text="Especialidad:", font=estructuraDatos, bg="silver")
doctorEspecialidadLabel.grid(row=2, column=0, padx=5, pady=5, sticky="w")
doctorEspecialidadVar=tk.StringVar()
doctorEspecialidadVar.set("Cardiología")
doctorComboEspecialidad=ttk.Combobox(frameDoctores, values=["Cardiología", "Neurología", "Pediatría", "Traumatología"], textvariable=doctorEspecialidadVar, state="readonly")
doctorComboEspecialidad.grid(row=2, column=1, padx=5, pady=5, sticky="w")

#AÑOS DE EXPERIENCIA
doctorExperienciaLabel=tk.Label(frameDoctores, text="Años de Experiencia:", font=estructuraDatos, bg="silver")
doctorExperienciaLabel.grid(row=3, column=0, padx=5, pady=5, sticky="w")
doctorExperienciaSpin=tk.Spinbox(frameDoctores, from_=1, to=100, state="readonly")
doctorExperienciaSpin.grid(row=3, column=1, padx=5, pady=5, sticky="w")

#SEXO
doctorSexoLabel=tk.Label(frameDoctores, text="Sexo:", font=estructuraDatos, bg="silver")
doctorSexoLabel.grid(row=4, column=0, padx=5, pady=5, sticky="w")

"frame para opciones"
doctor_sexo_frame=tk.Frame(frameDoctores, bg="silver")
doctor_sexo_frame.grid(row=4, column=1, padx=5, pady=5, sticky="w")

doctorSexoVar=tk.StringVar()
doctorSexoVar.set("Masculino")
doctorMasculinoRadio=tk.Radiobutton(doctor_sexo_frame, text="Masculino", variable=doctorSexoVar, value="Masculino", bg="silver")
doctorMasculinoRadio.grid(row=0, column=0, sticky="w")
doctorFemeninoRadio=tk.Radiobutton(doctor_sexo_frame, text="Femenino", variable=doctorSexoVar, value="Femenino", bg="silver")
doctorFemeninoRadio.grid(row=1, column=0, sticky="w")

#HOSPITAL DONDE TRABAJA
doctorHospitalLabel=tk.Label(frameDoctores, text="Lugar de Trabajo:", font=estructuraDatos, bg="silver")
doctorHospitalLabel.grid(row=5, column=0, padx=5, pady=5, sticky="w")
doctorHospitalVar=tk.StringVar()
doctorHospitalVar.set("Hospital Central")
doctorComboHospital=ttk.Combobox(frameDoctores, values=["Hospital Central", "Hospital Norte", "Clínica Santa Maria", "Clínica Vida"], textvariable=doctorHospitalVar, state="readonly")
doctorComboHospital.grid(row=5, column=1, padx=5, pady=5, sticky="w")

#BOTON REGISTRAR
doctorBotonRegistrar=tk.Button(frameDoctores, text="Guardar", command=lambda:registrarDoctor(), bg="silver")
doctorBotonRegistrar.grid(row=6, column=1, padx=5, pady=5, sticky="w")

#TREEVIEW DE DOCTORES
treeviewDoctor=ttk.Treeview(frameDoctores, columns=("Nombre", "Especialidad", "Años_Experiencia", "Sexo", "Lugar_Trabajo"), show="headings")
#DEFINIR ENCABEZADOS
treeviewDoctor.heading("Nombre", text="Nombre Completo")
treeviewDoctor.heading("Especialidad", text="Especialidad")
treeviewDoctor.heading("Años_Experiencia", text="Años de Experiencia")
treeviewDoctor.heading("Sexo", text="Sexo")
treeviewDoctor.heading("Lugar_Trabajo", text="Lugar de Trabajo")
#DEFINIR ANCHOS DE COLUMNAS
treeviewDoctor.column("Nombre", width=130, anchor="center")
treeviewDoctor.column("Especialidad", width=120, anchor="center")
treeviewDoctor.column("Años_Experiencia", width=159, anchor="center")
treeviewDoctor.column("Sexo", width=130, anchor="center")
treeviewDoctor.column("Lugar_Trabajo", width=160, anchor="center")
#UBICAR EL TREEVIEW EN LA CUADRICULA
treeviewDoctor.grid(row=7, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)
#SCROLLBAR VERTICAL
scroll_y2=ttk.Scrollbar(frameDoctores, orient="vertical", command=treeviewDoctor.yview)
treeviewDoctor.configure(yscrollcommand=scroll_y2.set)
scroll_y2.grid(row=7, column=2, sticky="ns")

cargarDesdeArchivoDoctor()

ventanaPrincipal.mainloop()