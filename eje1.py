import tkinter as tk
from tkinter import messagebox
 
def nuevoPaciente():
    ventanaRegistro=tk.Toplevel(ventanaPrincipal)
    ventanaRegistro.title("Registro de Paciente")
    ventanaRegistro.geometry("400x400")
    ventanaRegistro.configure(bg="silver")
   
    nombreLabel=tk.Label(ventanaRegistro,text="Nombre" , bg="silver")
    nombreLabel.grid(row=0,column=0,padx=0,pady=5,sticky="w") #n norte e este etc
    entryNombre=tk.Entry(ventanaRegistro, bg="silver")
    entryNombre.grid(row=0,column=1,padx=10,pady=5,sticky="we")
   
    direccionLabel=tk.Label(ventanaRegistro,text="Direccion" ,bg="silver")
    direccionLabel.grid(row=1,column=0,padx=0,pady=5,sticky="w") #n norte e este etc
    entryDireccion=tk.Entry(ventanaRegistro , bg="silver")
    entryDireccion.grid(row=1,column=1,padx=10,pady=5,sticky="we")
   
    telefonoLabel=tk.Label(ventanaRegistro,text="Telefono" ,bg="silver")
    telefonoLabel.grid(row=2,column=0,padx=0,pady=5,sticky="w") #n norte e este etc
    entryTelefono=tk.Entry(ventanaRegistro, bg="silver")
    entryTelefono.grid(row=2,column=1,padx=10,pady=5,sticky="we")
   
    sexoLabel=tk.Label(ventanaRegistro,text="Sexo" ,bg="silver")
    sexoLabel.grid(row=3,column=0,padx=10, pady=5,sticky="w")
    sexo=tk.StringVar(value="Masculino")
   
    rbMaculino=tk.Radiobutton(ventanaRegistro,text="Maculino",variable=sexo,value="Maculino",bg="silver")
    rbMaculino.grid(row=3,column=1,sticky="w")
    rbFemenino=tk.Radiobutton(ventanaRegistro,text="Femenino",variable=sexo,value="Femenino",bg="silver")
    rbFemenino.grid(row=3,column=2,sticky="w")
   
    enfLabel=tk.Label(ventanaRegistro,text="Enfermedad base",bg="silver")
    enfLabel.grid(row=6,column=0,padx=10,pady=5,sticky="w")
    diabetes=tk.BooleanVar()
    hipertension=tk.BooleanVar()
    asma=tk.BooleanVar()
   
    cbDiabetes=tk.Checkbutton(ventanaRegistro,text="Diabetes",variable=diabetes,bg="silver")
    cbDiabetes.grid(row=5,column=1,sticky="w")
   
    cbHipertension=tk.Checkbutton(ventanaRegistro,text="Hipertension",variable=hipertension,bg="silver")
    cbHipertension.grid(row=6,column=1,sticky="w")
   
    cbAsma=tk.Checkbutton(ventanaRegistro,text="Asma",variable=asma,bg="silver")
    cbAsma.grid(row=7,column=1,sticky="w")
    
    def registarDatos():
        enfermedades=[]
        if diabetes.get():
            enfermedades.append("Diabetes")
        if hipertension.get():
            enfermedades.append("hipertension")
        if asma.get():
            enfermedades.append("Asma")
       
        if len(enfermedades)>0:
            enfermedadesTexto=",".join(enfermedades)
        else:
            enfermedadesTexto="Ninguna"
        info=(
            f"Nombre:{entryNombre.get()}\n"
            f"Direccion:{entryDireccion.get()}\n"
            f"Telefono:{entryTelefono.get()}\n"
            f"Sexo:{sexo.get()}\n"
            f"Enfermedades:{enfermedadesTexto}"
        )
        messagebox.showinfo("Datos Registrados",info)
        ventanaRegistro.destroy()
        
    btnRegistar=tk.Button(ventanaRegistro,text="Datos Registrados", command=registarDatos)
    btnRegistar.grid(row=9,column=0,columnspan=2,pady=15)

def nuevoDoctor():
    ventanaRegistro=tk.Toplevel(ventanaPrincipal)
    ventanaRegistro.title("Registro de Doctores")
    ventanaRegistro.geometry("400x400")
    ventanaRegistro.configure(bg="silver")
   
    nombreLabel=tk.Label(ventanaRegistro,text="Nombre Completo:" , bg="silver")
    nombreLabel.grid(row=0,column=0,padx=0,pady=5,sticky="w")
    entryNombre=tk.Entry(ventanaRegistro, bg="silver")
    entryNombre.grid(row=0,column=1,padx=10,pady=5,sticky="we")
   
    direccionLabel=tk.Label(ventanaRegistro,text="Direccion:" ,bg="silver")
    direccionLabel.grid(row=1,column=0,padx=0,pady=5,sticky="w")
    entryDireccion=tk.Entry(ventanaRegistro , bg="silver")
    entryDireccion.grid(row=1,column=1,padx=10,pady=5,sticky="we")
   
    telefonoLabel=tk.Label(ventanaRegistro,text="Telefono:" ,bg="silver")
    telefonoLabel.grid(row=2,column=0,padx=0,pady=5,sticky="w")
    entryTelefono=tk.Entry(ventanaRegistro, bg="silver")
    entryTelefono.grid(row=2,column=1,padx=10,pady=5,sticky="we")
   
    especialidadLabel=tk.Label(ventanaRegistro,text="Especialidad:" ,bg="silver")
    especialidadLabel.grid(row=3,column=0,padx=10, pady=5,sticky="w")
    especialidad=tk.StringVar(value="Pediatría")
   
    rbPediatria=tk.Radiobutton(ventanaRegistro,text="Pediatría",variable=especialidad,value="Pediatría",bg="silver")
    rbPediatria.grid(row=3,column=1,sticky="w")
    rbCardiologia=tk.Radiobutton(ventanaRegistro,text="Cardiología",variable=especialidad,value="Cardiología",bg="silver")
    rbCardiologia.grid(row=4,column=1,sticky="w")
    rbNeurologia=tk.Radiobutton(ventanaRegistro,text="Neurología",variable=especialidad,value="Neurología",bg="silver")
    rbNeurologia.grid(row=5,column=1,sticky="w")
   
    disponibilidadLabel=tk.Label(ventanaRegistro,text="Disponibilidad:",bg="silver")
    disponibilidadLabel.grid(row=6,column=0,padx=10,pady=5,sticky="w")
    mañana=tk.BooleanVar()
    tarde=tk.BooleanVar()
    noche=tk.BooleanVar()
   
    cbMañana=tk.Checkbutton(ventanaRegistro,text="Mañana",variable=mañana,bg="silver")
    cbMañana.grid(row=6,column=1,sticky="w")
   
    cbTarde=tk.Checkbutton(ventanaRegistro,text="Tarde",variable=tarde,bg="silver")
    cbTarde.grid(row=7,column=1,sticky="w")
   
    cbNoche=tk.Checkbutton(ventanaRegistro,text="Noche",variable=noche,bg="silver")
    cbNoche.grid(row=8,column=1,sticky="w")
   
    def registarDatos():
        disponibilidad=[]
        if mañana.get():
            disponibilidad.append("Mañana")
        if tarde.get():
            disponibilidad.append("Tarde")
        if noche.get():
            disponibilidad.append("Noche")
       
        if len(disponibilidad)>0:
            disponibilidadTexto=",".join(disponibilidad)
        else:
            disponibilidadTexto="Ninguna"
        info=(
            f"Nombre:{entryNombre.get()}\n"
            f"Direccion:{entryDireccion.get()}\n"
            f"Telefono:{entryTelefono.get()}\n"
            f"Especialidad:{especialidad.get()}\n"
            f"Disponibilidad:{disponibilidadTexto}"
        )
        messagebox.showinfo("Datos Registrados",info)
        ventanaRegistro.destroy()
       
    btnRegistar=tk.Button(ventanaRegistro,text="Datos Registrados", command=registarDatos)
    btnRegistar.grid(row=9,column=0,columnspan=2,pady=15)
 
ventanaPrincipal=tk.Tk()
ventanaPrincipal.title("Sistema de Registro de Hospital")
ventanaPrincipal.geometry("600x400")
ventanaPrincipal.configure(bg="silver")
 
barraMenu=tk.Menu(ventanaPrincipal)
ventanaPrincipal.configure(menu=barraMenu)
 
menuPacientes=tk.Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Pacientes", menu=menuPacientes)
menuPacientes.add_command(label="Nuevo Pacientes", command=lambda:nuevoPaciente())
menuPacientes.add_command(label="Buscar Pacientes")
menuPacientes.add_command(label="Eliminar Pacientes")
menuPacientes.add_separator()
menuPacientes.add_command(label="Salir", command=ventanaPrincipal.quit)
 
menuDoctores=tk.Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Doctores", menu=menuDoctores)
menuDoctores.add_command(label="Nuevo Doctor", command=lambda:nuevoDoctor())
menuDoctores.add_command(label="Buscar Doctor")
menuDoctores.add_command(label="Eliminar Doctor")
menuDoctores.add_separator()
menuDoctores.add_command(label="Salir", command=ventanaPrincipal.quit)
 
menuAyuda=tk.Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)
menuAyuda.add_command(label="Acerca de", command=lambda:messagebox.showinfo("Version 1.0 - Sistema Biomedicina"))
 
ventanaPrincipal.mainloop()