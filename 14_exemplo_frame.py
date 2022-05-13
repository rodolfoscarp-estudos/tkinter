from tkinter import *

root = Tk()
root.title('Frame')


# Funções
def executar():
    print("Fez Login")


# Widgets
frame_login = Frame(root)

label_usuario = Label(frame_login, text="Usuario: ")
label_password = Label(frame_login, text="Password: ")
text_usuario = Entry(frame_login)
text_password = Entry(frame_login)
cmd_entrar = Button(frame_login, text="Login", command=executar)

# Layout
label_usuario.grid(row=0, column=0, sticky=E)
label_password.grid(row=1, column=0, sticky=E)
text_usuario.grid(row=0, column=1, padx=(5, 0))
text_password.grid(row=1, column=1, pady=(5, 0), padx=(5, 0))
cmd_entrar.grid(row=2, column=1, sticky=E, pady=(5, 0))

frame_login.grid(padx=5, pady=5)


root.mainloop()
