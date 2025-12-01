# Vamos a crear una función utilizando kwargg     *args = listas, **kwargs= diccionarios

def registro_profesores (nombre, apellido, **materias):
    """Crear un registro de profesor, utilizando kwargs"""
    print(f"El profesor {nombre} {apellido} imparte las materias: ")
    for ciclo, materias in materias.items():
        print(f"\t - {ciclo}: \t {materias}")

registro_profesores(
    "Rogelio",
    "Rivera",
    Ciclo1 = ["BD1", "IIJ", "AYGD"],
    Ciclo2 = ["DAI", "BD2", "SINE"],
    Ciclo3 = ["ISD", "FPEN", "PAD"]
)