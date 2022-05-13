from tkinter import *


def printar():
    print(selected.get())


root = Tk()
root.title("Exemplo OptionMenu")

options = ['Guilherme', 'Rodolfo', 'Matheus']

selected = StringVar()
selected.set(options[0])

label = Label(root, text="Nomes")
opt_menu = OptionMenu(root, selected, *options)
btn = Button(root, text="Printar", command=printar)

label.pack()
opt_menu.pack()
btn.pack()

root.mainloop()
