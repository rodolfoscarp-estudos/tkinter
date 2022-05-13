from tkinter import *

window = Tk()
window.title("Variaveis")

# A classe StringVar cria um objeto para guardar um texto
# que pode servir com estado de um widget
texto = StringVar()
texto.set("Meu Texto")

# a propriedade textvariable fica ligada a variavel texto
# e quando for alterada todas as referencias tambèm são
label = Label(
    window,
    textvariable=texto,
    font="tahoma 20",
    bg="#FF00FF"
).pack()


label_2 = Label(
    window,
    textvariable=texto,
    font="tahoma 20",
    bg="#FF00FF"
).pack()

label_3 = Label(
    window,
    textvariable=texto,
    font="tahoma 20",
    bg="#FF00FF"
).pack()

button = Button(
    window,
    text="Mudar",
    command=lambda: texto.set("Mudou")
).pack()

window.mainloop()
