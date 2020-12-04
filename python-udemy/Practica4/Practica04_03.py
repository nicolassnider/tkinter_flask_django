'''
Ejercicio 3
Realiza una función llamada intermedio(a, b) que a partir de dos números, devuelva su punto intermedio. Cuando lo tengas comprueba 
el punto intermedio entre dos valores que tenga que ingresar por teclado:
Recordatorio
El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2
'''

def promedio(a,b):
    
    return (a+b)/2

a=float(input("NumA:\n"))
b=float(input("NumB:\n"))

print(promedio(a,b))

    