from tkinter import *

# Funções


def apresentar():
    print(bool(valor_check.get()))


# GUI
root = Tk()
root.title("Exemplo CheckButton")

valor_check = IntVar()

# Widgets

check = Checkbutton(
    root,
    text="CheckButton",
    variable=valor_check,
    command=apresentar
).pack()


# Layout


root.mainloop()
