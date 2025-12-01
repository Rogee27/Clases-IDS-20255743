"""clientes = []
servicios = []
contrataciones = []

def menu_principal(clientes, servicios, contrataciones):
    while True:
        print("   MENÚ PRINCIPAL   ")
        print("1. Crear cliente")
        print("2. Contratar servicio")
        print("3. Listar clientes por servicio")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_clientes(clientes)

        elif opcion == "2":
            contratar_servicio(clientes, servicios, contrataciones)

        elif opcion == "3":
            listar_clientes_por_servicios(clientes, contrataciones)

        elif opcion == "4":
            print("Gracias por usar el sistema :)")
            break

        else:
            print("Opción inválida.")

def crear_clientes(clientes):
    print("   Crear Cliente   ")

validar_dui = False 
while validar_dui == False:
    dui = input("Ingrese el número de DUI: ")
    if len(dui)!=10 and (dui[-2] != "-"):
            print("Dui no existe")
    else:
         existe_dui = False
         for cliente in clientes:
              if cliente["dui"] == dui:
                   existe_dui = True

         if existe_dui == True:
              print("Este DUI ya está registrado.")
         else:
              validar_dui = True

validar_nombre = False
while validar_nombre == False:
    nombre = input("Ingrese el primer nombre: ")
    if len(nombre) < 2:
        print("El nombre tiene que tener más de dos carácteres: ")
    else:
         validar_nombre = True

validar_apellido = False
while validar_apellido == False:
    apellido = input("Ingrese el primer apellido: ")
    if len(apellido) < 2:
        print("El nombre tiene que tener más de dos carácteres: ")
    else:
         validar_apellido = True

cliente = {
     "dui": dui,
     "nombre": nombre,
     "apellido": apellido
}

clientes.append(cliente)
print("El cliente se creo correctamente.")

def contratar_servicio(clientes, servicios, contratacioenes):
    print("   Contratar servicio   ")
dui = input("Ingrese e DUI del cliente a contratar: ")
existe_clientes = False
for numero_dui in clientes:
    if numero_dui["dui"] == dui:
        existe_clientes = True
    if existe_clientes == False:
        print("Este cliente no existe")
    else:
         contratado = False
         for esta_contartado in contrataciones:
              if esta_contartado["dui"] == dui:
                   contratado = True

         if contratado == True:
              print("Este cliente no está disponible.")
         else: 
              print("   Servicios disponibles   ")
              for tipos_servicios in servicios:
                print(tipos_servicios["codigo"], "-", tipos_servicios["nombre"])
              codigo_servicio = input("Ingrese en código del servicio: ")
              existe_servicio = False
              for tipos_servicios in servicios:
                if tipos_servicios["codigo"] == codigo_servicio:
                    servicio_existe = True
                if servicio_existe == False:
                    print("Este servicio no existe")
                else: 
                    nueva_contratacion = {
                    "dui": dui,
                    "servicio": codigo_servicio
                }

                contrataciones.append(nueva_contratacion)

                print("Servicio contratado correctamente.")

def listar_clientes_por_servicios(clientes, contrataciones):
    print("  Clientes por Servicio   ")
    if len(contrataciones) == 0:
        print("Aún no hay contrataciones registradas :(")
    else:
        # Paso 2- mostrar submenú
        print("Seleccione un servicio:")
        print("1. WD")
        print("2. DS")
        print("3. ML")
        print("4. API")
        print("5. No contratados")

        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            servicio = "WD"
            print("\nClientes que contrataron WD:")
            encontrados = False
            for c in contrataciones:
                if c["servicio"] == servicio:
                    print("DUI:", c["dui"])
                    encontrados = True
            if encontrados == False:
                print("Ningún cliente ha contratado WD.")
        elif opcion == "2":
            servicio = "DS"
            print("\nClientes que contrataron DS:")
            encontrados = False
            for c in contrataciones:
                if c["servicio"] == servicio:
                    print("DUI:", c["dui"])
                    encontrados = True
            if encontrados == False:
                print("Ningún cliente ha contratado DS.")

        elif opcion == "3":
            servicio = "ML"
            print("\nClientes que contrataron ML:")
            encontrados = False

            for c in contrataciones:
                if c["servicio"] == servicio:
                    print("DUI:", c["dui"])
                    encontrados = True
            
            if encontrados == False:
                print("Ningún cliente ha contratado ML.")
        elif opcion == "4":
            servicio = "API"
            print("\nClientes que contrataron API:")
            encontrados = False

            for c in contrataciones:
                if c["servicio"] == servicio:
                    print("DUI:", c["dui"])
                    encontrados = True
            
            if encontrados == False:
                print("Ningún cliente ha contratado API.")

        elif opcion == "5":
            print("\nClientes que NO han contratado ningún servicio:")
            encontrados = False

            for cliente in clientes:
                contrato = False
                for ct in contrataciones:
                    if ct["dui"] == cliente["dui"]:
                        contrato = True
                
                if contrato == False:
                    print("DUI:", cliente["dui"], "-", cliente["nombre"], cliente["apellido"])
                    encontrados = True
            
            if encontrados == False:
                print("Todos los clientes tienen un servicio contratado.")

        else:
            print("Opción inválida.")"""

clientes = []
contrataciones = []

# Servicios fijos
servicios = [
    {"codigo": "WD", "nombre": "Desarrollo Web"},
    {"codigo": "DS", "nombre": "Ciencia de Datos"},
    {"codigo": "ML", "nombre": "Machine Learning Aplicado"},
    {"codigo": "API", "nombre": "Desarrollo de APIs Empresariales"}
]


def crear_clientes(clientes):
    print("   Crear Cliente   ")

    # validar DUI
    validar_dui = False
    while validar_dui == False:
        dui = input("Ingrese el número de DUI: ")

        if len(dui) != 10:
            print("El DUI debe tener 10 caracteres (incluyendo guion).")
        else:
            existe_dui = False
            for cliente in clientes:
                if cliente["dui"] == dui:
                    existe_dui = True

            if existe_dui == True:
                print("Este DUI ya está registrado.")
            else:
                validar_dui = True

    # validar nombre
    validar_nombre = False
    while validar_nombre == False:
        nombre = input("Ingrese el primer nombre: ")
        if len(nombre) < 2:
            print("El nombre debe tener mínimo 2 caracteres.")
        else:
            validar_nombre = True

    # validar apellido
    validar_apellido = False
    while validar_apellido == False:
        apellido = input("Ingrese el primer apellido: ")
        if len(apellido) < 2:
            print("El apellido debe tener mínimo 2 caracteres.")
        else:
            validar_apellido = True

    # guardar cliente
    cliente = {
        "dui": dui,
        "nombre": nombre,
        "apellido": apellido
    }

    clientes.append(cliente)
    print("El cliente se creó correctamente.")



def contratar_servicio(clientes, servicios, contrataciones):
    print("   Contratar servicio   ")

    dui = input("Ingrese el DUI del cliente a contratar: ")

    # verificar si existe cliente
    existe_cliente = False
    for c in clientes:
        if c["dui"] == dui:
            existe_cliente = True

    if existe_cliente == False:
        print("Este cliente no existe.")
    else:
        # verificar si ya tiene servicio
        contratado = False
        for ct in contrataciones:
            if ct["dui"] == dui:
                contratado = True

        if contratado == True:
            print("Este cliente ya tiene un servicio contratado.")
        else:
            # mostrar servicios
            print("   Servicios disponibles   ")
            for s in servicios:
                print(s["codigo"], "-", s["nombre"])

            codigo_servicio = input("Ingrese el código del servicio: ")

            servicio_existe = False
            for s in servicios:
                if s["codigo"] == codigo_servicio:
                    servicio_existe = True

            if servicio_existe == False:
                print("Este servicio no existe.")
            else:
                nueva_contratacion = {
                    "dui": dui,
                    "servicio": codigo_servicio
                }

                contrataciones.append(nueva_contratacion)
                print("Servicio contratado correctamente.")



def listar_clientes_por_servicios(clientes, contrataciones):
    print("  Clientes por Servicio   ")

    if len(contrataciones) == 0:
        print("Aún no hay contrataciones registradas :(")
    else:
        print("Seleccione un servicio:")
        print("1. WD")
        print("2. DS")
        print("3. ML")
        print("4. API")
        print("5. No contratados")

        opcion = input("Ingrese una opción: ")

        # WD
        if opcion == "1":
            servicio = "WD"
            print("\nClientes que contrataron WD:")
            encontrados = False
            for c in contrataciones:
                if c["servicio"] == servicio:
                    print("DUI:", c["dui"])
                    encontrados = True
            if encontrados == False:
                print("Ningún cliente ha contratado WD.")

        # DS
        elif opcion == "2":
            servicio = "DS"
            print("\nClientes que contrataron DS:")
            encontrados = False
            for c in contrataciones:
                if c["servicio"] == servicio:
                    print("DUI:", c["dui"])
                    encontrados = True
            if encontrados == False:
                print("Ningún cliente ha contratado DS.")

        # ML
        elif opcion == "3":
            servicio = "ML"
            print("\nClientes que contrataron ML:")
            encontrados = False

            for c in contrataciones:
                if c["servicio"] == servicio:
                    print("DUI:", c["dui"])
                    encontrados = True
            
            if encontrados == False:
                print("Ningún cliente ha contratado ML.")

        # API
        elif opcion == "4":
            servicio = "API"
            print("\nClientes que contrataron API:")
            encontrados = False

            for c in contrataciones:
                if c["servicio"] == servicio:
                    print("DUI:", c["dui"])
                    encontrados = True
            
            if encontrados == False:
                print("Ningún cliente ha contratado API.")

        # No contratados
        elif opcion == "5":
            print("\nClientes que NO han contratado ningún servicio:")
            encontrados = False

            for cliente in clientes:
                contrato = False
                for ct in contrataciones:
                    if ct["dui"] == cliente["dui"]:
                        contrato = True
                
                if contrato == False:
                    print("DUI:", cliente["dui"], "-", cliente["nombre"], cliente["apellido"])
                    encontrados = True
            
            if encontrados == False:
                print("Todos los clientes tienen un servicio contratado.")

        else:
            print("Opción inválida.")



def menu_principal(clientes, servicios, contrataciones):
    while True:
        print("\n   MENÚ PRINCIPAL   ")
        print("1. Crear cliente")
        print("2. Contratar servicio")
        print("3. Listar clientes por servicio")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_clientes(clientes)

        elif opcion == "2":
            contratar_servicio(clientes, servicios, contrataciones)

        elif opcion == "3":
            listar_clientes_por_servicios(clientes, contrataciones)

        elif opcion == "4":
            print("Gracias por usar el sistema :)")
            break

        else:
            print("Opción inválida.")

menu_principal(clientes, servicios, contrataciones)