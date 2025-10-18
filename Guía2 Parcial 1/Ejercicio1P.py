correo = input()
posicion_arroba = correo.index("@")
condicion1 = correo.count("@")==1
condicion2_1 = posicion_arroba>= 3
condicion2_2 = (len(correo)-posicion_arroba)> 3
condicion3 = correo.count(".")>= 1
condicion4 = correo.count(" ")== 0
condicion5_1 = correo[0] != "."
condicion5_2 = correo[-1] != "."
print(condicion1 and condicion2_1 and condicion2_2 and condicion3 and condicion4 and condicion5_1 and condicion5_2)
