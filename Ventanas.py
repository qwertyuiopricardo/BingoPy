from tkinter import *
from tkinter import messagebox as mb
from tkinter import colorchooser
from tkinter import filedialog

def Reinicio():
	'''
	Regresa 'SI' o 'NO'
	'''
	r = mb.askyesno("Pregunta!", "¿Deseas reiniciar el juego?")
	Label(root,text=r).pack()

def Cierre():
	'''
	Regresa 'SI' o 'NO'
	'''
	r = mb.askquestion("Pregunta!", "¿Deseas finalizar el juego?")
	Label(root,text=r).pack()

	
def guardar():
	'''
	Regresa la ruta absoluta del archivo modo de apertura = w y la codificación (juego de caracteres)
	'''
	fichero = filedialog.asksaveasfile(title="Guardar",mode="w+",defaultextension=".py",filetypes = (("Fichero texto","*.txt"),("Fichero PDF","*.pdf"),("Todos los ficheros","*.*")))
	if fichero is not None:
		fichero.write("print('Hola Mundo - Creado desde el GUI')\n")
		fichero.write("input('ctrl+z para salir')")
		fichero.close()
	Label(root,text=fichero).pack()	
	
root = Tk()
root.geometry("300x300+500+300") # +500+300 es para indicar en que parte de la pantalla se ubicara
root.title("Crear Pop-Up")
root.config(bd=10)


Button(root,text="Reiniciar", command=Reinicio).pack()
Button(root,text="Finalizar",command=Cierre).pack()
Button(root,text="Guardar", command=guardar).pack()

root.mainloop()