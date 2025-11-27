
def registrar_prestamo(lista_libros, lista_estudiantes, lista_prestamos):
    print("\n--- Registrar Préstamo ---")

    # Pedir el carnet del estudiante
    carnet = input("Ingrese el carnet del estudiante: ")

    # Verificar si el estudiante está registrado
    estudiante_encontrado = False
    for estudiante in lista_estudiantes:
        if estudiante["Carnet"] == carnet:
            estudiante_encontrado = True

    if estudiante_encontrado == False:
        print("Este estudiante no está registrado :(")

    # Pedir el código del libro
    codigo = input("Ingrese el código del libro: ")

    # Verificar si el libro existe y si está disponible
    libro_existe = False
    libro_disponible = False
    for libro in lista_libros:
        if libro["Código"] == codigo:
            libro_existe = True
            if libro["Disponible"] == True:
                libro_disponible = True
                # Pedir la fecha solo si el libro está disponible
                fecha_prestamo = input("Digite la fecha: ")

    # Mensajes si el libro no existe o no está disponible
    if libro_existe == False:
        print("Este libro no existe :(")
    if libro_existe and libro_disponible == False:
        print("Este libro no está disponible :(")

    # Registrar el préstamo solo si todo es correcto
    if estudiante_encontrado and libro_existe and libro_disponible: 
        prestamo = {
            "carnet_prestamo": carnet,
            "codigo_prestamo": codigo,
            "fecha": fecha_prestamo
        }
        # Guardar el préstamo en la lista
        lista_prestamos.append(prestamo)
        print("El préstamo se registró correctamente")

def mostrar_prestamos(lista_prestamos):
    print("\n--- LISTA DE PRÉSTAMOS ---")
    # Mostrar cada préstamo de la lista
    for p in lista_prestamos:
        print("Carnet:", p["carnet_prestamo"])
        print("Libro:", p["codigo_prestamo"])
        print("Fecha:", p["fecha"])