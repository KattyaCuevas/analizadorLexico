# -*- encoding: utf-8 -*-
from Tkinter import *  #Importamos el módulo para la interfaz

ventana = Tk() #creamos la ventana principal
ventana.title('Analizador Léxico')
ventana.geometry("500x500") #tamaño de la ventana
label = Label(ventana, text="		")
label.grid(row=1,column=1)
label1 = Label(ventana, text="Ingresa la cadena:")
label1.grid(row=1,column=2)
label2 = Label(ventana, text="		")
label2.grid(row=1,column=3)
label3 = Label(ventana, text="Tokens encontrados")
label3.grid(row=1,column=4)
#text1 = Text(ventana)
#text1.grid(row=2,column=1-2)
boton = Button(ventana, text="Procesa")
boton.grid(row=4,column=4)
ventana.mainloop() #evento que llama al inicio del programa