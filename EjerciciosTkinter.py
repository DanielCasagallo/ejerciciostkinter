#Ejercicio 1

from tkinter import *
root = Tk()
etiqueta1= Label(root, text="Hello Tkinter!")
etiqueta1.pack()
root.mainloop()


#Ejercicio2
master = Tk()
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it. \n(Mahatma Gandhi)"
msg = Message(master, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack( )
mainloop( )

#Ejercicio 3
class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.button = Button(frame, text="SALIR",fg="red",command=frame.quit)
        self.button.pack(side=LEFT)
        self.slogan =Button(frame,text="ENTRAR",command=self.write_slogan)
        self.slogan.pack(side=LEFT)
def write_slogan(self):
    print("Estamos aprendiendo a usar Tkinter!")
    root = Tk()
    app = App(root)
    root.mainloop()

#Ejercicio 4

root = Tk()
v = IntVar()
Label(root,text="""Choose a programming language:""",justify = LEFT,padx = 20).pack()
Radiobutton(root,text="Python",padx = 20,variable=v,value=1).pack(anchor=W)
Radiobutton(root,text="Perl",padx = 20,variable=v,value=2).pack(anchor=W)
mainloop()

#Ejercicio 5
root = Tk()
v = IntVar()
v.set(1)
languages = [("Python",1),("Perl",2),("Java",3),("C++",4),("C",5)]

def ShowChoice():
 print (v.get())
Label(root,text="""Elija su lenguaje de programación favorito:""",justify = LEFT,padx = 20).pack()
for txt, val in languages:
 Radiobutton(root,text=txt,padx = 30,variable=v,command=ShowChoice,value=val).pack(anchor=W)
mainloop()

#Ejercicio 6
root = Tk()
v = IntVar()
v.set(1)
languages = [("Python",1),("Perl",2),("Java",3),("C++",4),("C",5)]
def ShowChoice():
 print (v.get())
Label(root,text="""Escoja un lenguaje de programación:""",justify = LEFT,padx = 20).pack()
for txt, val in languages:
 Radiobutton(root,text=txt,indicatoron =0,width = 20,padx = 20,variable=v,command=ShowChoice,value=val).pack(anchor=W)
mainloop()

#Ejercicio 7

master = Tk()
var1 = IntVar()
Checkbutton(master, text="Hombre", variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text="Mujer", variable=var2).grid(row=1, sticky=W)
mainloop()

#Ejercicio 8

master = Tk()

def var_states():
    print ("male: ",var1.get())
    print ("female: ",var2.get())

Label(master, text="Indicar el sexo:").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(master, text="male", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="female", variable=var2).grid(row=2, sticky=W)
Button(master, text='Quit', command=master.quit).grid(row=3, sticky=W, padx=4)
Button(master, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)
mainloop()

#Ejercicio 9

from Tkinter import *
master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
mainloop()

#Ejercicio 10

from Tkinter import *
def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
mainloop()
