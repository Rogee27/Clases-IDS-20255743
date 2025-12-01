import modulo_datos as m_d

# Registrar estudiante
def registrar_estudiante():
    """Pide al usuario que ingrese el carnet, nombre, apellido del estudiante, además de las validacionesque se agregarán en el diccionario"""
    while True:

        try:
            carnet_estudiante = input("Ingrese el carnet: ").strip()
        except Exception:
            # Validar valores que no se permiten
            print("Error de valor al ingresas el carnet, vuelva a intentarlo.")
            continue
        # Excepción de entrada vacía
        if carnet_estudiante == "":
            print("El campo de carnet no puede quedar vacio. Intente nuevamente.")
        # Validación de caracteres necesarios 
        if len(carnet_estudiante) < 6 or len(carnet_estudiante) > 10:
            print("El carnet debe tener entre 6 y 10 caracteres")
            continue
        # Validar si el carnet ya existe
        carnet_existe = False 
        for estudiante in m_d.lista_estudiantes:
            if estudiante ["carnet_estudiante"] == carnet_estudiante:
                carnet_existe = True
                break
        if carnet_existe:
            print("El carnet ya existe. Intente nuevamente ")  
            continue
        break
    while True:

        # Excepciones
        try: 
            nombre_estudiante = input("Digite el nombre: ").strip()
        except Exception:
            print("Error al digitar el nombre. Intente nuevamente")
            continue
        # Verificar que el campo no quede vacio
        if nombre_estudiante == "":
            print("El campo no puede quedar vacio. Intente nuevamente")
            continue
        # Verificar que el nombre tenga al menos 2 caracteres
        if len(nombre_estudiante) < 2:
            print("El nombre debe tener al menos 2 caracteres.")      
            continue
        break
    while True:
        try:
            apellido_estudiante = input("Digite el apellido").strip()  
        except Exception:
            print("Error al digitar el apellido. Intente nuevamente.")
            continue
        if apellido_estudiante == "":
            print("El campo apellido no puede quedar vacio. Intente nuevamente")
            continue
        if len(apellido_estudiante) < 2:
            print("El apellido debe etener al menos 2 caracteres")
            continue
        break
    estudiante = {
        "carnet_estudiante": carnet_estudiante,
        "nombre_estudiante": nombre_estudiante,
        "apellido_estudiante": apellido_estudiante
    }

    try:
        m_d.lista_estudiantes.append(estudiante)
    except Exception:
        print("Hubo un problema al ingresar el estudiante")
    else:
        print("Se agrego correctamente el estudiante al sistema")

def inscribir_en_curso():
    """
    Docstring para inscribir_en_curso
    """
    while True:
        try:
            # 1. Solicitar el carnet del estudiante.
            carnet_estudiante_inscribir = input("Digite el carnet del estudiante a inscribir: ").strip()
        except Exception:
            print("Error al digitar el carnet. Intente nuevamente")

        # 2. Debe permitir escribir la palabra salir para regresar al menú.
        if carnet_estudiante_inscribir == "salir":
            return
        
        # Validación de que no este vacio el campo
        if carnet_estudiante_inscribir == "":
            print("El campo de carnet no puede estar vacio. Intente nuevamente")
            continue

        # Validación si el carnet existe
        carnet_estudiante_existe = None
        for estudiante in m_d.lista_estudiantes:
            if estudiante["carnet_estudiante"] == carnet_estudiante_inscribir:
                carnet_estudiante_existe = estudiante
                break

        if carnet_estudiante_existe is None:
            print("El carnet no existe. Intente nuevamente")
            continue

        break

    # 4. Mostrar lista de cursos disponibles.
    for curso_disponible in m_d.lista_cursos_disponibles:
        print(f"Código: {curso_disponible['codigo']}")
        print(f"Descripción: {curso_disponible['descripcion']}")
        print("-" * 6)

    while True:
        try:
            # 5. Solicitar el código del curso.
            opcion_curso = input("Digite el código del curso: ")
        except Exception:
            print("Error al deigitar el codigo. Intenta nuevamente")
            continue
    
        # Validar si el código del curso existe
        curso_existe = None
        for curso in m_d.lista_cursos_disponibles:
            if curso["codigo"] == opcion_curso:
                curso_existe = curso
                break
        
        if curso_existe is None:
            print("El código del curso no existe. Intente nuevamente")
            continue

        # Validar si el estudiante ya esta inscrito al curso
        ya_inscrito = False
        for inscripcion in m_d.lista_de_inscripciones:
            if inscripcion[0] == carnet_estudiante_inscribir and inscripcion[1] == opcion_curso:
                ya_inscrito = True
                break

        if ya_inscrito:
            print("El estudiante ya está inscrito en este curso. Pruebe otro curso.")
            continue

        try:
            m_d.lista_de_inscripciones.append((carnet_estudiante_inscribir, opcion_curso))
        except Exception:
            print("Error al inscribir al alumnos, intente nuevamente")
            continue
        else:
            print("El alumno fue inscrito correctamente")
            break

def generar_reporte():
    
    if len(m_d.lista_de_inscripciones) < 1:
        print("No hay alumnos inscritos")
        return
    
    print("----- Cursos ------")
    print("1. PY")
    print("2. JS")
    print("3. BD")
    print("4. SE")
    print("5. Estudiantes sin inscripción")

    while True:
        try:
            opcion_submenu = int(input("Digite una opción: "))
        except ValueError:
            print("Por favor digitar el número de las opciones")
            continue
        break
    
    inscritos = 0
    if opcion_submenu == 1:
        print("Inscritos en el Curso de PY")
        for inscrito in m_d.lista_de_inscripciones:
            if inscrito[1] == "PY": 
                print(f"Carnet: {inscrito[0]}")
                inscritos += 1 
        
        if inscritos == 0:
            print("No hay ningún estudiante inscrito a este curso")
    elif opcion_submenu == 2:
        print("Inscritos en el Curso de JS")
        for inscrito in m_d.lista_de_inscripciones:
            if inscrito[1] == "JS":
                print(f"Carnet: {inscrito[0]}")
                inscritos += 1
        
        if inscritos == 0:
            print("No hay ningún estudiante inscrito a este curso")
    elif opcion_submenu == 3:
        print("Inscritos en el Curso de BD")
        for inscrito in m_d.lista_de_inscripciones:
            if inscrito[1] == "BD":
                print(f"Carnet: {inscrito[0]}")
                inscritos += 1
        
        if inscritos == 0:
            print("No hay ningún estudiante inscrito a este curso")
    elif opcion_submenu == 4:
        print("Inscritos en el Curso de SE")
        for inscrito in m_d.lista_de_inscripciones:
            if inscrito[1] == "SE":
                print(f"Carnet: {inscrito[0]}")
                inscritos += 1
        
        if inscritos == 0:
            print("No hay ningún estudiante inscrito a este curso")
    elif opcion_submenu == 5:
        for estudiante in m_d.lista_estudiantes:
            estudiante_no_inscrito = True 

            for inscrito in m_d.lista_de_inscripciones:
                if estudiante["carnet_estudiante"] == inscrito[0]: 
                    estudiante_no_inscrito = False
                    break

            if estudiante_no_inscrito:
                print(f"Carnet del estudiante: {estudiante['carnet_estudiante']}")
                print(f"Nombre del estudiante: {estudiante['nombre_estudiante']}")
                print(f"Apellido del estudiante: {estudiante['apellido_estudiante']}")
                print("-" * 6)

def salir():
    print("Gracias por preferirnos ...")
    return False
        