from customtkinter import *

def abrir_janela(janela_abrir, janela_fechar):
    janela_fechar.pack_forget()
    janela_abrir.pack(fill="both", expand=True)

def abrir_livro():
    pass