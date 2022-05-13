from tkinter import *

root = Tk()
root.title('Exemplo Message')

# Semelhante ao Label mas,
# Se adapta ao texto, quebrando linha
# e utilizando o tamanho do texto se width for maior

t = Message(
    root,
    text="Este é o texto do message widget.",
    width=800
)
t.pack()

root.mainloop()
