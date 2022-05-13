from tkinter import *

root = Tk()
root.title('ColumnSpan')

Label(root, width=20, bg='red').grid()
Label(root, width=20, bg='green').grid(column=1)
Label(root, width=40, bg='blue').grid(columnspan=2, sticky='we')

# 'we' remove respiro nas laterais quando usado columnspan

root.mainloop()
