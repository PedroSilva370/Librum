from customtkinter import * 
from .funcoes import *
from PIL import Image
from tkinter import filedialog
from backend.imagem import processar_imagem

app = CTk()
popup_cadastrar = None
caminho_imagem = None

app.title("Librum")
app.geometry("1000x650")
app.resizable(False, False)

frame_menu = CTkFrame(app, width=1000, height=30)
frame_menu.pack(fill="x", padx=5, pady=5)

def abrir_popcad():
    global popup_cadastrar

    if popup_cadastrar is not None:
        try:
            if popup_cadastrar.winfo_exists():
                popup_cadastrar.focus_force()
                return
        except:
            popup_cadastrar = None

    popup_cadastrar = CTkToplevel(app)
    popup_cadastrar.title("Cadastrar")
    popup_cadastrar.geometry("550x450")
    popup_cadastrar.grab_set()

    nome = CTkEntry(popup_cadastrar, width=200, placeholder_text="Nome do Livro")
    nome.pack(pady=5)

    autor = CTkEntry(popup_cadastrar, width=200, placeholder_text="Autor do Livro")
    autor.pack(pady=5)

    descricao = CTkEntry(popup_cadastrar, width=200, placeholder_text="Descrição (Opcional)")
    descricao.pack(pady=5)

    qtd_pags = CTkEntry(popup_cadastrar, width=200, placeholder_text="Quantidade de Páginas")
    qtd_pags.pack(pady=5)

    def selecionar_imagem():
        global caminho_imagem

        caminho = filedialog.askopenfilename(filetypes=[("Imagens", "*.png *.jpg *.jpeg")])
        if caminho:
            caminho_imagem = caminho
            imagem = CTkImage(light_image=Image.open(caminho), size=(150, 180))
            label_imagem.configure(image=imagem, text="")
            label_imagem.image = imagem

    label_imagem = CTkLabel(popup_cadastrar, text="Nenhuma imagem selecionada", width=150, height=180, fg_color="#333333", corner_radius=10)
    label_imagem.pack(pady=10)

    CTkButton(popup_cadastrar, text="Escolher imagem", width=200, command=selecionar_imagem).pack()

    def salvar():
        nome_livro = nome.get()
        autor_livro = autor.get()
        descricao_livro = descricao.get()
        paginas = qtd_pags.get()
        imagem = processar_imagem(caminho_imagem)

        #função do back q cadastra

    btn_salvar = CTkButton(popup_cadastrar, command=salvar, width=200, text="Salvar")
    btn_salvar.pack(pady=5)

    def fechar_popup():
        global popup_cadastrar
        popup_cadastrar.destroy()

btn_pesquisar = CTkButton(frame_menu, text="Pesquisar", width=65, height=25)
btn_pesquisar.pack(side="right", padx=5, pady=10)

campo_pesquisar = CTkEntry(frame_menu, placeholder_text="Pesquisar", width=100, height=25)
campo_pesquisar.pack(side="right", padx=10, pady=10)

btn_cadastrar = CTkButton(frame_menu, text="Cadastrar", command=abrir_popcad, fg_color="transparent", hover_color="#333333")
btn_cadastrar.pack(side="left", padx=10, pady=10)

frame_inicio = CTkFrame(app)

CTkLabel(frame_inicio, text="Librum", font=("Poppins", 27, "bold")).pack(pady=(15, 20))

Scrollbar_livros = CTkScrollableFrame(frame_inicio, width=950, height=100, corner_radius=12, border_width=1, border_color="#6495ed", orientation='horizontal')
Scrollbar_livros.pack()

frame_inicio.pack(fill="both", expand=True)

app.mainloop()