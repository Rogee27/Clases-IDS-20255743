
def registrar_estudiante(lista_estudiantes):
    print("\n--- Registrar Estudiante ---")

    # Pedir el nombre del estudiante
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")

    # Calcular cuántos estudiantes hay + 1 para generar el carnet
    carnet_estudiante = len(lista_estudiantes) + 1

    # Crear el carnet con el formato S001, S002, etc.
    if carnet_estudiante < 10:
        carnet = f"S00{carnet_estudiante}"
    elif carnet_estudiante < 100:
        carnet = f"S0{carnet_estudiante}"
    else: 
        carnet = f"S{carnet_estudiante}"
    
    # Crear el diccionario del estudiante
    Estudiante = {
        "Nombre": nombre_estudiante,
        "Carnet": carnet
    }

    # Guardar el estudiante en la lista
    lista_estudiantes.append(Estudiante)

    print("Estudiante registrado correctamente :)")

def mostrar_estudiantes(lista_estudiantes):
    print("\n--- LISTA DE ESTUDIANTES ---")

    # Recorrer y mostrar cada estudiante de la lista
    for est in lista_estudiantes:
        print("Carnet:", est["Carnet"])
        print("Nombre:", est["Nombre"])
    