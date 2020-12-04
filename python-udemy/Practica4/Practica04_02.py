'''
Ejercicio 2
Realiza una función llamada relacion(a, b) que a partir de dos números cumpla lo siguiente:
 Si el primer número es mayor que el segundo, debe devolver 1.
 Si el primer número es menor que el segundo, debe devolver -1.
 Si ambos números son iguales, debe devolver un 0.
Los numero a y b tienes que ser ingresados por teclado
'''
def relacion(a,b):
    if a>b:
        return 1
    elif (a<b):
        return -1
    else: 
        return 0
a=float(input("NumA:\n"))
b=float(input("NumB:\n"))

print(relacion(a,b))