#sistema de gestión de alumnos 

menu_iniciado = True
alumnos = []

while menu_iniciado:
    opcion = int(input("1.Agregar, 2.Consultar, 3,Modificar, 4.Borrar, 5.Salir"))
    if opcion == 5: 
        menu_iniciado = False 
    elif opcion == 1:
        alumnos.append(input("Digite el nombre del alumno: "))
    elif opcion == 2:
        for a in alumnos:
            print(a)
    elif opcion == 3:
        indice = int(input("Digite el número de alumno (1-3): "))
        nuevo = input("Digite el nombre nuevo: ")
        alumnos[indice-1] = nuevo
    elif opcion == 4:
        indice = int(input("Digite el número del alumno (1-3) a borrar: "))
        alumno_borrado = alumnos.pop(indice-1)
        print(f"Hemos borrado a : {alumno_borrado}")


print("Gracias por usar nuestro sistema.")