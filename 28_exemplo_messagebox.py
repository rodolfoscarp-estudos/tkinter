from tkinter import *
from tkinter import messagebox


def show_msg(tipo: str):

    if tipo == 'info':
        messagebox.showinfo(
            "Info", "Mensagem de Informação!"
        )

    if tipo == 'alert':
        messagebox.showwarning(
            "Alerta", "Mensagem de Alerta!"
        )

    if tipo == 'error':
        messagebox.showerror(
            "Erro", "Mensagem de Erro!"
        )


root = Tk()

tipo_mensagem = ['info', 'alert', 'error']

opt = StringVar()
opt.set(tipo_mensagem[0])

label = Label(root, text="Tipo de Mensagem: ")
opt_menu = OptionMenu(root, opt, *tipo_mensagem)
btn = Button(root, text="Mostrar alerta!", command=lambda: show_msg(opt.get()))

label.grid(row=0, column=0)
opt_menu.grid(row=0, column=1)
btn.grid(row=1, column=0, columnspan=2, sticky=W)

root.mainloop()
