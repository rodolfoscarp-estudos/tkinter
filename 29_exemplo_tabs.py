from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Exemplo Abas')

root.geometry('500x300')

# notebook é o elemnto pai das abas
nb = ttk.Notebook(root, width=500, height=300)

# Cria os frames
tb1 = Frame(nb)
tb2 = Frame(nb)

# Adiciona os frames ao notbook
nb.add(tb1, text="Aba 1")
nb.add(tb2, text="Aba 2")

# Elementos da aba 1
label1 = Label(tb1, text="Esta label pertence a Aba 1.")
label1.pack()

# Elementos da aba 2
label2 = Label(tb2, text="Esta label pertence a Aba 2.")
label2.pack()


nb.pack()

root.mainloop()
