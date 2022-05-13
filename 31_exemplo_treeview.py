from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *


def mostrar_selecionado():
    try:
        index = dataset.selection()[0]
        valores = dataset.item(index, 'values')
    except IndexError:
        messagebox.showwarning("Alerta", "Selecione um item.")
        return

    print(valores)


root = Tk()
root.title('Exemplo ThreeView')

columns = ['id', 'nome', 'telefone']

values = [
    ['0', 'Rodolfo', '2422516300'],
    ['1', 'Guilherme', '2422516301'],
    ['2', 'Matheus', '2422516302']
]

# show = ['tree', 'headings', 'tree headings', '']
dataset = Treeview(root, columns=columns, show='headings')

btn_mostrar = Button(
    root, text="Mostrar Selecionado",
    command=mostrar_selecionado
)

# Define as colunas
dataset.column('id')
dataset.column('nome')
dataset.column('telefone')

# Define os cabeçalhos
dataset.heading('id', text="ID")
dataset.heading('nome', text="NOME")
dataset.heading('telefone', text="TELEFONE")

# Inserindo valores
dataset.insert('', index=END, values=values[0])
dataset.insert('', index=END, values=values[1])
dataset.insert('', index=END, values=values[2])

dataset.pack()
btn_mostrar.pack()

root.mainloop()
