from tkinter import *


def novo():
    print("Novo")


def abrir():
    print("Abrir")


def salvar():
    print("Salvar")


def editar():
    print("Editar")


root = Tk()
root.title("Menu")

menu_menu = Menu(root)

# Elementos do menu arquivo
file_menu = Menu(menu_menu, tearoff=0)
file_menu.add_command(label="Novo", command=novo)
file_menu.add_command(label="Abrir", command=abrir)
file_menu.add_command(label="Salvar", command=salvar)
file_menu.add_separator()
file_menu.add_command(label="Fechar")

# Elementos do menu principal
menu_menu.add_cascade(label="Arquivo", menu=file_menu)

# Command serve adiciona uma ação
menu_menu.add_command(label="Editar", command=editar)


# Define o menu na janela
root.config(menu=menu_menu)

root.mainloop()
