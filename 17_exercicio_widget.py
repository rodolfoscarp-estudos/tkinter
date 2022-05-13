from tkinter import *


class MinhaFrame(Frame):
    def __init__(self, parent):
        super().__init__()

        # Estados
        self.text1_text = StringVar()
        self.label1_text = StringVar()

        # Widgets
        self.label1 = Label(self, textvariable=self.label1_text).grid()
        text1 = Entry(self, textvariable=self.text1_text).grid()
        botao1 = Button(self, text="Clique", command=self.executar).grid()

    def executar(self):
        self.label1_text.set(f"Olá {self.text1_text.get()}!")


root = Tk()
root.title("Exercício Widget")
root.geometry('300x150')

# widgets
frame1 = MinhaFrame(root).grid()
frame2 = MinhaFrame(root).grid()

root.mainloop()
