'''
. Problema 03: Dado el valor de venta de un producto, hallar el
IGV (18%) y el precio de venta.
Análisis: Para la solución de este problema, se requiere que
usuario ingrese el valor de venta del producto por teclado y el
sistema realice el cálculo respectivo para hallar el IGV y el
precio de venta.
'''
valor=float(input("valor:\n"))
igv= 0.18
print(f"IGV={valor+igv*valor}({igv*100}%)")
