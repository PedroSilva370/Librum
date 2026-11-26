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
popup_autenticar = None
caminho_imagem = None
Scrollbar_livros = None
font_text = "Georgia"
cor_principal = "#0f4bbb"
# "#6495ed"

app.title("Librum")
largura = 1450
altura = 900
x = (app.winfo_screenwidth() - largura) // 2
y = (app.winfo_screenheight() - altura) // 2
app.geometry(f"{largura}x{altura}+{x}+{y}")
app.resizable(False, False)

frame_inicio = CTkFrame(app)
frame_menu = CTkFrame(app, width=1000, height=30)
frame_menu.pack(fill="x", padx=5, pady=5)

def aplicar_livro():
    for widget in Scrollbar_livros.winfo_children():
        widget.destroy()

    livros = listar_livros()
    if livros:
        for livro in livros:
            id_book, nome, autor, img_db = livro

            imagem_pil = Image.open(BytesIO(img_db))
            imagem_ctk = CTkImage(light_image=imagem_pil, dark_image=imagem_pil, size=(120, 160))

            label_imagem = CTkLabel(Scrollbar_livros, text="", image=imagem_ctk)
            label_imagem.bind("<Button-1>", lambda evento, id_livro=id_book: abrir_livro(id_livro))
            label_imagem.pack(side="left", padx=10, pady=10)
            label_imagem.image = imagem_ctk

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
    popup_cadastrar.resizable(False, False)
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
        cad = cadastrar_livro(nome_livro, autor_livro, ano_livro, descricao_livro, paginas, imagem)

        if cad:
            aplicar_livro()
            fechar_popup()
        else:
            messagebox.showerror("Erro", "Não foi possível cadastrar este livro.")

    btn_salvar = CTkButton(popup_cadastrar, command=salvar, width=200, text="Salvar")
    btn_salvar.pack(pady=5)


    def fechar_popup():
        global popup_cadastrar
        popup_cadastrar.destroy()
    
btn_pesquisar = CTkButton(frame_menu, text="Pesquisar", fg_color=cor_principal, width=65, height=25)
btn_pesquisar.pack(side="right", padx=5, pady=10)

campo_pesquisar = CTkEntry(frame_menu, placeholder_text="Pesquisar", width=125, height=25)
campo_pesquisar.pack(side="right", padx=10, pady=10)

btn_inicio = CTkButton(frame_menu, text="Librum", font=(font_text, 19), text_color=cor_principal, command=lambda: abrir_janela(frame_inicio), fg_color="transparent", hover_color="#333333")
btn_inicio.place(relx=0.5, rely=0.5, anchor="center")

btn_cadastrar = CTkButton(frame_menu, text="Cadastrar", command=abrir_popcad, fg_color="transparent", hover_color="#333333")
btn_cadastrar.pack(side="left", padx=10, pady=10)

Scrollbar_livros = CTkScrollableFrame(frame_inicio, width=950, height=175, corner_radius=10, border_width=1, border_color=cor_principal, orientation='horizontal')
Scrollbar_livros.pack(fill="x", padx=5, pady=5)
aplicar_livro()

def abrir_autenticador():
    global popup_autenticar

    if popup_autenticar is not None:
        try:
            if popup_autenticar.winfo_exists():
                popup_autenticar.focus_force()
                return
        except:
            popup_autenticar = None

    popup_autenticar = CTkToplevel(app)
    popup_autenticar.title("Autenticador")
    popup_autenticar.geometry("400x450")
    popup_autenticar.resizable(False, False)
    popup_autenticar.grab_set()

    CTkLabel(popup_autenticar, text="Autenticador Requerida", font=(font_text, 22, "bold")).pack(pady=15)

    imagem_usuario = CTkImage(light_image=Image.open("assets/icone_usuario3.png"), dark_image=Image.open("assets/icone_usuario3.png"), size=(90, 90))
    user_image = CTkLabel(popup_autenticar, text="", image=imagem_usuario, width=65, height=65, fg_color="transparent")
    user_image.pack()

    CTkLabel(popup_autenticar, text="Coloque a senha de permição", font=("Arial", 15), text_color="#7C7C7C").pack(pady=5)
    entrada_senha = CTkEntry(popup_autenticar, placeholder_text="Senha de Verificação", width=200, height=30)
    entrada_senha.pack()

    CTkButton(popup_autenticar, text="Cancelar", font=("Arial", 15), command=popup_autenticar.destroy).pack(side="left", anchor="s", pady=20, padx=20)

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

    retangulo_img = CTkFrame(frame_livro, width=300, height=350, fg_color="#FFFFFF", corner_radius=0)
    retangulo_img.pack(side="left", anchor="nw", padx=35, pady=25)

    retangulo_text = CTkFrame(frame_livro, width=1035, height=200, border_width=1, border_color=cor_principal, fg_color="transparent", corner_radius=10)
    retangulo_text.pack_propagate(False)
    retangulo_text.pack(side="top", anchor="nw", padx=35, pady=25)

    CTkLabel(retangulo_text, text=nome.title(), font=(font_text, 30)).pack(side="top", anchor="nw", padx=20, pady=(25, 0))
    CTkLabel(retangulo_text, text=f"Autor: {autor.title()}", font=("Arial", 15)).pack(side="top", anchor="w", padx=20, pady=2.5)
    CTkLabel(retangulo_text, text=f"N.º de páginas: {qtd_pags}", font=("Arial", 15)).pack(side="top", anchor="w", padx=20, pady=2.5)
    CTkLabel(retangulo_text, text=f"Ano: {ano}", font=("Arial", 15)).pack(side="top", anchor="w", padx=20, pady=2.5)
    CTkLabel(retangulo_text, text=f"ID: {id_book}", font=("Arial", 15)).place(relx=1.0, x=-20, y=15, anchor="ne")

    retangulo_desc = CTkFrame(frame_livro, width=1035, height=150, border_width=1, border_color=cor_principal, fg_color="transparent", corner_radius=10)
    retangulo_desc.pack_propagate(False)
    retangulo_desc.pack(side="top", anchor="nw", padx=35, pady=25)

    CTkLabel(retangulo_desc, text="Descrição", font=(font_text, 17)).pack(side="top", anchor="nw", padx=20, pady=10)
    CTkLabel(retangulo_desc, text=descricao.capitalize(), font=(font_text, 13), wraplength=980, justify="left").pack(side="top", padx=20, pady=15, fill="both")

    imagem_pil = Image.open(BytesIO(img))
    imagem_ctk = CTkImage(light_image=imagem_pil, dark_image=imagem_pil, size=(300, 400))
    label_imagem = CTkLabel(retangulo_img, text="", image=imagem_ctk)
    label_imagem.pack(fill="both", expand=True)
    label_imagem.image = imagem_ctk

    btn_editar = CTkButton(frame_livro, text="Editar Livro", font=("Arial", 15), command=abrir_autenticador, width=175, fg_color=cor_principal)
    btn_editar.pack()

frame_inicio.pack(fill="both", expand=True)

app.mainloop()