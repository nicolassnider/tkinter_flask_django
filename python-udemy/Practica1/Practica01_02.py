'''
Problema 02: Hallar el cociente y residuo (resto) de dos números
enteros.
Análisis: Para la solución de este problema, se requiere que
ingrese dos números entero por teclado y el sistema realice el
cálculo respectivo para hallar el cociente y residuo.
'''
num1=float(input("num1:\n"))
num2=float(input("num2:\n"))

cociente=num1 // num2
residuo=num1 % num2


print(f"cociente = {cociente}")
print(f"residuo = {residuo}")
