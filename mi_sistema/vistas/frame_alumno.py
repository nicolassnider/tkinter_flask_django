from tkinter import *
from tkinter import ttk
from conexion_db.cusultas_db import *

class Vista_alumno(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Editar Campo de Textos 
        def nuevo():
            self.entry_nombre.config(state = "normal")
            self.entry_edad.config(state = "normal")
            self.entry_telefono.config(state = "normal")
        
        #Agrega datos a BD
        def agregar_datos():
            
            carrera = self.carre_combo.get()
            carrera = carrera[0]+carrera[1]
            print(carrera)

            query = 'INSERT INTO alumno VALUES (NULL, ?, ?, ?, ?)'
            parametros = (self.entry_nombre.get(), self.entry_edad.get(), self.entry_telefono.get(),carrera)
            conn = Conectar_db()
            conn.run_db(query, parametros)

            #lIMPIAR CAPMPOS 
            self.entry_nombre.delete(0, END)
            self.entry_edad.delete(0, END)
            self.entry_telefono.delete(0, END)
             
            #Actulizar Tabla 
            listar_datos()

        #Label de titulo de registrar  
        self.label_titulo_registrar = Label(self, text= "Resgistrar Nuevo Alumno ")
        self.label_titulo_registrar.grid(row = 0, column = 0, columnspan = 2, pady = 10, padx = 10)

        #Label y campo de nombre 
        self.label_nombre = Label(self, text = "Nombre del Alumno: ")
        self.label_nombre.grid(row = 1, column = 0, pady = 10, padx = 10)
        self.entry_nombre = Entry(self, state = 'readonly')
        self.entry_nombre.grid(row = 1, column = 1,pady = 10, padx = 10)

        #Label y campo de Edad 
        self.label_edad = Label(self, text = "Edad del Alumno: ")
        self.label_edad.grid(row = 2, column = 0,pady = 10, padx = 10)
        self.entry_edad = Entry(self, state = 'readonly')
        self.entry_edad.grid(row = 2, column = 1, pady = 10, padx = 10)

        #Label y campo de Telefono 
        self.label_telefono = Label(self, text = "Telefono del Alumno: ")
        self.label_telefono.grid(row = 3, column = 0,pady = 10, padx = 10)
        self.entry_telefono = Entry(self, state = 'readonly')
        self.entry_telefono.grid(row = 3, column = 1, pady = 10, padx = 10)

        
        #Como Box de Carreras 
        self.label = Label(self, text = "Escojer Carreras: ").grid(row = 1, column = 2, pady = 10, padx = 10)
        self.carre_combo = ttk.Combobox(self)
        self.carre_combo.grid(row = 1, column = 3, pady = 10, padx = 10)

        #Cargar Datos al combobox de Carreras
        def cargar_combo():
            query = 'SELECT codigo_c, nombre_c FROM carrera'
            conn = Conectar_db()
            datos_c = conn.run_db(query)

            for carrera in datos_c:
                values = list(self.carre_combo["values"])
                self.carre_combo["values"] = values + [(carrera[0],',',carrera[1])]

                      
        #Ejecutar Funcion
        cargar_combo()

        #Boton Nunevo 
        self.boton_nuevo = Button(self, text = "REGISTRAR NUEVO ALUMNO", command = nuevo)
        self.boton_nuevo.grid(row = 4, column = 0,pady = 10, padx = 10)

        #Boton Guardar
        self.boton_guardar = Button(self, text = "GUARDAR ALUMNO", command = agregar_datos)
        self.boton_guardar.grid(row = 4, column = 1,pady = 10, padx = 10)

        #Label de titulo de listar  
        self.label_titulo_listar = Label(self, text= "Lista de Alumnos  ")
        self.label_titulo_listar.grid(row = 5, column = 0, columnspan = 2, pady = 10, padx = 10)

        #Crear tabla  
        self.tabla = ttk.Treeview(self, columns=('','','',''))
        self.tabla.grid(row = 6, column = 0, columnspan = 3,pady = 10, padx = 10)
        self.tabla.heading('#0', text = "CODIGO DEL ALUMNO")
        self.tabla.heading('#1', text = "NOMBRE DEL ALUMNO")
        self.tabla.heading('#2', text = "EDAD DEL ALUMNO")
        self.tabla.heading('#3', text = "TELEFONO DEL ALUMNO")
        self.tabla.heading('#4', text = "CARRERA")

        #Boton de Editar 
        self.boton_editar = Button(self, text = "EDITAR ALUMNO")
        self.boton_editar.grid(row = 7, column = 0, pady = 10, padx = 10)

        #Boton Eliminar
        self.boton_eliminar = Button(self, text = "ELIMINAR ALUMNO")
        self.boton_eliminar.grid(row = 7, column = 1, pady = 10, padx = 10 )

        #Listar Datos 
        def listar_datos():
            #Eliminar datos de la tabla
            alumno_tabla = self.tabla.get_children()
            for elementos in alumno_tabla:
                self.tabla.delete(elementos)
            
            #Ejecutar la consulta y cargar datos a la tabla
            query = '''SELECT codigo_a, nombre_a, edad_a, telefono_a, nombre_c FROM alumno
                    INNER JOIN carrera ON alumno.codigo_c1 = carrera.codigo_c '''
                    
            conn = Conectar_db()
            datos = conn.run_db(query)
            #Cargar datos a la tabla
            for alumno in datos:
                self.tabla.insert('',0, text =alumno[0], value=(alumno[1],alumno[2],alumno[3],alumno[4]))
                

        #Ejecuta la funcion Listar datos 
        listar_datos()

        