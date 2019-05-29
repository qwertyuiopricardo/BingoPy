n = int(input("¿Cuántos jugarán?: "))
j=[]
for i in range (n):
    nombre=input("Nombre de jugador: ")
    cartilla=int(input("¿Cuántas cartillas escogerá?: "))

    N=[]
    N.append(cartilla)
    pozo = 0
    if len(N) >=1:
        pozo=pozo*5
        
        print(N)
        
    else:
        print("No puede acceder al pozo")


    m=[]
    m.append(nombre)
    m.append(cartilla)
    j.append(m)
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
