'''
Ejercicio 4
Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica 
en un mensaje al usuario la causa y/o solución:
resultado = 15 + "20"
'''
try:
    print(15+"20")
except TypeError:
    print("Error de tipo")