from tkinter import *
from tkinter import simpledialog


def show_dialog(tipo: str):
    if tipo == 'string':
        valor = simpledialog.askstring('String', 'Digite um String: ')
    elif tipo == 'float':
        valor = simpledialog.askfloat('Float', 'Digite um Float: ')
    elif tipo == 'int':
        valor = simpledialog.askinteger('Integer', 'Digite um Inteiro: ')

    print(f'`{type(valor)}` : {valor}')


root = Tk()
root.title("Exemplo Dialog")

tipo_dialogo_value = StringVar()
tipo_dialogo_options = ['string', 'float', 'int']
tipo_dialogo_value.set(tipo_dialogo_options[0])

label_tipo_dialogo = Label(root, text="Selecione o tipo de dialogo: ")
tipo_dialogo = OptionMenu(root, tipo_dialogo_value, *tipo_dialogo_options)

btn = Button(
    root, text='Abrir Dialogo',
    command=lambda: show_dialog(tipo_dialogo_value.get())
)

label = Label(root, text='')

label_tipo_dialogo.grid(row=0, column=0)
tipo_dialogo.grid(row=0, column=1)

btn.grid(row=1, column=0)
label.grid(row=1, column=1)


root.mainloop()
