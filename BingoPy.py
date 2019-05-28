# Pidiendo el nombre de usuario
n = int(input("¿Cuántos jugarán?: "))
j=[]
for i in range (n):
    nombre=input("Nombre de jugador: ")
    cartilla=int(input("¿Cuántas cartillas escogerá?: "))
    j[0][0].append(nombre)
    j[0][1].append(cartilla)
print(j)