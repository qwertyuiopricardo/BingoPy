n = int(input("¿Cuántos jugarán?: "))
j=[]
N=[]
pozo = 0
suma = 0
for i in range (n):
    nombre=input("Nombre de jugador: ")
    cartilla=int(input("¿Cuántas cartillas escogerá?: "))  
    N.append(cartilla)
    m=[]
    m.append(nombre)
    m.append(cartilla)
    j.append(m)

for i in (N):
    suma=suma+i

pozo = suma*5

print(j)
print("El pozo es de: ", pozo, "soles")


B = []
import random
for i in range(80):
    B.append(i)

C = []
while len(C)<=15:
    random.shuffle(B)
    B.remove(B[0])
    C.append(B[0])

print(C)
print("El juego ha finalizado")
