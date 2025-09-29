import sqlite3 as sql
conexao = sql.connect("biblioteca.db")
cursor = conexao.cursor()

def menu():
    print("\nMenu Biblioteca!")

    print("\n1. Listar livro")
    print("2. Adcionar livro")
    print("3. Atualizar livro")
    print("4. Remover um livro da biblioteca")
    print("5. Sair do sistema")

def listar_livros():
    for linha in cursor.fetchall():
        print(f"ID - {linha[0]} | Título - {linha[1]} | Autor - {linha[2]} | Ano - {linha[3]} | Disponibilidade - {linha[4]}")


def cadastrar_livros():
    titulo = input("Digite o Título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = int(input("Digite o ano de lançamento do livro: "))
    disponivel = "sim"
    cursor.execute("""
    INSERT INTO livros (titulo, autor, ano, disponível)
    VALUES (?, ?, ?, ?)
""", (titulo, autor, ano, disponivel))
    conexao.commit()
    
