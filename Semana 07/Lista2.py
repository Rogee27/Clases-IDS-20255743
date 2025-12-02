nombres=["Ana","Antonio","Ana","Jose"]
print(nombres)
nombres[2] = "Pablo"
print(nombres)   #Para agregar tengo .append y agrega al final y .insert i, en la posición donde me digan.
nombres.append(input("Ingrese el nuevo nombre: "))
print(nombres)
nombres.insert(int(input("Indique el indice: ")), "Sebas")
print(nombres)
nombres.remove("Sebas")
#pop borra y lo guarda en un avariable el valor que acaba de borrar
print(nombres)
nombre_borrado = nombres.pop(int(input("Indique el indice: ")), input("Nombre: "))
"""nombrebb= nombres.pop(int(input())-1)
print(nombres)
print(nombrebb)"""
print(nombres)
nombres.remove("Sebas")
print(nombres)
nombres[1]