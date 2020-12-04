class Galletas:
    chocolate=False
    sabor=None
    color=None
    forma="Cuadrado"

    def __init__(self,sabor,color):
        self.sabor=sabor
        self.color=color
        
        if sabor is not None and color is not None:
            print(f"se creo una Galleta sabor {sabor} y color {color}")            

    def chocolatear(self):
        self.chocolate=True
    
    def tieneChocolate(self):
        if self.chocolate:
            print(f"Galleta con chocolate")
        else:
            print(f"Galleta sin chocolate")

g=Galletas("Naranja","DDL")
print(g.color)
print(g.sabor)
print(g.chocolate)
g.chocolatear()
print(g.chocolate)
g.tieneChocolate()