from tkinter import *

"""
Anchor:
|------------------|
| NW |   N    | NE |
|----|--------|----|
| W  | CENTER |  E |
|----|--------|----|
| SW |    S   | SE |
|------------------|

N = Norte
S = Sul
W = Oeste
E = Leste

"""

window = Tk()
window.title = 'Exmplo Alinhamento'

window.resizable(width=False, height=False)


label_1 = Label(
    window,
    text="Noroeste - NW",
    width=30,
    height=3,
    border=2,
    font="Arial 15",
    relief='solid',
    anchor=NW
).pack()

label_2 = Label(
    window,
    text="Norte - N",
    width=30,
    height=3,
    border=2,
    font="Arial 15",
    relief='solid',
    anchor=N
).pack()

label_3 = Label(
    window,
    text="Nordeste - NE",
    width=30,
    height=3,
    border=2,
    font="Arial 15",
    relief='solid',
    anchor=NE
).pack()

label_4 = Label(
    window,
    text="Oeste - W",
    width=30,
    height=3,
    border=2,
    font="Arial 15",
    relief='solid',
    anchor=W
).pack()

label_5 = Label(
    window,
    text="Center - CENTER",
    width=30,
    height=3,
    border=2,
    font="Arial 15",
    relief='solid',
    anchor=CENTER
).pack()

label_6 = Label(
    window,
    text="Leste - E",
    width=30,
    height=3,
    border=2,
    font="Arial 15",
    relief='solid',
    anchor=E
).pack()

label_7 = Label(
    window,
    text="Sudoeste - SW",
    width=30,
    height=3,
    border=2,
    font="Arial 15",
    relief='solid',
    anchor=SW
).pack()

label_8 = Label(
    window,
    text="Sul - S",
    width=30,
    height=3,
    border=2,
    font="Arial 15",
    relief='solid',
    anchor=S
).pack()

label_9 = Label(
    window,
    text="Sudeste - SE",
    width=30,
    height=3,
    border=2,
    font="Arial 15",
    relief='solid',
    anchor=SE
).pack()

window.mainloop()
