from customtkinter import * 

app = CTk()

app.title("Librum")
app.geometry("1000x650")
app.resizable(False, False)

frame_menu = CTkFrame(app, width=1000, height=30)
frame_menu.pack(fill="x", padx=5, pady=5)


btn_pesquisar = CTkButton(frame_menu, text="Pesquisar", width=65, height=25)
btn_pesquisar.pack(side="right", padx=5, pady=10)

campo_pesquisar = CTkEntry(frame_menu, placeholder_text="Pesquisar", width=100, height=25)
campo_pesquisar.pack(side="right", padx=10, pady=10)


frame_inicio = CTkFrame(app)

CTkLabel(
    frame_inicio,
    text="Librum",
    font=("Poppins", 27, "bold")
).pack(pady=(15, 20))

Scrollbar_livros = CTkScrollableFrame(frame_inicio, width=950, height=100, corner_radius=12, border_width=1, border_color="#6495ed", orientation='horizontal')
Scrollbar_livros.pack()



frame_inicio.pack(fill="both", expand=True)

app.mainloop()