# Pidiendo el nombre de usuario
while True:
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

    import random
    B=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80]

    while True:
        for i in range(1):
            C=random.choice(B)
            B.remove(C)

            D=[]
            D.append(C)
            print(C)
            
            print("¿Deseas continuar?: ")
            m=input()
        if m=="no":
            break
    print(D)
    
     
