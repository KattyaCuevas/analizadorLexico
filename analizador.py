# -*- encoding: utf-8 -*-
from Tkinter import *  #Importamos el módulo para la interfaz

ventana = Tk() #creamos la ventana principal
ventana.config(bg="gray") #cambiamos el color
#ventana.geometry("500x500") #tamaño de la ventana

frame = Frame(ventana)
frame.pack()

label = Label(frame, text="Hola mundo")
text = Text(frame)
c1 = Checkbutton(frame, text="Uno")
c2 = Checkbutton(frame, text="Dos")
entry = Entry(frame)
button = Button(frame, text="Aceptar")
button.pack()
ventana2=Toplevel(ventana)
ventana2.withdraw()

label.pack()
c1.pack()
entry.pack()
button.pack()

ventana.mainloop() #evento que llama al inicio del programa