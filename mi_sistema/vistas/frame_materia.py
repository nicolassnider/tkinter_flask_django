from tkinter import *
from tkinter import ttk


class Vista_materia(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Editar Campo de Textos 
        def nuevo():
            self.entry_nombre.config(state = "normal")
            self.entry_creditos.config(state = "normal")

        #Label de titulo de registrar  
        self.label_titulo = Label(self, text= "Resgistrar Nueva Materia ")
        self.label_titulo.grid(row = 0, column = 0, columnspan = 2, pady = 10, padx = 10)

        #Label y campo de nombre 
        self.label_nombre = Label(self, text = "Nombre de Materia: ")
        self.label_nombre.grid(row = 1, column = 0, pady = 10, padx = 10)
        self.entry_nombre = Entry(self, state = 'readonly')
        self.entry_nombre.grid(row = 1, column = 1,pady = 10, padx = 10)

        #Labol y campo de Creditos 
        self.label_creditos = Label(self, text = "Credito de Materia: ")
        self.label_creditos.grid(row = 2, column = 0,pady = 10, padx = 10)
        self.entry_creditos = Entry(self, state = 'readonly')
        self.entry_creditos.grid(row = 2, column = 1, pady = 10, padx = 10)

        #Boton Nunevo 
        self.boton_nuevo = Button(self, text = "REGISTRAR NUEVA MATERIA", command = nuevo)
        self.boton_nuevo.grid(row = 3, column = 0,pady = 10, padx = 10)

        #Boton Guardar
        self.boton_guardar = Button(self, text = "GUARDAR MATERIA")
        self.boton_guardar.grid(row = 3, column = 1,pady = 10, padx = 10)

        #Label de titulo de listar  
        self.label_titulo = Label(self, text= "Lista de Materias  ")
        self.label_titulo.grid(row = 4, column = 0, columnspan = 2, pady = 10, padx = 10)

        #Crear tabla  
        self.tabla = ttk.Treeview(self, columns=('',''))
        self.tabla.grid(row = 5, column = 0, columnspan = 3,pady = 10, padx = 10)
        self.tabla.heading('#0', text = "CODIGO DE MATERIA")
        self.tabla.heading('#1', text = "NOMBRE DE MATERIA")
        self.tabla.heading('#2', text = "DRURACION DE MATERIA")

        #Boton de Editar 
        self.boton_editar = Button(self, text = "EDITAR MATERIA")
        self.boton_editar.grid(row = 6, column = 0, pady = 10, padx = 10)

        #Boton Eliminar
        self.boton_eliminar = Button(self, text = "ELIMINAR MATERIA")
        self.boton_eliminar.grid(row = 6, column = 1, pady = 10, padx = 10 )