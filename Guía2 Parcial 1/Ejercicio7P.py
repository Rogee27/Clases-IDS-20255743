nom = input()
ape = input()
nick = (nom[:5]+ ape[0]).lower()
print(f"Nick: {nick}")
pin = (len(nom)*1000 + len(ape)) % 10000
print(f"Pin: {pin}")
print(f"ID: C3-{nick}-{pin}")