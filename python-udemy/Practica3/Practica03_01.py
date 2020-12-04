usuarios= {"Marta","David","Elvira","Juan","Marcos"}
administradores={"Juan","Marta"}

administradores.discard("Juan")
administradores.add("Marcos")

for usuario in usuarios:
    if usuario in administradores:
        print(f"{usuario}\t Admin")
    else:
        print(f"{usuario}\t User")