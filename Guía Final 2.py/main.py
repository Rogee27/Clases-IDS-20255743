from modulo_funciones import registrar_estudiante, inscribir_en_curso, generar_reporte, salir

inicio_programa = True
while inicio_programa:
    print("   Menú   ")
    print("1. Registrar estudiantes")
    print("2. Inscribir curso")
    print("3. Generar Reportes")
    print("4. Salir")

    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError:
            print("Por favor ingresar el número de las opciones.")
            continue
        break

    if opcion == 1:
        registrar_estudiante()
    elif opcion == 2:
        inscribir_en_curso()
    elif opcion == 3:
        generar_reporte()
    elif opcion == 4:
        inicio_programa = salir()
    else:
        print("Error, vuelva a intentarlo.")
