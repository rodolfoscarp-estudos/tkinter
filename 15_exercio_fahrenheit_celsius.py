from tkinter import *


# Funções
def calcular():
    f = float(textbox1.get())
    c = (f - 32) * (5 / 9)
    final.set(str(round(c, 2)) + " Graus Celsius")


# GUI
root = Tk()
root.title("Fahrenheit para Celsius")

final = StringVar()


# Widgets
label1 = Label(root, text="Grau Fahrenheit: ")
textbox1 = Entry(root)
button1 = Button(root, text="Calcular", command=calcular)
label_resultado = Label(root, textvariable=final)

# Layout
label1.grid()
textbox1.grid()
button1.grid()
label_resultado.grid()

# Loop
root.mainloop()
