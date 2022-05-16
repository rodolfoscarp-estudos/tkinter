from tkinter import *

window = Tk()
window.title('Cores e Fonte')

size = 40


# Width depende tipo tipo fonte
label_1 = Label(
    window,
    text=f"Tamanho {size} fonte Arial - Solid",
    bg='#FFFF22',
    fg='#22BB00',
    font=f'Arial {size} bold italic',
    width=size,
    borderwidth=2,
    relief='solid'
)

# Width depende tipo tipo fonte
label_2 = Label(
    window,
    text=f"Tamanho {size} fonte Verdana - Raised",
    bg='#BBBB15',
    fg='#00A200',
    font=f'Verdana {size} bold italic',
    width=size,
    borderwidth=2,
    relief='raised'
)

# Width depende tipo tipo fonte
label_3 = Label(
    window,
    text=f"Tamanho {size} fonte Courier - Sunken",
    bg='#BBAAEE',
    fg='#1111CB',
    font=f'Courier {size} bold italic',
    width=size,
    borderwidth=2,
    relief='sunken'
)

label_4 = Label(
    window,
    text="""
    Também é possivel utilizar 
    textos multilines
    Ridge
    """,
    bg='#22FFCC',
    fg='#0025D8',
    font='Times 13',
    width=size,
    borderwidth=2,
    relief='ridge'
)

# Relief define o tipo de borda
label_5 = Label(
    window,
    text="Utilizando Bordas - Groove",
    bg='#DD22DD',
    fg='#220055',
    font='Times 15',
    borderwidth=2,
    relief='groove'
)

label_5 = Label(
    window,
    text="Utilizando Bordas - Flat",
    bg='#FF88EE',
    fg='#550066',
    font='Times 15',
    borderwidth=2,
    relief='flat'
)


label_1.pack()
label_2.pack()
label_3.pack()
label_4.pack()
label_5.pack()

window.mainloop()
