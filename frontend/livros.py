from customtkinter import * 
from univesal import * 

app = CTk()

app.title("Librum")
app.geometry("1000x650")
app.resizable(False, False)

frame_inicio = CTkFrame(app)

CTkLabel(
    frame_inicio,
    text="RH",
    font=(txtfonte, 27, "bold")
).pack(pady=(15, 20))

Scrollbar_livros = CTkScrollableFrame(frame_inicio, width=300, height=200, corner_radius=12, border_width=1, border_color="#6495ed", label_text="Livros", orientation='horizontal')
Scrollbar_livros.pack()



frame_inicio.pack()

app.mainloop()