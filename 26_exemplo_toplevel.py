from tkinter import *


def abrir_formulario():
    # Top Level - Janela secundaria
    top = Toplevel()
    top.title("Formulario")
    top.geometry("200x200")
    lb1 = Label(top, text="Label Outra Janela")
    lb1.pack()


root = Tk()
root.title('Exemplo TopLevel')
root.geometry("200x200")

btn = Button(root, text="Novo", command=abrir_formulario)
btn.pack()


root.mainloop()
