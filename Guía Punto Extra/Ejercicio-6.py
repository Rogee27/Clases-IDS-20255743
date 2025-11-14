N = int(input())

nombres = []
contador = 0

while N > contador:
    nombres.append(input())
    contador += 1

for i in nombres:
    if len(i) <= 6:
        print("No vale la pena")
    elif len(i) >= 8:
        print("Si aguanto otro desarrollo de personaje")
    elif len(i) > 6 and len(i) < 8:
        print("Dios no creo aguantar esta vez")