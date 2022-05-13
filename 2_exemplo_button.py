from tkinter import *


window = Tk()
window.title('Exemplo Botao')

window.geometry('300x300')

# Cria um botão
btn = Button(window, text="Executar", command=lambda: print("Clicou"))
# pack é necessario para desenhar o botão
btn.pack()


# Cria um botão
def click_2(mensagem: str):
    print(mensagem)


btn2 = Button(
    window, text="Executar2",
    command=lambda: click_2("Minha Mensagem")
)
# pack é necessario para desenhar o botão
btn2.pack()


window.mainloop()
