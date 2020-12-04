'''
Ejercicio 1
Realiza una función llamada area_rectangulo(base, altura) que devuelva el área del rectangulo a partir de una base y una altura. 
Calcula el área de un rectángulo: su base y altura ingrese por teclado.
Nota: El área de un rectángulo se obtiene al multiplicar la base por la altura.
'''

def areaRectangulo(base,altura):
    return base*altura

base=float(input("Base:\n"))
altura=float(input("Altura:\n"))
print(areaRectangulo(base,altura))
    