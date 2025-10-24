nota = float(input("Ingrese la nota: "))
if nota == 10: 
    print("E")
elif nota > 7:
    print("MB")
else:
    if nota > 5:
        print("B")
    else: 
        if nota > 3: 
            print("R")
        else:
            print("M")