from io import open

texto="Linea y salto \n de linea"

fichero=open("ficheros/fichero.txt","w")

fichero.write(texto)

fichero.close()