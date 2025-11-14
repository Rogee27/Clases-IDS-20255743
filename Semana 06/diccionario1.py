"""mi_mascota = {"tipo":"perro",
              "nombre":"Phoenix",
              "edad": 4,
              "personalidad": "cariñosa(Davo)"}

print(type(mi_mascota))
#{tipo, nombre, edad, personalidad}"""

'''mi_mascota = {"tipo":"perro",
              "nombre":"Phoenix",
              "edad": 4 ,
              "personalidad":"amigable"}
rivera_mascota= {
    "edad": 4,
    "nombre": "Phoenix",
    "personalidad": "amigable",
    "tipo":"perro"
}

mascotass= mi_mascota == rivera_mascota
print(mascotass)'''

birthdays = {
    "Alice":"abril 1",
    "Bob":"diciembre 2",
    "Caro": "Marzo 4"
}
birthdays["Bob"] = "septiembre 2"
print(birthdays["Bob"])
birthdays["Pau"]= "julio 31"
print(birthdays)
del birthdays["Bob"]
print(birthdays)

for person, date in birthdays.items():
    print(f"El cumpleaños de {person} es el día {date}.")