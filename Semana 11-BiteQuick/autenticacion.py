"""
Este módulo contiene las funciones relacionadas con la autenticación de usuarios.
Permite crear nuevas cuentas de clientes y manejar el proceso de inicio de sesión.
Las funciones trabajan con la lista de usuarios enviada desde el módulo principal 
además devuelve el rol del que incio sesión para mostrar unas funciones u otras.
"""

def crear_cuenta(lista_usuarios):
    """
    Registra un nuevo usuario en el sistema. Solicita al cliente su nombre, 
    apellido, carnet, correo y contraseña. La información se guarda como un 
    diccionario dentro de la lista 'lista_usuarios'. El rol asignado 
    por defecto es 'cliente'.
    """

    # bucle de validación para que el nombre del usuario no quede vacio
    while True:
        nombre_usuario_nuevo = input("Ingrese su nombre: ")
        if nombre_usuario_nuevo == "":
            print("El nombre no puede estar vacío. Por favor ingrese un nombre")
        else:
            break

    # bucle de validación para que el apellido del usuario no quede vacio
    while True:
        apellido_usuario_nuevo = input("Ingrese su apellido: ")
        if apellido_usuario_nuevo == "":
            print("El apellido no puede estar vacío. Por favor ingrese un apellido")
        else:
            break
    
    # bucle de validación para que el carnet del usuario
    while True:
        carnet_usuario_nuevo = input("Ingrese su número de carnet (8 dígitos): ")

        # que el carnet no quede vacío
        if carnet_usuario_nuevo == "":
            print("El número de carnet no puede estar vacío.")
            continue
        
        # debe ser totalmente numérico (para 20255763)
        if not carnet_usuario_nuevo.isdigit():
            print("El carnet solo debe contener números.")
            continue

        # debe tener longitud 8
        if len(carnet_usuario_nuevo) != 8:
            print("El carnet debe tener exactamente 8 dígitos (ej: 20255762).")
            continue

        break

    # bucle de validación para correo institucional
    while True:
        correo_usuario_nuevo = input("Ingrese su correo institucional: ")

        if correo_usuario_nuevo == "":
            print("El correo no puede estar vacío.")
            continue

        # debe contener 1 arroba
        if "@" not in correo_usuario_nuevo:
            print("El correo debe contener '@'.")
            continue

        # separar en dos partes
        partes = correo_usuario_nuevo.split("@")

        if len(partes) != 2:
            print("El correo solo debe tener un '@'.")
            continue

        username, dominio = partes

        # username no puede estar vacío
        if username == "":
            print("Debe haber texto antes del '@'.")
            continue

        # dominio no puede estar vacío
        if dominio == "":
            print("Debe haber texto después del '@'.")
            continue

        # username debe tener 8 caracteres (ej: 20255762)
        if len(username) != 8:
            print("Antes del '@' debe haber exactamente 8 caracteres (ej: 20255762).")
            continue

        # username debe ser numérico
        if not username.isdigit():
            print("Antes del '@' deben ser solo números (su carnet).")
            continue

        # validar dominio exacto
        if dominio != "esen.edu.sv":
            print("El correo debe terminar exactamente en '@esen.edu.sv'.")
            continue

        break

    # bucle de validación para que la contraseña del usuario no quede vacio
    while True: 
        contrasena_usuario_nuevo = input("Ingrese su contraseña: ")
        if contrasena_usuario_nuevo == "":
            print("La contraseña no puede estar vacía. Por favor ingrese una contraseña")
        else:
            break


    # Con todos los datos que se le pedi al usuario, se crea un diccionario
    usuario = {
        "nombre_usuario": nombre_usuario_nuevo,
        "apellido_usuario": apellido_usuario_nuevo,
        "carnet_usuario": carnet_usuario_nuevo,
        "correo_usuario": correo_usuario_nuevo,
        "contrasena_usuario": contrasena_usuario_nuevo,
        "rol_usuario": "cliente"
    }

    # Se guarda este diccionario en la lista que se pasa como parametro de la función
    lista_usuarios.append(usuario)
    print("Se registro exitosamente el nuevo usuario")

def iniciar_sesion(lista_usuarios):
    """
    Permite a un usuario iniciar sesión mediante su número de carnet y contraseña.
    Busca el carnet en la lista de usuarios y, si lo encuentra, compara la 
    contraseña ingresada. Si ambas coinciden, devuelve el rol del usuario y su carnet.
    """

    # bucle de validación para pedir un carnet existente
    while True:
        # Se le pide al usuario su número de carnet
        numero_carnet_inicio = input("Digite su número de carnet: ")

        # un for-in para recorrer la lista de usuario en busca del carnet que acaba se acaba de digitar
        usuario_encontrado = None
        for usuario in lista_usuarios:
            if usuario["carnet_usuario"] == numero_carnet_inicio:
                usuario_encontrado = usuario
                break

        # Validación por si no se encuetra el carnet digitado
        if usuario_encontrado is None:
            print("El número de carnet que digitaste no existe. Intente nuevamente")
        else: 
            break

    # bucle de validación para pedir contraseña correcta
    while True:
        # Se le pide la contraseña al usuario
        contrasena_inicio = input("Digite su contraseña: ")

        if usuario_encontrado["contrasena_usuario"] != contrasena_inicio:
            print("Contraseña incorrecta. Intente nuevamente.")
        else:
            print("Sesión iniciada")
            # Devolvemos el rol del usuario y el carnet del usuario, al modulo principal,
            # ya que se ocupan para otras funciones
            return usuario_encontrado["rol_usuario"], usuario_encontrado["carnet_usuario"]