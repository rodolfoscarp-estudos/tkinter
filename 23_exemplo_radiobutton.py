from tkinter import *

# Funções


def exibir():
    t = f'Opção A: {valor_a.get()} - Opção B: {valor_b.get()}'
    label['text'] = t


# GUI
root = Tk()
root.title("Exemplo Radiobutton")

valor_a = IntVar()
valor_b = IntVar()

# Widget
ra_1 = Radiobutton(root, text='Opção A 1', variable=valor_a, value=1)
ra_2 = Radiobutton(root, text='Opção A 2', variable=valor_a, value=2)
ra_3 = Radiobutton(root, text='Opção A 3', variable=valor_a, value=3)

# indicatoron=0 dá um aspecto de botão
rb_1 = Radiobutton(
    root, text='Opção B 1',
    variable=valor_b, value=1, indicatoron=0)
rb_2 = Radiobutton(
    root, text='Opção B 2',
    variable=valor_b, value=2, indicatoron=0)
rb_3 = Radiobutton(
    root, text='Opção B 3',
    variable=valor_b, value=3, indicatoron=0)

ra_1.select()
rb_1.select()

btn = Button(root, text="Mostrar", command=exibir)
label = Label(root, text="")

# Layout
ra_1.grid(row=0, column=0)
ra_2.grid(row=0, column=1)
ra_3.grid(row=0, column=2)

rb_1.grid(row=1, column=0)
rb_2.grid(row=1, column=1)
rb_3.grid(row=1, column=2)

btn.grid(row=2, column=0)
label.grid(row=2, column=1, columnspan=2, sticky=W)

root.mainloop()
