#Ejercicio 1

from Tkinter import *
root = Tk()
etiqueta1= Label(root, text="Hello Tkinter!")
etiqueta1.pack()
root.mainloop()


#Ejercicio2

from Tkinter import *
master = Tk()
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it. \n(Mahatma Gandhi)"
msg = Message(master, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack( )
mainloop( )
