'''
2. Crear una clase Coche, a través de la cual se pueda conocer el color del coche, la marca, el modelo, el número de caballos, el número de puertas y la matricula. 
Crear el constructor del coche, así como los métodos que considere necesarios. Crear una clase PruebaCoche que instancie varios coches, cambiándole el color a lo largo 
de la vida a algunos de ellos y mostrándolo por pantalla.
'''
class Coche(object):

    color=""
    marca=""
    modelo=""
    hp=""
    puertas=""
    patente=""


    def __init__(self, color,marca,modelo,hp,puertas,patente):
        super(Coche, self).__init__()
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.hp=hp
        self.puertas=puertas
        self.patente=patente
    
    
        