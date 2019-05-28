# Pidiendo el nombre de usuario
n = int(input("¿Cuántos jugarán?: "))
j=[]
for i in range (n):
    nombre=input("Nombre de jugador: ")
    cartilla=int(input("¿Cuántas cartillas escogerá?: "))
    m=[]
    m.append(nombre)
    m.append(cartilla)
    j.append(m)
print(j)

Pozo = len(cartilla)

B = []
import random
for i in random.randint(1,81):
    B.append(i)
    print(B)

if B == 15:
    Pozo = Pozo*5
else:
    print("Faltan números en cartilla")

print(Pozo)

