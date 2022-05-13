from tkinter import *


def executar():
    print(s3.get())


root = Tk()
root.title("Exemplo SpinBox")
root.geometry("300x300")

s1 = Spinbox(root, from_=0, to=10)
s2 = Spinbox(root, values=[r for r in range(0, 100, 2)])

# wrap deixa os valor em loop
s3 = Spinbox(root, values=("Matheus", "Rodolfo", "Maluco"), wrap=True)

cmd = Button(root, text="Clique", command=executar)

s1.pack()
s2.pack()
s3.pack()
cmd.pack()

root.mainloop()
