from tkinter import *

root = Tk()
root.config(bd=20)

choco = IntVar()
fruta = IntVar()


def seleccionar():
    cadena = ''
    if choco.get():
        cadena += ' Con salsa de chocolate'
    else:
        cadena += ' Sin salsa de chocolate'

    if fruta.get():
        cadena += ' con frutas'
    else:
        cadena += ' sin frutas'
    etiqueta1.config(text=cadena)


imagen = PhotoImage(file='helado.gif')
Label(root, image=imagen).pack(side=LEFT)

marco1 = Frame(root)
marco1.pack(side=LEFT)

Label(marco1, text='Cómo quieres el helado?').pack(anchor='w')
Checkbutton(marco1, text='Con salsa de chocolate', variable=choco, onvalue=1, offvalue=0, command=seleccionar).pack(
    anchor='w')
Checkbutton(marco1, text='Con frutas', variable=fruta, onvalue=1, offvalue=0, command=seleccionar).pack(anchor='w')

etiqueta1 = Label(marco1)
etiqueta1.pack()

root.mainloop()