# -*- encoding: utf-8 -*-
from Tkinter import *  #Importamos el módulo para la interfaz

ventana = Tk() #creamos la ventana principal
ventana.title('Analizador Léxico')
ventana.geometry("600x500") #tamaño de la ventana
label1 = Label(ventana, text="Ingresa la cadena:")
label1.grid(row=1,column=1)
label2 = Label(ventana, text="Tokens encontrados")
label2.grid(row=1,column=2)
text1 = Text(ventana,width=40,height=4)
text1.grid(row=2,column=1)
text2 = Text(ventana,width=40,height=4)
text2.grid(row=2,column=2)
boton = Button(ventana, text="Procesa")
boton.grid(row=4,column=1)
ventana.mainloop() #evento que llama al inicio del programa