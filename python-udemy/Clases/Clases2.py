class Pelicula(object):
    def __init__(self,titulo,duracion,year):
        super().__init__()
        self.titulo=titulo
        self.duracion=duracion
        self.year=year
        
        print(f"se creó pelicula {self.titulo}, dura {self.duracion}. año {self.year}")

    def __del__(self):
        print(f"se elimino pelicula")

    def __str__(self):
        return f"{self.titulo} {self.duracion} {self.year}"

    #metodo privado y attr privado
    def __metodoPrivado(self):
        print("metodo privado")
    __attr_privado="Attr Privado"


class Catalogo(object):

    peliculas=[]
    def __init__(self,peliculas=[]):
        super().__init__()
        self.peliculas=peliculas

    def mostrar(self):
        for p in self.peliculas:
            print (p)
    
    def add(self,p):
        self.peliculas.append(p)

p= Pelicula("Padrino",160,1980)

c=Catalogo()

c.add(p)

c.mostrar()