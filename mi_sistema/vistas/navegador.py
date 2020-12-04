from tkinter import *
from tkinter import ttk
from vistas.frame_carrera import *
from vistas.frame_materia import *
from vistas.frame_profesor import *
from vistas.frame_alumno import *


class Aplicaion(ttk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        self.mi_ventana = ventana
        self.mi_ventana.title("Sistema Universitario")
        self.mi_ventana.iconbitmap("img/uni.ico")

        #Contener de Paneles 
        self.navegador = ttk.Notebook(self)

        #Panel de Inicio
        self.inicio = Label(self.navegador, text = "Pagina de Inicio ")
        self.navegador.add(self.inicio, text = "Inicio ")

        #Pamel de Carrera 
        self.resg_carrera = Vista_carrera(self.navegador)
        self.navegador.add(self.resg_carrera, text = "Carrera ")

        #Pamel de Materia 
        self.panel_materia = Vista_materia(self.navegador)
        self.navegador.add(self.panel_materia, text = "Materia ")

        #Pamel de Profesor 
        self.panel_profe = Vista_profesor(self.navegador)
        self.navegador.add(self.panel_profe, text = "Profesor ")

        #Pamel de Alumno 
        self.panel_alumno = Vista_alumno(self.navegador)
        self.navegador.add(self.panel_alumno, text = "Alumno ")

        self.navegador.pack()
        self.pack()
