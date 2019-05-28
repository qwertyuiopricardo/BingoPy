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
