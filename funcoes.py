import sqlite3 as sql
import funcoes as fun
conexao = sql.connect("biblioteca.db")
cursor = conexao.cursor()

def sql_table_users():
    conexao = sql.connect("Clientes.db")
    cursor = conexao.cursor("")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
    )
""")

def cadastro(nome, email, senha):
    conexao = sql.connect("Clientes.db")
    cursor = conexao.cursor()
    try:
        cursor.execute("""
    INSERT INTO usuarios (nome, email, senha) 
    VALUES (?, ?, ?)
    """, (nome, email, senha))
        conexao.commit()
    except Exception as erro:
        print(f"Erro ao cadastrar o usuario! Erro: {erro}")


def sql_table():
    cursor.execute("""
CREATE TABLE IF NOT EXISTS livros(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER,
    disponível TEXT         
)
""")
print("Tabela criada com sucesso!")

def conexaoo():
    conexao = sql.connect("biblioteca.db")
    cursor = conexao.cursor()

def menu():
    print("\nMenu Biblioteca!")

    print("\n1. Listar livro")
    print("2. Adcionar livro")
    print("3. Atualizar os status de um livro")
    print("4. Remover um livro da biblioteca")
    print("5. Sair do sistema")

def listar_livros():
    conexao = sql.connect("biblioteca.db")
    cursor = conexao.cursor()
    try:
        cursor.execute("""
        SELECT * FROM livros
        """)
        livros = cursor.fetchall()
        return livros
    except Exception as erro:
        print(f"Erro ao tentar listar os livros: {erro}")
    finally:
        if conexao:
            conexao.close()

def cadastrar_livros(titulo, autor, ano):
    conexao = sql.connect("biblioteca.db")
    cursor = conexao.cursor()
    disponivel = "Sim"
    try:
        cursor.execute("""
        INSERT INTO livros (titulo, autor, ano, disponível)
        VALUES (?, ?, ?, ?)
        """, (titulo, autor, ano, disponivel))
        conexao.commit()
    except Exception as erro:
        print(f"Erro ao tentar cadastrar livro: {erro}")
    finally:
        if conexao:
            conexao.close()
    
def atualização_disponibilidade(id_atualizar, nao_sim):
    conexao = sql.connect("biblioteca.db")
    cursor = conexao.cursor()
    try:
        if nao_sim == 0:
            cursor.execute("""
            UPDATE livros
            SET disponível = ? WHERE id = ?
            """, ("Não", id_atualizar,))
            conexao.commit()

        elif nao_sim == 1:
            cursor.execute("""
            UPDATE livros
            SET disponível = ? WHERE id = ?
            """, ("Sim", id_atualizar,))
            conexao.commit()
    except Exception as erro:
        print(f"Erro ao tentar atualizar a disponibilidade: {erro}")
    finally:
        if conexao:
            conexao.close()

def remover_livro(id_livro):
    conexao = sql.connect("biblioteca.db")
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM livros WHERE id = ?", (id_livro,))
        conexao.commit()

        if cursor.rowcount > 0:
            print("Livro excluido com sucesso!")
        else:
            print("Nenhum livro encontrado com o ID fornecido")
    except Exception as error:
        print(f"Error encontrado! ERRO {error}")

    finally:
        if conexao:
            conexao.close()