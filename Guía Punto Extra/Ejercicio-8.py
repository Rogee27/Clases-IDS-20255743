A = int(input())

contador = 0
ledades = []
personasAptas = 0

while A > contador:
    ledades.append(int(input()))
    contador += 1

for i in ledades:
    if i >= 15:
        personasAptas += 1

print(personasAptas)