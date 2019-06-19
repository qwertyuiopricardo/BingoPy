# Definiendo tiempo de espera después de cada bolill
import random
B=[]
for i in range(1,81):
    B.append(i)

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
    
    
    D=[]
    while True:
        for i in range(1):
            C=random.choice(B)
            B.remove(C)

            
            
            print("Bolilla n° ",C) 

            
            D.append(C)
            
            
            timer(4)
        m=input("¿Deseas continuar?: ")
        if m=="no":
            break
        
        
        

    print(D)     
    ganador = input("¿Conforme?")
    if ganador == "si":
        print("Tenemos un ganador. ¡FELICIDADES!")
        suma2 = 0
        suma2 = suma*5
        print("El pozo es: ",suma2, "soles", "Y usted ganó:",suma2, "soles")
      

    suma=0
    for i in N:
        suma = suma + i

     
                       
    reinicio=input("¿Desea reiniciar el juego?: ")
    if reinicio=="no":
        
        print("El juego ha finalizado")
        
        break
    