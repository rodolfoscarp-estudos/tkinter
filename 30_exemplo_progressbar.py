from tkinter import *
from tkinter.ttk import *
import time


def carregar():
    bar_value.set(0)

    for i in range(100):
        time.sleep(0.02)
        bar_value.set(i)
        # redesenha a tela
        root.update()


root = Tk()
root.title('Exemplo Barra de Progressao')

bar_value = DoubleVar()
bar_value.set(0)

button = Button(root, text="Carregar", command=carregar)
bar = Progressbar(root, variable=bar_value, maximum=100)

button.pack()
bar.pack()

root.mainloop()
