import sqlite3 as sql
import funcoes as fun

conexao = sql.connect("biblioteca.db")

cursor = conexao.cursor()

tabela = fun.sql_table()

while True:
    menu = fun.menu()

    pergunta = int(input("Digite o número que queira entrar: "))

    if pergunta == 1:
        listar = fun.listar_livros()

    if pergunta == 2:
        cadastro = fun.cadastrar_livros()

    if pergunta == 5:
        break

cursor.close()