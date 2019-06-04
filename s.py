from tkinter import *


def uno():
	'''
	Regresa "SI" o "NO"
	'''
    r = mb.askquestion("Pregunta!", "¿Deseas reiniciar el juego?")
    Label(root,text=r).pack()

def dos():
	'''
	Regresa "SI" o "NO"
	'''
    r = mb.askquestion("Pregunta!", "¿Deseas finalizar el juego?")
    Label(root,text=r).pack()


	
    root = Tk()
    root.geometry("300x300+500+300") 
    root.title("Ventanas Emergentes")
    root.config( bd=10)


    Button(root,text="Reiniciar Juego", command=uno).pack()
    Button(root,text="Finalizar Juego",command=dos).pack()

root.mainloop()