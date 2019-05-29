while True:
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
    print(j)

    for i in N:
        suma = suma + i

    suma2 = 0
    suma2 = suma*5
    print("El pozo es: ",suma2)
    
    B = []
    import random
    for i in range(1,81):
        B.append(i)

    C = []
    while len(C)<=15:
        random.shuffle(B)
        B.remove(B[0])
        C.append(B[0])

    print(C)
    print("Again")