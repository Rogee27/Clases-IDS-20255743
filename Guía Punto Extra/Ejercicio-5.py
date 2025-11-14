N = int(input())
pa, pb, pc = map(int, input().split())
contador = 0
lcombos = []

while N > contador:
    lcombos.append(input())
    contador += 1
    
for i in lcombos:
   dA = i.count("A") * pa
   dB = i.count("B") * pb
   dC = i.count("C") * pc
   print(dA + dB + dC)