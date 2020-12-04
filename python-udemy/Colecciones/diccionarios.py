colores={"amarillo":"yellow", "azul":"blue", "verde":"green"}


print(colores.get("azul","no se encuentra"))
print(colores.values())
print(colores.keys())

print(colores.items())

for clave, valor in colores.items():
    print(clave,valor)

print(colores.pop("amarillo","no se encuentra"))
print(colores)
colores.clear()
print(colores)

