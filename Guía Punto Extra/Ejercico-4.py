N = int(input())
lista = []
contador = 0
c7 = 0
c5 = 0

while N > contador:
    lista.append(int(input()))
    contador+=1
for i in lista: 
    if i == 7: 
        c7+=1
    if i == 5:
        c5+=1

print(c7, c5)