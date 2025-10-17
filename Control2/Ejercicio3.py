correo = input()
print(f"Contiene exactamente un @: {correo.count('@')==1}")
print(f"El @ no está ubicado al inicio del correo: {correo[0] is not '@'}")
print(f"El @ no está ubicado al final del correo: {correo[-1] is not '@'}")