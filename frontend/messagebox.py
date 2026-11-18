from customtkinter import *

tipos = ["Erro", "Aviso", "MensagemInformativa"]

def criar_messagebox(titulo="MassageBox", largura=450, altura=150, tipo="Aviso", texto=""):
    box = CTk()
    box.title(titulo)
    x = (box.winfo_screenwidth() - largura) // 2
    y = (box.winfo_screenheight() - altura) // 2
    box.geometry(f"{largura}x{altura}+{x}+{y}")

    if tipo == "Aviso":
        pass

    elif tipo == "MensagemInformativa":
        pass

    elif tipo == "Erro":
        pass

    box.mainloop()

criar_messagebox()