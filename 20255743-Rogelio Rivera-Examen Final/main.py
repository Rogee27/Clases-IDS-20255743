from modulo_funciones import registrar_clientes, registrar_pedido, generar_reporte, salir

inicio_programa = True
while inicio_programa:
    print("   Menú   ")
    print("1. Registrar cliente")
    print("2. Registrar pedido")
    print("3. Generar reporte")
    print("4. Salir")

    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError:
            print("Por favor ingresar el número de las opciones.")
            continue
        break

    if opcion == 1:
        registrar_clientes()
    elif opcion == 2:
        registrar_pedido()
    elif opcion == 3:
        generar_reporte()
    elif opcion == 4:
        inicio_programa = salir()
    else:
        print("Error, vuelva a intentarlo.")