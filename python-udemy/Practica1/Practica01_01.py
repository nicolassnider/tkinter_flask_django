'''
Problema 01: Dado dos números, hallar las suma, resta, división
y multiplicación.
Análisis: Para la solución de este problema, se requiere que
ingrese dos números por teclado y el sistema realice el cálculo
respectivo para hallar la suma, resta, división y
multiplicación.
'''
num1=float(input("num1:\n"))
num2=float(input("num2:\n"))


suma=num1+num2
resta=num1-num2
division=num1/num2
multiplicacion=num1*num2

print(f"suma = {suma}")
print(f"resta = {resta}")
print(f"division = {division}")
print(f"multiplicacion = {multiplicacion}")