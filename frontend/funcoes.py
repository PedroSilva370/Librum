from customtkinter import *

janela_atual = None

def abrir_janela(nova_janela, janela_anterior=None):
    global janela_atual

    if janela_anterior is not None:
        janela_anterior.pack_forget()

    elif janela_atual is not None:
        janela_atual.pack_forget()

    nova_janela.pack(fill="both", expand=True)
    janela_atual = nova_janela