from customtkinter import * 
from tkinter import messagebox
from .funcoes import *
from PIL import Image
from tkinter import filedialog
from backend.imagem import processar_imagem
from backend.database import *
from io import BytesIO

app = CTk()
popup_cadastrar = None
caminho_imagem = None

app.title("Librum")
largura = 1450
altura = 900
x = (app.winfo_screenwidth() - largura) // 2
y = (app.winfo_screenheight() - altura) // 2
app.geometry(f"{largura}x{altura}+{x}+{y}")
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

    ano = CTkEntry(popup_cadastrar, width=200, placeholder_text="Ano de Publicação")
    ano.pack(pady=5)

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
        nome_livro = nome.get().lower()
        autor_livro = autor.get().lower()
        ano_livro = ano.get()
        if ano_livro.isdigit():
            ano_livro = int(ano_livro)
        else:
            messagebox.showerror("Erro", "O ano de publicação do livro deve ser um número inteiro.")
        descricao_livro = descricao.get().lower()
        paginas = qtd_pags.get()
        if paginas.isdigit():
            paginas = int(paginas)
        else:
            messagebox.showerror("Erro", "A quantidade de páginas deve ser um número inteiro ou maior que 4.")
        imagem = processar_imagem(caminho_imagem)
        cadastrar_livro(nome_livro, autor_livro, ano_livro, descricao_livro, paginas, imagem)

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

Scrollbar_livros = CTkScrollableFrame(frame_inicio, width=950, height=175, corner_radius=10, border_width=1, border_color="#6495ed", orientation='horizontal')
Scrollbar_livros.pack(fill="x", padx=5, pady=5)

def abrir_livro(id_livro):
    busca = listar_livro_por_id(id_livro)
    if busca is None:
        print("Livro não encontrado!")
        return
    if busca is False:
        print("Erro na consulta!")
        return

    id_book, nome, autor, ano, descricao, qtd_pags, img = busca
    frame_livro = CTkFrame(app)
    abrir_janela(frame_livro, frame_inicio)

    retangulo_img = CTkFrame(frame_livro, width=300, height=400, fg_color="#FFFFFF", corner_radius=0)
    retangulo_img.pack(side="left", anchor="nw", padx=35, pady=25)

    retangulo_text = CTkFrame(frame_livro, width=1035, height=150, border_width=1, border_color="#6495ed", fg_color="transparent", corner_radius=10)
    retangulo_text.pack_propagate(False)
    retangulo_text.pack(side="right", anchor="nw", padx=35, pady=25)

    CTkLabel(retangulo_text, text=nome.title(), font=("Georgia", 30)).pack(side="top", anchor="nw", padx=20, pady=(20, 0))
    CTkLabel(retangulo_text, text=f"Autor: {autor.title()}", font=("Arial", 15)).pack(side="top", anchor="w", padx=20, pady=0)
    CTkLabel(retangulo_text, text=f"N.º de páginas: {qtd_pags}", font=("Arial", 15)).pack(side="top", anchor="w", padx=20, pady=0)
    CTkLabel(retangulo_text, text=f"Ano: {ano}", font=("Arial", 15)).pack(side="top", anchor="w", padx=20, pady=0)

    imagem_pil = Image.open(BytesIO(img))
    imagem_ctk = CTkImage(light_image=imagem_pil, dark_image=imagem_pil, size=(300, 400))
    label_imagem = CTkLabel(retangulo_img, text="", image=imagem_ctk)
    label_imagem.pack(fill="both", expand=True)
    label_imagem.image = imagem_ctk

livros = listar_livros()
if livros:
    for livro in livros:
        id_book, nome, autor, img_db = livro

        imagem_pil = Image.open(BytesIO(img_db))
        imagem_ctk = CTkImage(light_image=imagem_pil, dark_image=imagem_pil, size=(120, 160))

        label_imagem = CTkLabel(Scrollbar_livros, text="", image=imagem_ctk)
        label_imagem.bind("<Button-1>", lambda evento, id=id_book: abrir_livro(id))
        label_imagem.pack(padx=10, pady=10)
        label_imagem.image = imagem_ctk

frame_inicio.pack(fill="both", expand=True)

app.mainloop()