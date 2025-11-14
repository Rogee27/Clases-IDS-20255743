"""valores = [[1, 3, 6],
           [2, 7, 4],
           [1, 10, 20]]"""
mayores= []
for v in valores:
    for valorcito in v:
        if valorcito > 6: 
            mayores.append(valorcito)
print(mayores)
