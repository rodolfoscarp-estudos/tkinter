from tkinter import *
from tkinter import filedialog


root = Tk()
root.title("Exemplo Dialog")

# Retorna um file modo leitura
file = filedialog.askopenfile(
    mode='r', parent=root, filetypes=(("Arquivo Python", '*.py'),)
)

try:
    print(file.read())
    file.close()
except AttributeError as e:
    print(e)


# Retorna um file modo escrita
file = filedialog.asksaveasfile(
    mode='w', parent=root, filetypes=(("Arquivo Texto", '*.txt'),))

try:
    print(file.write("Teste"))
    file.close()
except AttributeError as e:
    print(e)

root.mainloop()
