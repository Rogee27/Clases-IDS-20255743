import modulo_datos as m_d

#Función de registro de clientes

def registrar_clientes():
    while True:
        # Excepciones del cliente
        try: 
            nombre_cliente = input("Digite el nombre: ").strip()
        except Exception:
            print("Error al digitar el nombre. Intente nuevamente")
            continue
        # Verificar que el nombre tenga al menos 2 caracteres
        if len(nombre_cliente) < 2:
            print("El nombre debe tener al menos 2 caracteres.")      
            continue
        break
    while True:
        #Excepciones del correo
        try:
            correo_cliente = input("Ingrese su correo electrónico: ").strip()  
        except Exception:
            print("Error al ingresar su correo. Intente nuevamente.")
            continue
        if correo_cliente == "":
            print("El campo correo no puede quedar vacio. Intente nuevamente")
            continue
        correo_existe = False 
        for correo in m_d.clientes:
            if correo ["Correo electrónico"] == correo_cliente:
                correo_existe = True
                break
        if correo_existe:
            print("El correo ya existe. Intente nuevamente ")  
            continue
        break
    clientes = {
        "Nombre": nombre_cliente,
        "Correo electrónico": correo_cliente
    }
    try:
        m_d.clientes.append(clientes)
    except Exception:
        print("Hubo un problema al ingresar el cliente")
    else:
        print("Se agrego correctamente el cliente al sistema")

# Función de registro de pedidos

def registrar_pedido():
    while True:
        try:
            # 1. Solicitar el correo del cliente.
            correo_cliente_registrar = input("Digite el correo del cliente: ").strip()
        except Exception:
            print("Error al digitar el correo. Intente nuevamente")

        # 2. Debe permitir escribir la palabra salir para regresar al menú.
        if correo_cliente_registrar == "salir":
            return

        # Validación si el carnet existe
        correo_cliente_existe = None
        for cliente in m_d.clientes:
            if cliente["Correo electrónico"] == correo_cliente_registrar:
                correo_cliente_existe = cliente
                break

        if correo_cliente_existe is None:
            print("El correo no existe. Intente nuevamente")
            continue

        break

    # 4. Mostrar lista de sabores disponibles.
    for sabor_disponible in m_d.sabores_disponibles:
        print(f"Letra: {sabor_disponible['letra']}")
        print(f"Sabor: {sabor_disponible['sabor']}")
        

    while True:
        try:
            # 5. Solicitar la primera letra del sabor.
            opcion_sabor = input("Ingrese la primera letra del sabor: ").upper()

        except Exception:
            print("Error al ingresar la letra del sabor. Intenta nuevamente")
            continue
    
        # Validar si el sabor del sorbete existe
        sabor_existe = None
        for sabor in m_d.sabores_disponibles:
            if sabor["letra"] == opcion_sabor:
                sabor_existe = sabor
                break
        
        if sabor_existe is None:
            print("Esa letra de sabor no existe. Intente nuevamente")
            continue
        
        """pedidos = {
            "correo": correo_cliente_registrar,
            "sabor": sabor
        }"""
    
        try:
            m_d.pedidos.append((correo_cliente_registrar, opcion_sabor))
        except Exception:
            print("Error al registrar pedido, intente nuevamente")
            continue
        else:
            print("El pedido fue registrado correctamente")
            break

# Función generar reporte 
def generar_reporte():
    if len(m_d.pedidos) < 1:
        print("No hay pedidos sregistrados")
        return
    
    print("   Sabores   ")
    print("1. C")
    print("2. V")
    print("3. F")
    print("4. L")
    print("5. Cliente sin pedidos")

    while True:
        try:
            opcion_submenu = int(input("Digite una opción: "))
        except ValueError:
            print("Por favor digitar el número de las opciones")
            continue
        break
    
    registrados = 0
    if opcion_submenu == 1:
        print("Pedidos del sabor Chocolate")
        for registrado in m_d.pedidos:
            if registrado[1] == "C": 
                print(f"Correo: {registrado[0]}")
                registrados += 1 
        
        if registrados == 0:
            print("No hay ningún pedido registrado de este sabor")
    elif opcion_submenu == 2:
        print("Pedidos de sabor Vainilla")
        for registrado in m_d.pedidos:
            if registrado[1] == "V":
                print(f"Correo: {registrado[0]}")
                registrados += 1
        
        if registrados == 0:
            print("No hay ningún pedido registrado de este sabor")
    elif opcion_submenu == 3:
        print("Pedidos de sabor Fresa")
        for registrado in m_d.pedidos:
            if registrado[1] == "F":
                print(f"Correo: {registrado[0]}")
                registrados += 1
        
        if registrados == 0:
            print("No hay ningún pedido registrado de este sabor")
    elif opcion_submenu == 4:
        print("Pedidos de sabor Limón")
        for registrado in m_d.pedidos:
            if registrado[1] == "L":
                print(f"Correo: {registrado[0]}")
                registrados += 1
        
        if registrados == 0:
            print("No hay ningún pedido registrado de este sabor")
    elif opcion_submenu == 5:
        for cliente in m_d.clientes:
            cliente_no_registrado = True 

            for registrado in m_d.pedidos:
                if cliente["correo_cliente"] == registrado[0]: 
                    cliente_no_registrado = False
                    break

            if cliente_no_registrado:
                print(f"Correos de clientes: {cliente['carnet_estudiante']}")
                print(f"Nombre del estudiante: {cliente['nombre_estudiante']}")
        
                

def salir():
    print("Gracias por preferirnos ...")
    return False
        
