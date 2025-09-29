import sqlite3 as sql
import funcoes as fun
conexao = sql.connect("biblioteca.db")
cursor = conexao.cursor()

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
    try:
        cursor.execute("""
        SELECT * FROM livros
        """)
        for linha in cursor.fetchall():
            print(f"ID - {linha[0]} | Título - {linha[1]} | Autor - {linha[2]} | Ano - {linha[3]} | Disponibilidade - {linha[4]}")
    except Exception as erro:
        print(f"Erro ao tentar listar os livros: {erro}")

def cadastrar_livros():
    titulo = input("Digite o Título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = int(input("Digite o ano de lançamento do livro: "))
    disponivel = "Sim"
    try:
        cursor.execute("""
        INSERT INTO livros (titulo, autor, ano, disponível)
        VALUES (?, ?, ?, ?)
        """, (titulo, autor, ano, disponivel))
        conexao.commit()
    except Exception as erro:
        print(f"Erro ao tentar cadastrar livro: {erro}")
    
def atualização_disponibilidade():
    id_atualizar = input("Digite o id que queira modificar: ")
    nao_sim = int(input("Deseja disponibilizar (1) ou não disponibilizar (0): "))
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

def remover_livro():
    id_livro = int(input("Digite o ID do livro: "))
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