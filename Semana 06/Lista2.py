nombres=["Ana","Antonio","Ana","Jose"]
print(nombres)
nombres[2] = "Pablo"
print(nombres)   #Para agregar tengo .append y agrega al final y .insert i, en la posición donde me digan.
nombres.append(input("Ingrese el nuevo nombre: "))
print(nombres)
nombres.insert(int(input("Indique el indice: ")), "Sebas")
print(nombres)
nombres.remove("Sebas")
print(nombres)