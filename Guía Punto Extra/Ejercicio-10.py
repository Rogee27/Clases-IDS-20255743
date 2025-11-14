N = int(input())

contador = 0
listas_cantidad_distribuida = []

while N > contador:
    listas_cantidad_distribuida.append(int(input()))
    contador += 1

for i in listas_cantidad_distribuida:
    if i >= 3:
        print("Ok")
    else:
        print("No")