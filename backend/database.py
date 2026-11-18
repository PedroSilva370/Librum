import sqlite3 as sql

NOME_DB = "database/booktrack.db"

def criar_db():
    try:
        with sql.connect(NOME_DB) as db:
            cur = db.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS biblioteca (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, autor TEXT NOT NULL, description TEXT, qtd_pags INTEGER NOT NULL, img BLOB)")
    except sql.Error as erro:
        print(f"Falha ao criar o Banco de Dados: {erro}")

def cadastrar_livro(nome, autor, descricao, paginas, imagem):
    try:
        with sql.connect(NOME_DB) as db:
            cur = db.cursor()
            cur.execute("INSERT INTO biblioteca (nome, autor, description, qtd_pags, img) VALUES (?, ?, ?, ?, ?)", (nome, autor, descricao, paginas, imagem))
        return True
    except sql.Error as erro:
        return False

def editar_livro():
    pass

def listar_livros():
    pass

def listar_livro_por_nome():
    pass

def excluir_livro():
    pass