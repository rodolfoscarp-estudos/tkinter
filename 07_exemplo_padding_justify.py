from tkinter import *

"""
justify:
CENTER
LEFT
RIGHT
"""

window = Tk()
window.title = 'Exmplo Alinhamento'

window.resizable(width=False, height=False)


label_1 = Label(
    window,
    text="Texo Justificado\nà direita",
    border=2,
    font="Arial 15",
    relief='solid',
    padx=50,
    pady=50,
    justify=RIGHT
).pack()

label_2 = Label(
    window,
    text="Texo Justificado\nà esquerda",
    border=2,
    font="Arial 15",
    relief='solid',
    padx=50,
    pady=50,
    justify=LEFT
).pack()

label_3 = Label(
    window,
    text="Texo Justificado\nao centro",
    border=2,
    font="Arial 15",
    relief='solid',
    padx=50,
    pady=50,
    justify=CENTER
).pack()

window.mainloop()
