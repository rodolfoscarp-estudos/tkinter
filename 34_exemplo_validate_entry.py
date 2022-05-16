from tkinter import *
from datetime import date


class MounthEntry(Entry):
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)

        # Registra um calback no component pai
        validate_callback = root.register(self._on_validate)

        # Faz a validação toda vez que um tecla é pressionada
        # '%P' - Valor que o campo tera
        # '%d' - Tipo de ação 1 - inclusão, 2 - exclusão, -1 - outros
        self.config(
            validate='key', validatecommand=(validate_callback, '%P', '%d'))

    def _on_validate(self, enter, action_type):
        if action_type == '1' and not enter.isdigit():
            return False

        if len(enter) > 2 and action_type == '1':
            return False

        try:
            if int(enter) > 12 and action_type == '1':
                return False
        except (ValueError, TypeError):
            return True

        return True


class YearEntry(Entry):
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)

        validate_callback = root.register(self._on_validate)

        self.config(
            validate='key', validatecommand=(validate_callback, '%P', '%d'))

    def _on_validate(self, enter, action_type):
        if action_type == '1' and not enter.isdigit():
            return False

        if len(enter) > 4 and action_type == '1':
            return False

        try:
            if int(enter) > date.today().year and action_type == '1':
                return False
        except (ValueError, TypeError):
            return True

        return True

# GUI


root = Tk()
root.title("Compara entrada Questro x Questor Zen")


# Widgets
lbl_mes_competencia = Label(root, text="Mês: ")
txt_mes_competencia = MounthEntry(root)

lbl_ano_competencia = Label(root, text="Ano: ")
txt_ano_competencia = YearEntry(root, )

btn_processar = Button(root, text="Processar")


# Layout
lbl_mes_competencia.pack()
txt_mes_competencia.pack()

lbl_ano_competencia.pack()
txt_ano_competencia.pack()

btn_processar.pack()


root.mainloop()
