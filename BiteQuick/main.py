"""
El módulo main.py conecta los demás módulos del programa. En este módulo se 
definen las listas principales que se enviarán a las funciones de los otros 
módulos. Además, incluye dos usuarios predefinidos con rol de administrador. 
En main también se gestionan los menús tanto del administrador como del cliente.
"""

from autenticacion import crear_cuenta, iniciar_sesion
from cliente import ver_menu, hacer_pedido, ver_historial_cliente
from admin import registrar_plato, ver_pedidos_admin, eliminar_menu

menu = []
pedidos = []
historial_clientes = []
lista_usuarios = []
# Estos son usuarios ya creados, para iniciar sesión con admin
lista_usuarios.extend([
    {
        "nombre_usuario": "admin1",
        "apellido_usuario": "admin1",
        "carnet_usuario": "001",
        "correo_usuario": "admin1@gmail.com",
        "contrasena_usuario": "12345",
        "rol_usuario": "admin"
    },
    {
        "nombre_usuario": "admin2",
        "apellido_usuario": "admin2",
        "carnet_usuario": "002",
        "correo_usuario": "admin2@gmail.com",
        "contrasena_usuario": "12345",
        "rol_usuario": "admin"
    }
])

def menu_principal():
    while True:
        print("\n--- BiteQuick ---")
        print("1. Iniciar sesión")
        print("2. Crear cuenta")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            rol, carnet = iniciar_sesion(lista_usuarios)  # la función iniciar sesión devuelve rol de usuario y carnet, que va a servir para registrar el pedido y ver el historial más facil
            if rol == "cliente":
                while True:
                    print("\n--- MENÚ CLIENTE ---")
                    print("1. Ver menú del día")
                    print("2. Hacer pedido")
                    print("3. Ver historial personal")
                    print("4. Cerrar sesión")
                    opcion_cliente = input("Seleccione una opción: ")

                    if opcion_cliente == "1":
                        ver_menu(menu)
                    elif opcion_cliente == "2":
                        hacer_pedido(menu, pedidos, carnet, historial_clientes)
                    elif opcion_cliente == "3":
                        ver_historial_cliente(historial_clientes, carnet)
                    elif opcion_cliente == "4":
                        print("Cerrando sesión de cliente...")
                        carnet = None # Como cerro sesión hay que borrar el carnet guardado
                        break 
                    else:
                        print("Opción inválida.")
            elif rol == "admin":
                while True:
                    print("\n--- MENÚ ADMIN ---")
                    print("1. Agregar nuevo plato al menú del día")
                    print("2. Ver pedidos del día")
                    print("3. Eliminar menú del dia")
                    print("4. Cerrar sesión")
                    opcion_admin = input("Seleccione una opción: ")

                    if opcion_admin == "1":
                        registrar_plato(menu)
                    elif opcion_admin == "2":
                        ver_pedidos_admin(pedidos)
                    elif opcion_admin == "3":
                        eliminar_menu(menu)
                    elif opcion_admin == "4":
                        print("Cerrando sesión de admin...")
                        break
                    else:
                        print("Opción inválida.")
        elif opcion == "2":
            crear_cuenta(lista_usuarios)

        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


menu_principal()