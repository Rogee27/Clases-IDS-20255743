"""
Este módulo contiene las funciones que utiliza el cliente dentro del sistema. 
Permite visualizar el menú del día, realizar pedidos y consultar el historial 
personal de compras. Todas las funciones dependen de listas compartidas que 
son enviadas desde el módulo principal (main.py).
"""

def ver_menu(menu):
    """
    Muestra los platos disponibles en el menú del día. Solo se muestran los platos 
    cuya cantidad sea mayor que cero. Recibe la lista de platos creada por el 
    administrador y la imprime en pantalla.
    """

    print("----- Menú del día -----")
    # Para poder mostrar los platos solo si la cantidad es mayor a 0, o sea que si hay platos.
    for plato in menu:
        if plato["cantidad"] > 0:
            print("Código:", plato["codigo"]) 
            print("Nombre:", plato["nombre"])
            print("Precio:", plato["precio"])

def hacer_pedido(menu, pedidos, carnet, historial_clientes):
    """
    Permite al cliente realizar un pedido seleccionando un plato por su código. 
    Verifica si el plato existe y si está disponible. Si el pedido es válido, 
    descuenta una unidad del menú y registra la información tanto en la lista de 
    pedidos general como en el historial personal del cliente.
    """

    print("----- Realizar pedido -----")

    # Les pedimos el código del plato que quieren
    codigo_plato = input("Ingrese el código del plato que desea ordenar: ")

    # Estos son los boolenos para saber si el plato existe y si hay disponible
    plato_encontrado = False
    plato_disponible = False

    # Con el for-in revisamos todos los platos del menu y con el if la condición
    for plato in menu:
        if plato["codigo"] == codigo_plato:
            plato_encontrado = True
            # Revisamos si hay platos
            if plato["cantidad"] > 0:
                plato_disponible = True 

    # Si no existen o si existe pero no hay les ponemos eso             
    if plato_encontrado == False:
        print("Este plato no existe :(")
    if plato_disponible == False:
        print("Este plato no está disponible :(")
        
    # Esto para que si existe y hay disponible que siga corriendo y pedir fecha
    if plato_encontrado and plato_disponible == True:
        fecha = input("Ingrese la fecha del pedido: ")
        # Le restamos el -1 para que se quite de la lista ya que ya lo van a pedir
        for plato in menu:
            if plato["codigo"] == codigo_plato:
                plato["cantidad"] = plato["cantidad"] - 1
        # Este es el diccionario con la info del pedido
        pedido = {
            "codigo_plato": codigo_plato,
            "carnet": carnet, 
            "fecha": fecha
        }

        # Lo guardamos en el del admin
        pedidos.append(pedido)
        # Lo guardamos en el historial de pedidos del cliente para que le salga
        historial_clientes.append(pedido)
        print("Pedido registrado correctamente :)")
    

def ver_historial_cliente(historial_clientes, carnet):
    """
    Muestra el historial de pedidos asociados al carnet del cliente. Si el cliente 
    no tiene registros, informa que no hay pedidos disponibles.
    """

    print("----- Tú historial -----")

    # Otro boolenao para saber si tiene pedidos
    tiene_pedidos = False

    # Que lo busque en todeos los pedidos
    for pedido in historial_clientes:
        # Si el carnet del pedido coincide con el carnet del estududiante entonces que lo muestre
        if pedido["carnet"] == carnet:
            tiene_pedidos = True
            print("Plato:", pedido["codigo_plato"])
            print("Fecha:", pedido["fecha"])

    # Si es que no tiene pedidos
    if tiene_pedidos == False:
        print("No tiene pedidos registrados.")  