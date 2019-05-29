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

B = []
import random
for i in range(80):
    B.append(i)

C = []
random.shuffle(B)
B.remove(B[0])
C.append(B[0])
print(C)




