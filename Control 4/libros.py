
def registrar_libro(lista_libros): 
    print("\n--- Registrar Libro ---")

    # Se piden los datos del libro
    Titulo = input("Ingrese el título del libro: ")
    Autor = input("Ingrese el autor del libro: ")

    # Se calcula cuántos libros hay para generar el código del nuevo libro
    numero_libros = len(lista_libros) + 1

    # Se genera el código con ceros dependiendo del número
    if numero_libros < 10:
        codigo_libro = f"L00{numero_libros}"
    elif numero_libros < 100:
        codigo_libro = f"L0{numero_libros}"
    else:
        codigo_libro = f"L{numero_libros}"
    
    # Se crea un diccionario que representa al libro
    Libro = {
        "Título": Titulo,
        "Autor": Autor,
        "Código": codigo_libro,
        "Disponible": True}  # Al registrarlo, siempre está disponible

    # Se agrega el libro a la lista
    lista_libros.append(Libro)

    print("El libro se registro correctamente :)")

def mostrar_libros(lista_libros):
    print("\n--- LISTA DE LIBROS ---")

    # Se recorre libro por libro para mostrarlo
    for libro in lista_libros:

        # Se determina si el libro está disponible o prestado
        if libro["Disponible"] == True:
            estado = "Disponible"
        else:
            estado = "Prestado"

        # Se muestran todos los datos del libro
        print("Código:", libro["Código"])
        print("Título:", libro["Título"])
        print("Autor:", libro["Autor"])
        print("Estado:", estado)


