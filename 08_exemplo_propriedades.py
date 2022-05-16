from tkinter import *

window = Tk()
window.title("Alterar Propriedade")

label_1 = Label(
    window,
    text="Minha Label",
    bd=1,
    relief='solid',
    font="Courier 16 bold",
    width=30,
    height=3,
)

label_1.pack()

# As propriedades também podem ser atribuidas no formato de dicionario

label_2 = Label(window)
label_2['text'] = 'Minha Label 2'
label_2['bd'] = 1
label_2['relief'] = 'solid'
label_2['width'] = 20
label_2['height'] = 3
label_2['font'] = 'Courier 16 bold'

label_2.pack()

# As propriedades podem ser acessadas também como um dicionario

print(label_2['text'])

# As propriedades podem ser reatribuidos após o pack
# Se estiver no mesmo escopo

label_2['text'] = 'Novo Texto'

#
print(label_2.keys())

window.mainloop()
