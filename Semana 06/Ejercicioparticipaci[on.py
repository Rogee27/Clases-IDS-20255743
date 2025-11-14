
app_inicio = True
clientes = []
productos = []
pedidos = []

while app_inicio:
    opcion = int(input(" 1. Mostrar productos \n 2. Agregar producto \n 3. Registrar nuevo cliente \n 4. Mostrar cliente \n 5. Registrar pedido \n 6. Mostrar pedidos del día \n 7. Mostrar categorías disponibles \n 8. Salir \n "))
    if opcion == 8:      
        app_inicio = False
        print("Gracias por preferirnos :)")
