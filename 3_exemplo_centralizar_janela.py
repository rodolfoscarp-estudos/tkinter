from tkinter import *

window = Tk()
window.title('Redimensionar')

# Dimensões
largura = 800
altura = 600

# Resolução
largura_screen = window.winfo_screenwidth()
altura_screen = window.winfo_screenheight()

# Posiçao da janela
pos_x = (largura_screen // 2) - (largura // 2)
pos_y = (altura_screen // 2) - (altura // 2)

# Geometry
geometry = f'{largura}x{altura}+{pos_x}+{pos_y}'
window.geometry(geometry)

window.mainloop()
