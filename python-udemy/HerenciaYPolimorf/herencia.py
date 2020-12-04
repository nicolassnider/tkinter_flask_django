class Producto:
    def __init__(self,codigo,nombre,precio,descripcion):
        super().__init__()
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.descripcion=descripcion

    def __str__(self):

        return f"{self.codigo}||{self.nombre} \t${self.precio} \t{self.descripcion}"

class Adorno(Producto):
    pass

class Alimento(Producto):
    productor=""
    distribuidor=""

    def __str__(self):
    
        return f"{self.codigo}||{self.nombre} \t${self.precio} \t{self.descripcion} \t{self.productor} \t{self.distribuidor}"

class Libro(Producto):
    isbn=""
    autor=""

    def __str__(self):
    
        return f"{self.codigo}||{self.nombre} \t${self.precio} \t{self.descripcion} \t{self.isbn} \t{self.autor}"


adorno=Adorno(2034,"Vaso azul",500,"vaso color azul 100ml")
print(adorno)

alimento=Alimento(2035,"Harina 1kg",20,"paquete harina 1kg")
alimento.productor="Productor Harina"
alimento.distribuidor="Distribuidor de harina"
print(alimento)

libro=Libro(2036,"Historia del tiempo",200,"breve historia del tiempo")
libro.isbn="9781234567897"
libro.autor="Hawkins"
print(libro)

productos=[alimento,libro,adorno]

for producto in productos:
    if (isinstance(producto,Adorno)):
        print(producto.codigo,producto.nombre)
    elif (isinstance(producto,Libro)):
        print(producto.codigo,producto.nombre,producto.autor)
    elif (isinstance(producto,Alimento)):
        print(producto.codigo,producto.nombre,producto.distribuidor)