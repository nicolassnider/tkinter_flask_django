'''
Problema 05: Hallar la radicación de , donde a y n pertenecen
a números enteros positivos.
Análisis: Para la solución de este problema, se requiere que
usuario ingrese el valor de a y n por teclado y el sistema
realice el cálculo respectivo y obtenga la radicación r.
Expresión Algorítmica
r = a ^ (1/n)
'''

valor=int(input("base:\n"))
raiz=float(input("raiz:\n"))

radicacion= (valor ** (1/raiz))

print(f"Expresión Algorítmica: {valor}^(1/{raiz})")

print(f"radicacion = {radicacion}")
