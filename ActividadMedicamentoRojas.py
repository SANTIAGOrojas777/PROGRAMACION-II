import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# -------------------------
# FUNCIONES DEL SISTEMA
# -------------------------

#FUNCION PARA ENMASCARAR FECHA
def formato_fecha_keyrelease(event):
    s = entry_fecha_var.get()
    # conservar solo dígitos y limitar a 8 (DDMMYYYY)
    digits = ''.join(ch for ch in s if ch.isdigit())[:8]

    if len(digits) > 4:
        formatted = f"{digits[:2]}-{digits[2:4]}-{digits[4:]}"
    elif len(digits) > 2:
        formatted = f"{digits[:2]}-{digits[2:]}"
    else:
        formatted = digits

    if formatted != s:
        entry_fecha_var.set(formatted)

    entry_fecha.icursor(tk.END)

#FUNCION PARA GUARDAR EL REGISTRO
def guardar_en_archivo():
    with open("medicamento.txt", "w", encoding="utf-8") as archivo:
        for gestion in gestiones_data:
            archivo.write(f"""{gestion["Nombre"]}|{gestion["Presentacion"]}|{gestion["Dosis"]}|{gestion["Fecha de vencimiento"]}\n""")
        
#FUNCION PARA CARGAR DESDE EL ARCHIVO
def cargar_desde_archivo_medicamento():
    try:
        with open("medicamento.txt", "r", encoding="utf-8") as archivo:
            gestiones_data.clear()
            for linea in archivo:
                datos=linea.strip().split("|")
                if len(datos)==4:
                    gestion={
                        "Nombre":datos[0],
                        "Presentacion":datos[1],
                        "Dosis":datos[2],
                        "Fecha de vencimiento":datos[3]
                    }
                    gestiones_data.append(gestion)
        cargar_treeview()
    except FileNotFoundError:
        open("medicamento.txt", "w", encoding="utf-8").close()

#FUNCION PARA ELIMINAR EL REGISTRO
def eliminar_registro():
    seleccionado=treeview.selection()
    if seleccionado:
        indice=int(seleccionado[0])
        id_item=seleccionado[0]
        if messagebox.askyesno("Eliminar registro", f"¿Estas seguro de eliminar la gestión '{treeview.item(id_item, 'values')[0]}'?"):
            del gestiones_data[indice]
            guardar_en_archivo()
            cargar_treeview()
            messagebox.showinfo("Eliminar registro", "Gestión eliminada exitosamente")
    else:
        messagebox.showwarning("Eliminar registro", "No se ha seleccionado ningun medicamento")
        return

""" LISTA DE GESTIONES """
gestiones_data=[]

#FUNCION PARA REGISTRAR LA GESTION DE MEDICAMENTOS
def registroGestion():
    gestion={
        "Nombre":entry_nombre.get(),
        "Presentacion":combo_presentacion.get(),
        "Dosis":entry_dosis.get(),
        "Fecha de vencimiento":entry_fecha_var.get()
    }
    #AGREGAR GESTION A LA LISTA
    gestiones_data.append(gestion)
    #LLAMANDO A LA FUNCION PARA GUARDAR EN ARCHIVO
    guardar_en_archivo()
    #CARGAR EL TREEVIEW
    cargar_treeview()
    
#FUNCION PARA CARGAR TREEVIEW
def cargar_treeview():
    #LIMPIAR EL TREEVIEW
    for gestion in treeview.get_children():
        treeview.delete(gestion)
    #INSERTAR GESTION
    for i, item in enumerate(gestiones_data):
        treeview.insert(
            "", "end", iid=str(i),
            values=(
                item["Nombre"],
                item["Presentacion"],
                item["Dosis"],
                item["Fecha de vencimiento"]
            )
        )

# -------------------------
# INTEFAZ GRAFICA
# -------------------------

#CREACION DE LA VENTANA
ventana = tk.Tk()
ventana.title("Gestión de Medicamentos")
ventana.geometry("800x520")
ventana.minsize(700, 450)

#FRAME DEL FORMULARIO
form_frame = ttk.Frame(ventana, padding=(12, 10))
form_frame.grid(row=0, column=0, sticky="ew")
form_frame.columnconfigure(0, weight=0)
form_frame.columnconfigure(1, weight=1)

#NOMBRE
lbl_nombre = ttk.Label(form_frame, text="Nombre:")
lbl_nombre.grid(row=0, column=0, sticky="w", padx=6, pady=6)
entry_nombre = ttk.Entry(form_frame)
entry_nombre.grid(row=0, column=1, sticky="ew", padx=6, pady=6)

#PRESENTACION
lbl_present = ttk.Label(form_frame, text="Presentación:")
lbl_present.grid(row=1, column=0, sticky="w", padx=6, pady=6)
combo_presentacion = ttk.Combobox(form_frame, values=["Tabletas", "Jarabe", "Inyectable", "Cápsulas", "Otro"], state="readonly")
combo_presentacion.grid(row=1, column=1, sticky="ew", padx=6, pady=6)

#DOSIS
lbl_dosis = ttk.Label(form_frame, text="Dosis:")
lbl_dosis.grid(row=2, column=0, sticky="w", padx=6, pady=6)
entry_dosis = ttk.Entry(form_frame)
entry_dosis.grid(row=2, column=1, sticky="w", padx=6, pady=6)

#FECHA VENCIMIENTO CON ENMASCARADO
lbl_fecha = ttk.Label(form_frame, text="Fecha Vencimiento (dd-mm-yyyy):")
lbl_fecha.grid(row=3, column=0, sticky="w", padx=6, pady=6)
entry_fecha_var = tk.StringVar()
entry_fecha = ttk.Entry(form_frame, textvariable=entry_fecha_var)
entry_fecha.grid(row=3, column=1, sticky="w", padx=6, pady=6)
entry_fecha.bind("<KeyRelease>", formato_fecha_keyrelease)

#BOTONES
btn_frame = ttk.Frame(form_frame)
btn_frame.grid(row=5, column=1, columnspan=2, sticky="ew", padx=6, pady=(10, 2))
btn_frame.columnconfigure((0, 1, 2, 3), weight=1)  # columnas equitativas

btn_registrar = ttk.Button(btn_frame, text="Registrar", command=lambda:registroGestion())
btn_registrar.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

btn_eliminar = ttk.Button(btn_frame, text="Eliminar", command=lambda:eliminar_registro())
btn_eliminar.grid(row=0, column=1, padx=5, pady=5, sticky="ew")


#FRAME LISTA
list_frame = ttk.Frame(ventana, padding=(12, 6))
list_frame.grid(row=1, column=0, sticky="nsew")
ventana.rowconfigure(1, weight=1)
ventana.columnconfigure(0, weight=1)
list_frame.rowconfigure(0, weight=1)
list_frame.columnconfigure(0, weight=1)

treeview = ttk.Treeview(list_frame, columns=("nombre", "presentacion", "dosis", "fecha"), show="headings")
treeview.grid(row=4, column=0, sticky="nsew")
treeview.heading("nombre", text="Nombre")
treeview.heading("presentacion", text="Presentación")
treeview.heading("dosis", text="Dosis")
treeview.heading("fecha", text="Fecha Vencimiento")

treeview.column("nombre", width=220)
treeview.column("presentacion", width=120, anchor="center")
treeview.column("dosis", width=100, anchor="center")
treeview.column("fecha", width=120, anchor="center")

scroll_y = ttk.Scrollbar(list_frame, orient="vertical", command=treeview.yview)
scroll_y.grid(row=4, column=1, sticky="ns")
treeview.configure(yscrollcommand=scroll_y.set)

#CARGAR DATOS DESDE EL ARCHIVO
cargar_desde_archivo_medicamento()

#EJECUTAR
ventana.mainloop()