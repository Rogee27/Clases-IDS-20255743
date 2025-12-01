
# Otro modulo para comprender las funciones

# Definimos la función
def describir_mascota(nombre_mascota: str, tipo_animal: str="perro"):
    """Esta función describre una mascota, por defecto perro"""
    print(f"Mi mascota se llama {nombre_mascota.capitalize()}")
    print(f"y es un tipo de animal {tipo_animal.lower()}.")

# Llamamos a la función
#describir_mascota(nombre_mascota="phoenix",tipo_animal= "perro")
#describir_mascota("gato", "misifus")

def registro_usuarios(nombre, apellido, inicial = "", edad = 0):
    """Construir un nombre a partir de sus componentes"""
    if edad:
        texto_completo = f"La persona {nombre} {inicial} {apellido}, de {edad} años de edad."
    else:
        texto_completo = f"La persona {nombre} {inicial} {apellido}."
    return texto_completo

#print(registro_usuarios("Daniel", "Wisecarver"))

# Definimos una función que es usada por una lista
def saludar_usuario(nombres):
    """"Saludará usuario"""
    for nombre in nombres:
        print(f"Hola, {nombre.capitalize()}")
usuarios = ["Vecna", "Once", "Erika"]
saludar_usuario(usuarios)
