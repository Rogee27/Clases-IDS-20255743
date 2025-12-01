# Vamos a proceder a atender pedidos de pizza

def ordenar_pizza(size, masa, *ingredientes): #ahora con args *tatarlo como una lista
    """Vamos a imprimir su orden"""
    print(f"Usted ha ordenado una pizza {size} con masa {masa} de:")
    for i in ingredientes:
   
        print(f"\t- {i}") 


# Llamando a la función
ordenar_pizza("grande", "gruesa", "queso", "tocino", "peperoni", "piña", "jamón", "chile", "tomate")