import sqlite3 as sql
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

def menu():
    print("\nMenu Biblioteca!")

    print("\n1. Listar livro")
    print("2. Adcionar livro")
    print("3. Atualizar os status de um livro")
    print("4. Remover um livro da biblioteca")
    print("5. Sair do sistema")

def listar_livros():
    cursor.execute("""
    SELECT * FROM biblioteca
    """)
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
    
def atualização_disponibilidade():
    id_atualizar = input("Digite o id que queira modificar: ")
    nao_sim = int(input("Deseja disponibilizar (1) ou não disponibilizar (0): "))
    if nao_sim == 0:
        cursor.execute("""
        SET disponível = ? FROM WHERE id = ?
        """, ("Não", id_atualizar))
        conexao.commit()

    elif nao_sim == 1:
        cursor.execute("""
        UPDATE biblioteca
        SET disponível = ? FROM WHERE id = ?
        """, ("Sim", id_atualizar))
        conexao.commit()
    