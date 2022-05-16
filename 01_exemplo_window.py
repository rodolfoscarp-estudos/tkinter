from tkinter import *
import platform

menu_inicial = Tk()
menu_inicial.title('Primeira Janela')

# 640x480 Dimensão
# 200 200 posição
menu_inicial.geometry('640x480+200+200')

# Redimensionamento
menu_inicial.resizable(width=True, height=False)

# Min Max Size
menu_inicial.minsize(width=400, height=480)
menu_inicial.maxsize(width=800, height=480)

# Cor de fundo
menu_inicial['bg'] = 'blue'

# Estado da janela
menu_inicial.state('icon')

# Icone
system = platform.system().lower()

# Para windows
if platform == 'windows':
    menu_inicial.iconbitmap(bitmap='assets/icon.ico')

else:
    # Ubuntu não aceita .ico
    img = PhotoImage(file='assets/icon.png')
    menu_inicial.tk.call('wm', 'iconphoto', menu_inicial._w, img)


# Loop Principal
menu_inicial.mainloop()
