from tkinter import *

window = Tk()
window.title("Exemplo Label")

window.geometry('300x300')

# Definição dos components
label_1 = Label(window, text='Label 1')
button_1 = Button(window, text="Botão 1")

label_2 = Label(window, text='Label 2')
button_2 = Button(window, text="Botão 2")

# A ordem em que os elementos são desenhados na janela
# É a ordem m que os packs são executados
label_2.pack()
button_2.pack()

label_1.pack()
button_1.pack()


window.mainloop()
