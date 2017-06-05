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
