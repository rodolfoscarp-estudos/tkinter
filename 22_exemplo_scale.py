from tkinter import *


def ver_valor(v):
    print(v)


def ver_valor_2():
    print(slide.get())


def ver_valor_3():
    print(slide_value.get())


root = Tk()
root.title("Exemplo Scale")
root.geometry('300x200')

slide_value = DoubleVar()

slide = Scale(
    root,
    from_=0, to=200, variable=slide_value,
    orient=HORIZONTAL, resolution=0.5,
    command=ver_valor
)

slide.pack()

btn = Button(
    root, text="Ver Valor 2",
    command=ver_valor_2
).pack()

btn2 = Button(
    root, text="Ver Valor 3",
    command=ver_valor_3
).pack()


root.mainloop()
