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

def listar_livros(limite=30, offset=0):
    try:
        with sql.connect(NOME_DB) as db:
            cur = db.cursor()
            cur.execute("SELECT id, nome, autor, img FROM biblioteca LIMIT ? OFFSET ?", (limite, offset))
            return cur.fetchall()
    except sql.Error as erro:
        return False

def listar_livro_por_nome():
    pass

def listar_livro_por_id(id_book):
    try:
        with sql.connect(NOME_DB) as db:
            cur = db.cursor()
            cur.execute("SELECT id, nome, autor, description, qtd_pags, img FROM biblioteca WHERE id = ?", (id_book,))
            return cur.fetchone()
    except sql.Error as erro:
        return False

def excluir_livro():
    pass