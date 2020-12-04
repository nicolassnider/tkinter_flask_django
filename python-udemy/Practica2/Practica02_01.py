'''
Problema 01: Dado dos números diferentes, devolver el número mayor.
Análisis: Para la solución de este problema, se requiere que ingrese dos números por teclado y el sistema realice el proceso de devolver el número mayor.
'''
num1 = int(input("num1:\n"))
num2 = int(input("num2:\n"))

if num1 > num2:
    print(f"{num1} es mayor")
elif num2 > num1:
    print(f"{num2} es mayor")
elif num1==num2:
    print(f"son iguales")
