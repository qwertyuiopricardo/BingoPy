# Definiendo tiempo de espera después de cada bolilla
while True:
    import time
    def timer(n):
        while n!=0:
            n=n-1
            time.sleep(n)#time.sleep(seconds) #here you can mention seconds according to your requirement.
            
# Preguntar cuantos jugadores hay  
    n = int(input("¿Cuántos jugarán?: "))
    j=[]
    N=[]
    for i in range (n):
        nombre=input("Nombre de jugador: ")
        cartilla=int(input("¿Cuántas cartillas escogerá?: "))
        while cartilla>3:
            cartilla = int(input("Seleccione número válido de cartillas: "))
            if cartilla <= 3:
                break
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
    
    
    import random
    B = []

    for i in range(1,81):
        B.append(i)
        
    while True:
        for i in range(15):
            A = []
            C = random.choice(B)
            A.append(C)
            B.remove(C)
            print(A)

        for i in range(15):
            
            #D=[]
            #D.append(C)
            print("Bolilla n° ",C)     
            
            timer(4)
    
        m=input("¿Deseas continuar?: ")
        if m=="no":
            break
        ganador = input("¿Conforme?")
        if ganador == "si":
            break
     
    reinicio=input("¿Desea reiniciar el juego?: ")
    if reinicio=="no":
        
        print("El juego ha finalizado")
        
        break
    
    



print("El pozo es:",suma2)


 
       