"""nota = float(input("Ingrese la nota: "))
if nota == 10: 
    print("E")
elif nota > 7:
    print("MB")
else:
    if nota > 5:
        print("B")
    else: 
        if nota > 3: 
            print("R")
        else:
            print("M")"""

"""monto = float(input("Ingrese el monto: "))
if monto > 500:
    print(f"{(monto*0.1):.2f}")
    print(f"{(monto*0.14):.2f}")
else:
    if monto > 200:
        print(f"{(monto*0.08):.2f}")
        print(f"{(monto*0.12):.2f}")
    else: 
        if monto > 50:
            print(f"{(monto*0.06):.2f}")
            print(f"{(monto*0.1):.2f}")
        else:
            print(monto)
            print(monto)"""
"""monto= float(input("coloque monto: "))
venta= input("coloque si la venta fue local o exportado: ").lower()
if monto > 500 and venta == "local": 
    print(f"El impuesto de la venta es de: {monto*0.10}")
elif monto > 200 and venta == "local": 
    print(f"El impuesto de la venta es de: {monto*0.08}")
elif monto > 50 and venta == "local": 
    print(f"El impuesto de la venta es de: {monto*0.06}")
elif monto <= 50 and venta == "local": 
    print(f"El impuesto de la venta es de: {monto*0.00}")
else: 
    if monto > 500 and venta == "exportado": 
        print(f"El impuesto de la venta es de: {monto*0.14}")
    elif monto > 200 and venta == "exportado": 
        print(f"El impuesto de la venta es de: {monto*0.12}")
    elif monto > 50 and venta == "exportado": 
        print(f"El impuesto de la venta es de: {monto*0.10}")
    elif monto <= 50 and venta == "exportado": 
        print(f"El impuesto de la venta es de: {monto*0.00}")"""
"""monto = int(input('Ingrese el monto: '))
tipo = input('Ingrese el tipo de venta: ')

if tipo.lower() == 'local':
    if monto > 500:
        impuesto = 0.1
    else:
        if monto > 200:
            impuesto = 0.08
        else:
            if monto > 50:
                impuesto = 0.06
            else:
                impuesto = 0
                
elif tipo.lower() == 'exportacion':
    if monto > 500:
        impuesto = 0.14
    elif monto > 200:
        impuesto = 0.12
    elif monto > 50:
        impuesto = 0.1
    else:
        impuesto = 0
        
else:
    print("Este tipo no es valido")
    
print(f"El impuesto a pagar de tipo {tipo} por venta de {monto:,.2f}")
print(f"es de {monto*impuesto:,.2f}")"""

monto = float(input("Digite el monto: "))
tipo = input("Ingrese el tipo (Local/Exportación)")
impuesto = 0

if tipo.lower() == "local":
    if monto > 500:
        print(f"El impuesto a pagar {monto*0.10:,.2f}")
    else:
        if monto > 200:
            impuesto = 0.08
        else: 
            if monto > 50:
                impuesto = 0.06
            else:
                impuesto = 0
                #h¿copiar y pegar 