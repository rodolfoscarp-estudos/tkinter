from tkinter import *


# Meu Widget Personalizado
class FrameNome(Frame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self['height'] = 150
        self['width'] = 200
        self['bd'] = 2
        self['relief'] = SOLID

        label_nome = Label(self, text='Nome: ')
        text_nome = Entry(self)
        label_nome.grid(column=0, row=0)
        text_nome.grid(column=1, row=0)


# GUI
root = Tk()
root.title("Widget Personalizado")

# Widget
frame1 = FrameNome(root).grid()
frame2 = FrameNome(root).grid()
frame3 = FrameNome(root).grid()
frame4 = FrameNome(root).grid()

root.mainloop()
