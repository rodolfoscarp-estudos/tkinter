from pathlib import Path
from tkinter import *


root = Tk()
root.title('Adicionar Imagem')

img = PhotoImage(file='assets/icon.png')

image1 = Label(root, image=img).grid()
Label(root, text="Home").grid()

root.mainloop()
