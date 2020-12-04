from tkinter import *
from tkinter import ttk
from conexion_db.cusultas_db import *


class Vista_carrera(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #Esta fucion abilita entrys 
        def nuevo_carrera():
            
            self.entry_nombre.config(state = "normal")
            self.entry_duracion.config(state = "normal")

        #Agrega datos a BD
        def agregar_datos():

            query = 'INSERT INTO carrera VALUES (NULL, ?, ?)'
            parametros = (self.entry_nombre.get(), self.entry_duracion.get())
            conn = Conectar_db()
            conn.run_db(query, parametros)

            #lIMPIAR CAPMPOS 
            self.entry_nombre.delete(0, END)
            self.entry_duracion.delete(0, END)
             
            #Actulizar Tabla 
            listar_datos()
            
        #Eliminar Datos 
        def eliminar_datos():

            codigo = self.tabla.item(self.tabla.selection())['text']
            query = 'DELETE FROM carrera WHERE codigo_c = ?'
            conn = Conectar_db()
            conn.run_db(query, (codigo,))

            #Actulizar Tabla 
            listar_datos()

        # Actualizar Datos 
        def actualizar_datos(codigo_n, codigo_a, nombre_nuevo, nombre_anti, duracion_nueva, duracion_ati):
            query = 'UPDATE carrera SET codigo_c = ?, nombre_c = ?, duracion_c =? WHERE codigo_c=? AND nombre_c=? AND duracion_c=?'
            parametros = (codigo_n, nombre_nuevo, duracion_nueva, codigo_a, nombre_anti, duracion_ati)

            conn = Conectar_db()
            conn.run_db(query, parametros)
            self.ventana_editar.destroy()

            #Actulizar Tabla 
            listar_datos()


        #Label titulo de registrar 
        self.label_titulo_registrar = Label(self, text= "Resgistrar Nueva Carrera ")
        self.label_titulo_registrar.grid(row = 0, column = 0, columnspan = 2, pady =10, padx = 10)

        #Label y Campo de Nombre 
        self.label_nombre = Label(self, text = "Nombre de Carrera: ")
        self.label_nombre.grid(row = 1, column = 0, pady = 10, padx = 10)
        self.entry_nombre = Entry(self, state = 'readonly')
        self.entry_nombre.grid(row = 1, column = 1,pady = 10, padx = 10)

        #Label y Campo de Duracion 
        self.label_duracion = Label(self, text = "Duracion de Carrera: ")
        self.label_duracion.grid(row = 2, column = 0,pady = 10, padx = 10)
        self.entry_duracion = Entry(self, state = 'readonly')
        self.entry_duracion.grid(row = 2, column = 1, pady = 10, padx = 10)

        #Boton Nunevo 
        self.boton_nuevo = Button(self, text = "REGISTRAR NUEVA CARRERA", command = nuevo_carrera)
        self.boton_nuevo.grid(row = 3, column = 0,pady = 10, padx = 10)

        #Boton Guardar
        self.boton_guardar = Button(self, text = "GUARDAR CARRERA", command = agregar_datos)
        self.boton_guardar.grid(row = 3, column = 1,pady = 10, padx = 10)

        #Label titulo de registrar 
        self.label_titulo_lista = Label(self, text= "Lista de Carreras ")
        self.label_titulo_lista.grid(row = 4, column = 0, columnspan = 2, pady =10, padx = 10)

        #Tabla 
        self.tabla = ttk.Treeview(self, columns=('',''))
        self.tabla.grid(row = 5, column = 0, columnspan = 3,pady = 10, padx = 10)
        self.tabla.heading('#0', text = "CODIGO DE CARRERA")
        self.tabla.heading('#1', text = "NOMBRE DE CARRERA")
        self.tabla.heading('#2', text = "DRURACION DE CARRERA")

        #Boton Eliminar
        self.boton_eliminar = Button(self, text = "ELIMINAR CARRERA", command = eliminar_datos)
        self.boton_eliminar.grid(row = 6, column = 0,pady = 10, padx = 10)

        #Editar Datos 
        def editar_datos():
            
            codigo = self.tabla.item(self.tabla.selection())['text']
            nombre_anti = self.tabla.item(self.tabla.selection())['values'][0]
            duracion_ati = self.tabla.item(self.tabla.selection())['values'][1]

            #Aranque de Ventana Editar
            self.ventana_editar = Toplevel()
            self.ventana_editar.title("Editar Carrera")

            #Label y Campo de Nombre 
            self.label_codigo = Label(self.ventana_editar, text = "Codigo de Carrera: ")
            self.label_codigo.grid(row = 0, column = 0, pady = 10, padx = 10)
            self.entry_codigo = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = codigo), state = 'readonly')
            self.entry_codigo.grid(row = 0, column = 1,pady = 10, padx = 10)

            #Label y Campo de Nombre Antiguo 
            self.label_nombre_antiguo = Label(self.ventana_editar, text = "Nombre de Carrera Antigua: ")
            self.label_nombre_antiguo.grid(row = 1, column = 0, pady = 10, padx = 10)
            self.entry_nombre_antiguo = Entry(self.ventana_editar,  textvariable = StringVar(self.ventana_editar, value = nombre_anti),state = 'readonly')
            self.entry_nombre_antiguo.grid(row = 1, column = 1,pady = 10, padx = 10)

            #Label y Campo de Nombre Nuevo 
            self.label_nombre_nuevo = Label(self.ventana_editar, text = "Nombre de Carrera Nueva: ")
            self.label_nombre_nuevo.grid(row = 2, column = 0, pady = 10, padx = 10)
            self.entry_nombre_nuevo = Entry(self.ventana_editar)
            self.entry_nombre_nuevo.grid(row = 2, column = 1,pady = 10, padx = 10)

            #Label y Campo de Duracion antigua
            self.label_duracion_antigua = Label(self.ventana_editar, text = "Duracion de Carrera Antigua: ")
            self.label_duracion_antigua.grid(row = 3, column = 0,pady = 10, padx = 10)
            self.entry_duracion_antigua = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = duracion_ati), state = 'readonly')
            self.entry_duracion_antigua.grid(row = 3, column = 1, pady = 10, padx = 10)

            #Label y Campo de Duracion Nuenvo
            self.label_duracion_nuevo = Label(self.ventana_editar, text = "Duracion de Carrera Nueva: ")
            self.label_duracion_nuevo.grid(row = 4, column = 0,pady = 10, padx = 10)
            self.entry_duracion_nuevo = Entry(self.ventana_editar)
            self.entry_duracion_nuevo.grid(row = 4, column = 1, pady = 10, padx = 10)

            #Boton Actualizar 
            self.boton_actualizar = Button(self.ventana_editar, text = "ACTUALIZAR CARRERA", command = lambda: actualizar_datos(codigo, codigo,
            self.entry_nombre_nuevo.get(),nombre_anti, self.entry_duracion_nuevo.get(), duracion_ati))
            self.boton_actualizar.grid(row = 5, column = 0, columnspan = 2,pady = 10, padx = 10)
            

        #Boton Editar
        self.boton_editar = Button(self, text = "EDITAR CARRERA", command = editar_datos)
        self.boton_editar.grid(row = 6, column = 1,pady = 10, padx = 10)

        #Listar Datos 
        def listar_datos():
            #Eliminar datos de la tabla
            recorrer_tabla = self.tabla.get_children()
            for elementos in recorrer_tabla:
                self.tabla.delete(elementos)
            
            #Ejecutar la consulta y cargar datos a la tabla
            query = 'SELECT * FROM carrera'
            conn = Conectar_db()
            datos = conn.run_db(query)
            #Cargar datos a la tabla
            for carrera in datos:
                self.tabla.insert('',0, text =carrera[0], value=(carrera[1],carrera[2]))

        #Ejecuta la funcion Listar datos 
        listar_datos()
       
