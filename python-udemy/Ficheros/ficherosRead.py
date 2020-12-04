from io import open

fichero=open("ficheros/fichero.txt","r")

texto=fichero.read()

print(texto)

fichero.close()