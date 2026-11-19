from customtkinter import *

tipos = ["Erro", "Aviso", "Sucesso"]

def criar_messagebox(pai, titulo="MessageBox", largura=450, altura=150, tipo="Aviso", texto="", tam_texto=15):
    box = CTkToplevel(pai)
    box.title(titulo)
    x = (box.winfo_screenwidth() - largura) // 2
    y = (box.winfo_screenheight() - altura) // 2
    box.geometry(f"{largura}x{altura}+{x}+{y}")
    box.transient(pai)
    box.grab_set()
    box.focus_force()

    frame_conteudo = CTkFrame(box, fg_color="transparent")
    frame_conteudo.pack(fill="both", expand=True, padx=20, pady=20)

    if tipo == "Aviso":
        CTkLabel(
            frame_conteudo,
            text="⚠️",
            font=("Arial", 45)
        ).pack(side="left", anchor="n", padx=(0, 15))

        CTkLabel(
            frame_conteudo,
            text=texto,
            font=("Arial", tam_texto),
            wraplength=300,
            justify="left"
        ).pack(side="left", anchor="n")

    elif tipo == "Sucesso":
        CTkLabel(
            frame_conteudo,
            text="✓",
            font=("Arial", 45, "bold"),
            text_color="#2ECC71"
        ).pack(side="left", anchor="n", padx=(0, 15))

        CTkLabel(
            frame_conteudo,
            text=texto,
            font=("Arial", tam_texto),
            wraplength=300,
            justify="left"
        ).pack(side="left", anchor="n")

    elif tipo == "Erro":
        CTkLabel(
            frame_conteudo,
            text="✕",
            font=("Arial", 45, "bold"),
            text_color="#E74C3C"
        ).pack(side="left", anchor="n", padx=(0, 15))

        CTkLabel(
            frame_conteudo,
            text=texto,
            font=("Arial", tam_texto),
            wraplength=300,
            justify="left"
        ).pack(side="left", anchor="n")

    else:
        CTkLabel(
            frame_conteudo,
            text="ⓘ",
            font=("Arial", 45),
            text_color="#3498DB"
        ).pack(side="left", anchor="n", padx=(0, 15))

        CTkLabel(
            frame_conteudo,
            text=texto,
            font=("Arial", tam_texto),
            wraplength=300,
            justify="left"
        ).pack(side="left", anchor="n")


app = CTk()
app.withdraw()

criar_messagebox(
    app
)

app.mainloop()
