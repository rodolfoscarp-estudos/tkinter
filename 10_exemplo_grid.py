from tkinter import *

window = Tk()
window.title('Grid')

label_1 = Label(
    window,
    text="Label1",
    font="tahoma 30",
    bg='red'
)

label_2 = Label(
    window,
    text="Label2",
    font="tahoma 30",
    bg='blue'
)

label_3 = Label(
    window,
    text="Label3",
    font="tahoma 30",
    bg='cyan'
)

button = Button(
    text="Botão1",
    font='tahoma 25'
)

label_1.grid(row=0, column=0)
label_2.grid(row=1, column=1)
label_3.grid(row=2, column=1)
button.grid(row=3, column=0)

window.mainloop()
