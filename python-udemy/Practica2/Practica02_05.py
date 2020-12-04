'''
Problema 05: determine si un nuero entero es par o impar.
Análisis: Para la solución de este problema, se requiere que usuario ingrese un número entero n, y luego el sistema verifique si el número es par o impar.
'''
valor1=int(input("valor1:\n"))
valor2=int(input("valor2:\n"))
valor3=int(input("valor3:\n"))

if valor1>valor2:
    if valor1>valor3:
        print(f"{valor1} es el mayor") 
    else:
        print(f"{valor3} es el mayor") 
else:
    if valor2>valor3:
        print(f"{valor2} es el mayor") 
    else:
        print(f"{valor3} es el mayor")
    
