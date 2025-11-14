# Parte 1: Configuración inicial.

agente = "encargado"      #Creación de las variables del agente y las vacias donde iran las listas.
platillo = []
precios = []

# Parte 2: Ingreso a la aplicación.

while(input("Por favor ingrese el nombre del agente: ")) != agente:   #Creación del while con un input para ingresar como la palabra clave y me deje entrar. 
    print("Agente no registrado")

# Parte 3: Gestión del menú principal.

agente = True      #Creación de variable agente porque así le puedo poner que siga el programa en True o Salir del paso 4 en falso. Creación de la variable de las opciones y le puse \n para que se mire ordenado verticalmente. 
while agente: 
    opcion = int(input("Selecciona una de las siguientes opciones: \n 1. Creación de platillos \n 2. Consulta de platillos y precios \n 3. Colocar un pedido \n 4. Salir \n "))

# Parte 4: Creación de platillos. 

    if opcion == 1:       
        platillo.append(input("Ingrese el nombre del platillo a crear: ").lower())     #Creación del if para la opción 1 con .append para que se agrege a la lista de platillos y variables. Además le puse .lower () para que no haya problma después (Ya me pasó y no funcionaba jajajaja). Y float para tirar decimales en los precios.
        precios.append(float(input("Ingrese el precio del platillo a crear: ")))

# Parte 5: Consulta de platillos.

    elif opcion == 2:             #Elif de la opción 2 y un if con len porque así le digo que me busque en la lista de los platillos y for in range para que me busque  en  el rango de todos los valores o bueno variables de la lista. Imprimir lo que ya puse en la lista con el platillo y precio y Else para que si no hay nada me tire el mensaje de que no he puesto nada.
        if len(platillo) > 0:
            for i in range(len(platillo)): 
                print(f"{platillo[i]}: ${precios[i]:.2f}")
        else: 
            print("Actualmente no hay platillos ingresados")
    
# Parte 6: Colocar un pedido. 

    elif opcion == 3: 
        nombre = input("Indique el nombre del platillo para su orden: ")    #Aquí me confundí un poco, pero recorde que, en clase para la opción 3, creo otra variable que sería el nombre del platillo que quiero y luego un if con un (i) para que me busque el platillo en la lista con .append y luego que se imprima lo que el usuario escriba si es que está en la lista sino el else.
        if nombre.lower() in platillo:
            i = platillo.index(nombre.lower())
            print(f"Usted ha elegido {platillo[i]} con un precio de ${precios[i]:.2f}")
        else: 
            print("Este platillo no existe.")

#Parte 7: Salir. 

    elif opcion == 4:     #Por último, elif de la opción 4 y como ya había creado que agente = True, si quiero salir sería agente = False y que imprima un mensaje para ser amable.
        agente = False
        print("Gracias por preferirnos :)")

    