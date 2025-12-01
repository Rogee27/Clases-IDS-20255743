# Creación de la estructura base del sistema
clientes = [{"dui":"07476069-8", "nombre":"Rogelio", "apellido":"Rivera"}]
menu = True
while menu:
    print("""---menu--- 
1. Crear cliente
2. Contratar servicio
3. Listar clientes por servicio
4. Salir
""")
    opcion = int(input("Selecciona una opción: "))
    if opcion == 1:
        dui = input("Ingrese su numero de DUI: ")
        if len(dui)!=10 and (dui[-2] != "-"):
            print("Dui no existe")
        for dato in clientes:
            if dato["dui"] == dui:
                print("Dui existente")
    nombre = input("Ingrese su primer nombre: ")
    if len(nombre) < 2:
        print("nombre no valido")   
        continue
   
    apellido = input ("Ingrese su primer apellido ")
    if len(apellido) < 2:
        print("apellido no valido")
        continue