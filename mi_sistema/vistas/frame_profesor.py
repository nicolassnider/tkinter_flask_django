from tkinter import *
from tkinter import ttk


class Vista_profesor(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Editar Campo de Textos 
        def nuevo():
            self.entry_nombre.config(state = "normal")
            self.entry_telefono.config(state = "normal")
            self.entry_direccion.config(state = "normal")

        #Label de titulo de registrar  
        self.label_titulo_registrar = Label(self, text= "Resgistrar Nuevo Profesor ")
        self.label_titulo_registrar.grid(row = 0, column = 0, columnspan = 2, pady = 10, padx = 10)

        #Label y campo de nombre 
        self.label_nombre = Label(self, text = "Nombre de Profesor: ")
        self.label_nombre.grid(row = 1, column = 0, pady = 10, padx = 10)
        self.entry_nombre = Entry(self, state = 'readonly')
        self.entry_nombre.grid(row = 1, column = 1,pady = 10, padx = 10)

        #Label y campo de Telefono 
        self.label_telefono = Label(self, text = "Telefono de Profesor: ")
        self.label_telefono.grid(row = 2, column = 0,pady = 10, padx = 10)
        self.entry_telefono = Entry(self, state = 'readonly')
        self.entry_telefono.grid(row = 2, column = 1, pady = 10, padx = 10)

        #Label y campo de Direccion 
        self.label_direccion = Label(self, text = "Direccion de Profesor: ")
        self.label_direccion.grid(row = 3, column = 0,pady = 10, padx = 10)
        self.entry_direccion = Entry(self, state = 'readonly')
        self.entry_direccion.grid(row = 3, column = 1, pady = 10, padx = 10)

        #Boton Nunevo 
        self.boton_nuevo = Button(self, text = "REGISTRAR NUEVO PROFESOR", command = nuevo)
        self.boton_nuevo.grid(row = 4, column = 0,pady = 10, padx = 10)

        #Boton Guardar
        self.boton_guardar = Button(self, text = "GUARDAR PROFESOR")
        self.boton_guardar.grid(row = 4, column = 1,pady = 10, padx = 10)

        #Label de titulo de listar  
        self.label_titulo_listar = Label(self, text= "Lista de Profesores  ")
        self.label_titulo_listar.grid(row = 5, column = 0, columnspan = 2, pady = 10, padx = 10)

        #Crear tabla  
        self.tabla = ttk.Treeview(self, columns=('','',''))
        self.tabla.grid(row = 6, column = 0, columnspan = 3,pady = 10, padx = 10)
        self.tabla.heading('#0', text = "CODIGO DE PROFESOR")
        self.tabla.heading('#1', text = "NOMBRE DE PROFESOR")
        self.tabla.heading('#2', text = "TELEFONO DE PROFESOR")
        self.tabla.heading('#3', text = "DIRECCION DE PROFESOR")

        #Boton de Editar 
        self.boton_editar = Button(self, text = "EDITAR PROFESOR")
        self.boton_editar.grid(row = 7, column = 0, pady = 10, padx = 10)

        #Boton Eliminar
        self.boton_eliminar = Button(self, text = "ELIMINAR PROFESOR")
        self.boton_eliminar.grid(row = 7, column = 1, pady = 10, padx = 10 )