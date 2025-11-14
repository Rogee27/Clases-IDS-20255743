nombres = ["Ana", "Sebas", "Mario", "Carla"]
nombre_buscar = input("Nombre a buscar: ")
for n in nombres: 
    if n == nombre_buscar:
        print("Ya lo encontre")
    else:
        print("Aquí no está")