'''
1. Crear una clase Rectángulo, con atributos base y altura. Crear también el constructor de la clase y los métodos necesarios para calcular el área y el perímetro. 
Crear otra clase PruebaRectangulo que pruebe varios rectángulos y muestre por pantalla sus áreas y perímetros.
'''
class Rectangulo():
    b=0
    h=0

    def __init__(self,b,h):
        super().__init__()
        self.b=float(b)
        self.h=float(h)
    
    def area(self):
        return self.b*self.h
    
    def perimetro(self):
        return ((self.b*2)+(self.h*2))

    def mostrarDatos(self):
        return (f"El rectángulo posee un perímetro p={self.perimetro()} unidades y un area a={self.area()} unidades cuadradas")


class TestRectangulos(object):

    def __init__(self, *args):
        super(TestRectangulos, self).__init__(*args)
        self.r1=Rectangulo(1,2)
        self.r2=Rectangulo(2,3)
        self.r3=Rectangulo(3,4)
        self.r4=Rectangulo(5,5.78)

    def testRectangulos(self):
        print(self.r1.mostrarDatos())
        print(self.r2.mostrarDatos())
        print(self.r3.mostrarDatos())
        print(self.r4.mostrarDatos())
        
tr=TestRectangulos()
tr.testRectangulos()

     
        

    
    
    

    
