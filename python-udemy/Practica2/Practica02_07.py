'''
Problema 07: Dado un número entero, devolver el doble si el número es par, caso contrario el triple.
Análisis: Para la solución de este problema, se requiere que usuario ingrese un número entero n y luego el sistema verifique y devuelva el doble o el tiple del número.
'''

valor=int(input("base:\n"))
if valor%2==0:
    print(f"{valor} es par, el doble es {valor * 2}") 
else:
    print(f"{valor} es impar, el triple es {valor * 3}") 