"""
Este módulo contiene las funciones que permiten al administrador gestionar 
el menú del día y revisar los pedidos realizados por los clientes. Incluye 
la creación de platos, la eliminación del menú y la visualización de pedidos 
registrados. Estas funciones reciben listas compartidas desde el módulo principal (main.py).
"""

def registrar_plato(menu):
    """
    Agrega un nuevo plato al menú del día. Solicita al administrador el nombre,
    precio y cantidad disponible. Genera automáticamente un código único y 
    lo agrega a la lista 'menu'.
    """

    print("----- Registrar plato -----")

    # Pedirle al adminitrador el nombre del plato a registrar
    nombre_plato=input("Ingrese el nombre del plato a crear: ")

    # Validación y manejo de errores para ingresar el precio del plato a agregar
    # Se ocupa un bucle para que le vuelva a preguntar el precio si se equivoco
    while True:
        try:
            # Se le pide al usuario el precio del plato a agregar
            # Si digita bien, se sale del bucle con el break y continua con lo demás
            precio = float(input("Ingrese el precio del plato: "))
            break
        except ValueError:
            # Mensaje de error, por si se digita un valor que no sea númerico
            print("Por favor ingrese un número válido para el precio.")

    # Se crea el codigo del plato de manera automatica
    numero_plato=len(menu)+1
    if numero_plato<10:
        codigo_plato=f"P00{numero_plato}"
    elif numero_plato<100:
        codigo_plato=f"P0{numero_plato}"
    else:
        codigo_plato=f"P{numero_plato}"

    # Validación y manejo de errores para ingresar la cantidad disponible del plato a agregar
    # Se ocupa un bucle para que le vuelva a preguntar la cantidad si se equivoco
    while True:
        try:
            # Se le pide al usuario la cantidad disponible del plato a agregar
            # Si digita bien, se sale del bucle con el break y continua con lo demás
            cantidad=int(input("Ingrese la cantidad disponible: "))
            break
        except ValueError:
            # Mensaje de error, por si se digita un valor que no sea númerico
            print("Por favor ingrese un número válido para el precio.")

    # Se guarda lo que se le acaba de pedir al usuario en un diccionario
    plato={
        "nombre":nombre_plato,
        "precio":precio,
        "codigo":codigo_plato,
        "cantidad":cantidad
    }

    # Se agrega al diccionario a la lista menu, que se recibe en el parametro de la función
    menu.append(plato)
    print("Plato agregado al menú correctamente")


def eliminar_menu(menu):
    """
    Elimina todos los platos del menú del día, dejándolo vacío.
    """

    menu.clear() # Limpio la lista, ya que se actualiza cada día
    print("El menú del día ha sido eliminado correctamente.")

def ver_pedidos_admin(pedidos):
    """
    Muestra todos los pedidos registrados durante el día.
    """
    # Mensaje por si no hay pedido registrados
    if not pedidos:
        print("No hay pedidos registrados.")
        return
    
    print("----- Pedidos -----")
    for plato in pedidos:
        # Se recorre la lista pedidos para mostrar los encargos de los clientes
        print("Código plato:", plato["codigo_plato"])
        print("Carnet del cliente:", plato["carnet"])
        print("Fecha:", plato["fecha"])
        print("-" * 20)