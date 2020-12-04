'''
Problema 02: Determinar si un número es positivo, negativo o neutro.
Análisis: Para la solución de este problema, se requiere que ingrese un número entero por teclado y el sistema verifique si es positivo, neutro o negativo.
'''

num = int(input("numero: \n"))

if num > 0:
    print(f"{num} es positivo")
elif num < 0:
    print(f"{num} es negativo")
elif num == 0:
    print(f"{num} es Neutro")

