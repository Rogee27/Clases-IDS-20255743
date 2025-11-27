# Este modulo va a contener funciones

# Una función tiene 2 tiempos, una definición y una llamada

# Vamos a definir una función
def mi_funcion ():
    """Esta función imprime un saludo"""
    print("Hola mundo")
    print("amigo susuario")
    print("gracias por usar nuestro sistema!")

# Vamos a recibir información desde afuera de la función
def captar_nombre():
    """Esta función recibe valores por medio de input"""
    nombre_input = input("Escriba su nombre: ")
    apellido_input = input("Digite su apellido: ")
    nombre_completo = f"{nombre_input.capitalize()} {apellido_input.capitalize()}"
    print(nombre_completo)

"""def capturar_usuario():
    nombre_usuario = input()
    edad_usuario = int(input())
    texto = f"El usuario {nombre_usuario.title()} tiene {edad_usuario} años de edad."
    print(texto)"""
def capturar_usuario(nombre, edad):
    """Esta función recibe valores por medio de argumentos"""
    nombre_usuario = nombre
    edad_usuario = edad
    texto = f"El usuario {nombre_usuario.title()} tiene {edad_usuario} años de edad."
    print(texto)

# Llamando la función capturar_nombre()
"""capturar_usuario("ROGELIO RIVERA", 19)"""
"""capturar_usuario(input("Ingrese su nombre: "), input("Edad: "))"""

#Función que devuelve un valor
def calculo_impuesto(ventas):
    """Esta es una función que calcula el valor del impuesto"""
    if ventas < 500:
        tasa_impuesto = 0.1
    else:
        tasa_impuesto = 0.25
    return tasa_impuesto
ventas = 100
# Aquí vamos a llamra a la función 
tasa_calculada = calculo_impuesto(ventas)
monto_impuesto =calculo_impuesto(ventas)*ventas
print(f"""El valor de la venta fue de ${ventas:,.2f},
      la tasa de impuesto es {tasa_calculada:.2f},
      y el monto por tanto es ${monto_impuesto:,.2f}""")