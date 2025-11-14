"""usuarios = ["Ana", "Carlos", "Luis", "María", "Lorenzo"]

for posicion, usuario in enumerate(usuarios,start=1): #Los enumera
    print(f"{posicion} {usuario}")"""
  
usuarios = ["Ana", "Carlos", "Luis", "María", "Lorenzo"]
edades = [20, 19, 21, 22, 18]
frutas =["mango", "fresa", "pera", "sandia", "pina"]
for usuario, edad, frutas in zip(usuarios, edades, frutas): #Los enumera
    print(f"El {usuario}, con {edad}, le gusta {frutas}.")