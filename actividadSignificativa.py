import tkinter as tk
from tkinter import messagebox, ttk
import tkinter.font as font
from datetime import datetime

"""FUNCIONES DEL FORMULARIO"""
#FUNCION PARA ENMASCARAR FECHA
def enmascarar_fecha(texto):
    limpio="".join(filter(str.isdigit, texto))
    formato_final=""
    if len(limpio)>8:
        limpio=limpio[:8]
    if len(limpio)>4:
        formato_final=f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
    elif len(limpio)>2:
        formato_final=f"{limpio[:2]}-{limpio[2:]}"
    else:
        formato_final=limpio
    if FechaEntryP.get()!=formato_final:
        FechaEntryP.delete(0, tk.END)
        FechaEntryP.insert(0, formato_final)
    if len(FechaEntryP.get())==10:
        fecha_actual=datetime.now().date()
        fecha_nacimiento=datetime.strptime(FechaEntryP.get(), "%d-%m-%Y").date()
        edad=fecha_actual.year-fecha_nacimiento.year
        edadVar.set(edad)
    else:
        edadVar.set("")
    return True

#FUNCION PARA GUARDAR EL REGISTRO
def guardar_en_archivo():
    with open("PacientePeso.txt", "w", encoding="utf-8") as archivo:
        for paciente in paciente_data:
            archivo.write(f"""{paciente["Nombre"]}|{paciente["Fecha de Nacimiento"]}|{paciente["Edad"]}|{paciente["Peso"]}|{paciente["Género"]}|{paciente["Grupo Sanguíneo"]}|{paciente["Tipo de Seguro"]}|{paciente["Centro Médico"]}\n""")

#FUNCION PARA CARGAR DESDE EL ARCHIVO
def cargar_desde_archivo_pacientes():
    try:
        with open("PacientePeso.txt", "r", encoding="utf-8") as archivo:
            paciente_data.clear()
            for linea in archivo:
                datos=linea.strip().split("|")
                if len(datos)==8:
                    paciente={
                        "Nombre":datos[0],
                        "Fecha de Nacimiento":datos[1],
                        "Edad":datos[2],
                        "Peso":datos[3],
                        "Género":datos[4],
                        "Grupo Sanguíneo":datos[5],
                        "Tipo de Seguro":datos[6],
                        "Centro Médico":datos[7]
                    }
                    paciente_data.append(paciente)
        cargar_treeview()
    except FileNotFoundError:
        open("PacientePeso.txt", "w", encoding="utf-8").close()

#FUNCION PARA ELIMINAR REGISTRO DE PACIENTE
def eliminarPaciente():
    seleccionado=treeview.selection()
    if seleccionado:
        indice=int(seleccionado[0])
        id_item=seleccionado[0]
        if messagebox.askyesno("Eliminar Paciente", f"¿Estas seguro de eliminar el paciente '{treeview.item(id_item, 'values')[0]}'?"):
            del paciente_data[indice]
            guardar_en_archivo()
            cargar_treeview()
            messagebox.showinfo("Eliminar Paciente", "Paciente eliminado exitosamente")
    else:
        messagebox.showwarning("Eliminar Paciente", "No se ha seleccionado ningun paciente")
        return
        
#LISTA DE PACIENTES
paciente_data=[]

#FUNCION PARA REGISTRAR PACIENTES
def registrarPaciente():
    paciente={
        "Nombre":NombreEntryP.get(),
        "Fecha de Nacimiento":FechaEntryP.get(),
        "Edad":edadVar.get(),
        "Peso":entryPeso.get(),
        "Género":genero.get(),
        "Grupo Sanguíneo":GrupoSanguineoEntry.get(),
        "Tipo de Seguro":tipoSeguro.get(),
        "Centro Médico":centroMedico.get()
    }
    #AGREGAR PACIENTE A LA LISTA
    paciente_data.append(paciente)
    #LLAMANDO A LA FUNCION PARA GUARDAR EN ARCHIVO
    guardar_en_archivo()
    #CARGAR EL TREEVIEW
    cargar_treeview()
    
#FUNCION PARA CARGAR TREEVIEW
def cargar_treeview():
    #LIMPIAR EL TREEVIEW
    for paciente in treeview.get_children():
        treeview.delete(paciente)
    #INSERTAR PACIENTE
    for i, item in enumerate(paciente_data):
        treeview.insert(
            "", "end", iid=str(i),
            values=(
                item["Nombre"],
                item["Fecha de Nacimiento"],
                item["Edad"],
                item["Peso"],
                item["Género"],
                item["Grupo Sanguíneo"],
                item["Tipo de Seguro"],
                item["Centro Médico"]
            )
        )



#CREACION DE LA VENTANA PRINCIPAL
ventanaPrincipal=tk.Tk()
ventanaPrincipal.title("REGISTRO HOSPITALARIO")
ventanaPrincipal.geometry("800x700")

#SE CREA EL NOTEBOOK
pestañas=ttk.Notebook(ventanaPrincipal)

#SE CREAN LAS PESTAÑAS
framePacientes=tk.Frame(pestañas, bg="silver")

#SE AGREGAN PESTAÑAS AL NOTEBOOK
pestañas.add(framePacientes, text="PACIENTES")

#MOSTRAR LAS PESTAÑAS EN LA VENTANA
pestañas.pack(expand=True, fill="both")

#ESTRUCTURAS DE LABEL
estructuraTitulos=font.Font(family="Times New Roman", size=18, weight="bold")
estructuraDatos=font.Font(family="Times New Roman", size=12, weight="bold")

"""PACIENTES"""
#TITULO
tituloPacientesLabel=tk.Label(framePacientes, text="FORMULARIO DE PACIENTES", font=estructuraTitulos, bg="silver")
tituloPacientesLabel.grid(row=0, column=1, sticky="w", padx=5, pady=5)

#NOMBRE
labelNombreP=tk.Label(framePacientes, text="Nombre Completo:", font=estructuraDatos, bg="silver")
labelNombreP.grid(row=1, column=0, sticky="w", pady=5, padx=5)
NombreEntryP=tk.Entry(framePacientes)
NombreEntryP.grid(row=1, column=1, sticky="w", pady=5, padx=5)

#FECHA DE NACIMIENTO
labelFechaP=tk.Label(framePacientes, text="Fecha de Nacimiento:", font=estructuraDatos, bg="silver")
labelFechaP.grid(row=2, column=0, sticky="w", pady=5, padx=5)
validacion_fecha=ventanaPrincipal.register(enmascarar_fecha)
FechaEntryP=ttk.Entry(framePacientes, validate="key", validatecommand=(validacion_fecha, "%P"))
FechaEntryP.grid(row=2, column=1, sticky="w", pady=5, padx=5)

#EDAD
labelEdadP=tk.Label(framePacientes, text="Edad:", font=estructuraDatos, bg="silver")
labelEdadP.grid(row=3, column=0, sticky="w", pady=5, padx=5)
edadVar=tk.StringVar()
EdadEntryP=tk.Entry(framePacientes, textvariable=edadVar, state="readonly")
EdadEntryP.grid(row=3, column=1, sticky="w", pady=5, padx=5)

#PESO
labelPeso=tk.Label(framePacientes, text="Peso (kg):", font=estructuraDatos, bg="silver")
labelPeso.grid(row=4, column=0, sticky="w", pady=5, padx=5)
entryPeso=tk.Entry(framePacientes)
entryPeso.grid(row=4, column=1, sticky="w", padx=5, pady=5)

#GENERO
labelGenero=tk.Label(framePacientes, text="Género:", font=estructuraDatos, bg="silver")
labelGenero.grid(row=5, column=0, sticky="w", pady=5, padx=5)
genero=tk.StringVar()
genero.set("Masculino")
framegenero=tk.Frame(framePacientes, bg="silver")
framegenero.grid(row=5, column=1, sticky="w", padx=5, pady=5)
radioMasculino=tk.Radiobutton(framegenero, text="Masculino", variable=genero, value="Masculino", bg="silver")
radioMasculino.grid(row=0, column=0, sticky="w", padx=5)
radioFemenino=tk.Radiobutton(framegenero, text="Femenino", variable=genero, value="Femenino", bg="silver")
radioFemenino.grid(row=0, column=1, sticky="w", padx=5)

#GRUPO SANGUINEO
labelGrupoSanguineo=tk.Label(framePacientes, text="Grupo Sanguíneo:", font=estructuraDatos, bg="silver")
labelGrupoSanguineo.grid(row=6, column=0, sticky="w", padx=5, pady=5)
GrupoSanguineoEntry=tk.Entry(framePacientes)
GrupoSanguineoEntry.grid(row=6, column=1, sticky="w", pady=5, padx=5)

#TIPO DE SEGURO
labelTipoSeguro=tk.Label(framePacientes, text="Tipo de Seguro:", font=estructuraDatos, bg="silver")
labelTipoSeguro.grid(row=7, column=0, sticky="w", padx=5, pady=5)
tipoSeguro=tk.StringVar()
tipoSeguro.set("Público")
comboTipoSeguro=ttk.Combobox(framePacientes, values=["Público", "Privado", "Ninguno"], textvariable=tipoSeguro, state="readonly")
comboTipoSeguro.grid(row=7, column=1, sticky="w", pady=5, padx=5)

#CENTRO MEDICO
labelCentroMedico=tk.Label(framePacientes, text="Centro de Salud:", font=estructuraDatos, bg="silver")
labelCentroMedico.grid(row=8, column=0, sticky="w", padx=5, pady=5)
centroMedico=tk.StringVar()
centroMedico.set("Hospital Central")
comboCentroMedico=ttk.Combobox(framePacientes, values=["Hospital Central", "Clínica Norte", "Centro Sur"], textvariable=centroMedico, state="readonly")
comboCentroMedico.grid(row=8, column=1, sticky="w", pady=5, padx=5)

#FRAME PARA LOS BOTONES
btn_frame=tk.Frame(framePacientes, bg="silver")
btn_frame.grid(row=10, column=1, columnspan=2, pady=5, sticky="w")

#BOTON PARA REGISTRAR
btn_registrar=tk.Button(btn_frame, text="Registrar", command=lambda:registrarPaciente(), bg="green")
btn_registrar.grid(row=0, column=0, padx=5)

#BOTON ELIMINAR
btn_eliminar=tk.Button(btn_frame, text="Eliminar", command=lambda:eliminarPaciente(), bg="red")
btn_eliminar.grid(row=0, column=1, padx=5)

#CREAR TREEVIEW PARA MOSTRAR PACIENTES
treeview=ttk.Treeview(framePacientes, columns=("Nombre", "FechaN", "Edad", "Peso", "Genero", "GrupoS", "TipoS", "CentroM"), show="headings")

#DEFINIR ENCABEZADOS
treeview.heading("Nombre", text="Nombre Completo")
treeview.heading("FechaN", text="Fexha Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Peso", text="Peso")
treeview.heading("Genero", text="Género")
treeview.heading("GrupoS", text="Grupo Sanguíneo")
treeview.heading("TipoS", text="Tipo Seguro")
treeview.heading("CentroM", text="Centro Médico")

#DEFINIR ANCHOS DE COLUMNAS
treeview.column("Nombre", width=120, anchor="center")
treeview.column("FechaN", width=120, anchor="center")
treeview.column("Edad", width=50, anchor="center")
treeview.column("Peso", width=50, anchor="center")
treeview.column("Genero", width=60, anchor="center")
treeview.column("GrupoS", width=100, anchor="center")
treeview.column("TipoS", width=100, anchor="center")
treeview.column("CentroM", width=120, anchor="center")

#UBICAR EL TREEVIEW EN LA CUADRICULA
treeview.grid(row=9, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)

#SCROLLBAR VERTICAL
scroll_y=ttk.Scrollbar(framePacientes, orient="vertical", command=treeview.yview)
treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=9, column=2, sticky="ns")

cargar_desde_archivo_pacientes()

ventanaPrincipal.mainloop()
