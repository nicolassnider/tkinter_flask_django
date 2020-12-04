'''
Problema 04: Determine si un número es múltiplo de 3 y 5.
Análisis: Para la solución de este problema, se requiere que usuario ingrese un número entero n, y luego el sistema analiza y determine si es el número de múltiplo de 3 y de 5.
'''
valor = int(input("Valor:\n"))
multiplo1=3
multiplo2=5

if valor%multiplo1==0:
    print (f"{valor} es multiplo de {multiplo1}")
if valor%multiplo2==0:
    print (f"{valor} es multiplo de {multiplo2}")
if(not valor%multiplo1==0 and not valor%multiplo2==0):
    print (f"{valor} no es multiplo de {multiplo1} ni {multiplo2}")
    
    