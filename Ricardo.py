# Pidiendo el nombre de usuario
while True:
    import time
    def timer(n):
        while n!=0:
            n=n-1
            time.sleep(n)#time.sleep(seconds) #here you can mention seconds according to your requirement.
            
    
    n = int(input("¿Cuántos jugarán?: "))
    j=[]
    N=[]
    for i in range (n):
        nombre=input("Nombre de jugador: ")
        cartilla=int(input("¿Cuántas cartillas escogerá?: "))
        N.append(cartilla)
        m=[]
        m.append(nombre)
        m.append(cartilla)
        j.append(m)
    print(j)
    
    suma=0
    for i in N:
        suma = suma + i

    suma2 = 0
    suma2 = suma*5
    print("El pozo es: ",suma2)
    
    import random
    B=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80]

    while True:
        for i in range(1):
            C=random.choice(B)
            B.remove(C)

            D=[]
            D.append(C)
            print(C)     
            
            timer(4)
    
            m=input("¿Deseas continuar?: ")
        if m=="no":
            break
     
    reinicio=input("¿Desea reiniciar el juego?: ")
    if reinicio=="no":
        break
    print(D)
    
     
