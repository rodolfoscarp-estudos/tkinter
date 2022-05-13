from tkinter import *
from tkinter.ttk import *


# Funções


def deletar():
    # Elimina o primeiro e o segundo item
    lista.delete(first=0, last=0)


def deletar_tudo():
    # Limpa todos os itens
    lista.delete(0, END)


# GUI
root = Tk()
root.title("Exemplo ListBox")

# Widgets

# selectmode=EXTENDED indica que podera ser selecionado varios itens
lista = Listbox(
    root,
    selectmode=EXTENDED
)

cmd = Button(root, text="Deletar", command=deletar)
cmd2 = Button(root, text="Deletar Tudo", command=deletar_tudo)

# Layout
lista.pack()
cmd.pack()
cmd2.pack()

# Inserir um item
# Use a constant do TK END para colocar por ultimo
lista.insert(0, "Rodolfo")
lista.insert(END, "Scarp")
lista.insert(END, "Costa")

root.mainloop()
