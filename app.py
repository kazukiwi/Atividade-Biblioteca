import streamlit as st
import funcoes as fun

st.set_page_config(page_title="Biblioteca SENAI 📚❤", layout="centered")
st.title("Biblioteca SENAI 📚❤")
menu = st.sidebar.radio("Menu", ["Cadastro", "Listar os livros", "Adicionar livros", "Atualizar disponibilidade", "Remover livros"])

if menu == "Cadastro":
    st.subheader("Cadastro do usuário")
    st.markdown("---")
    with st.form(key= "formulario_cadastro_usuario"):
        st.subheader("Insira seus dados: ")
        nome_input = st.text_input("Nome Completo:", placeholder="Seu nome")
        email_input = st.text_input("Email:", placeholder="Seu email")
        senha_input = st.text_input("Sua senha:", placeholder="Sua senha", type="password")
        st.markdown("---")

        submit_button = st.form_submit_button(label = "Finalizar Cadastro", type="primary")

        if submit_button:
            cadastro = fun.cadastro(nome_input, email_input, senha_input)

            st.spinner("Cadastrando...")
            st.success("Cadastro feito com sucesso")

if menu == "Listar os livros":
    st.subheader("Listar os livros")
    livros = fun.listar_livros()
    if livros:
        st.table(livros)
    else:
        st.warning("A tabela não está funcionando ou nenhum livro foi colocado")

if menu == "Adicionar livros":
    with st.form(key = "Adicao_de_livros"):
        st.subheader("Adicionar livros")
        nome = st.text_input("Nome do livro:", placeholder="Nome do livro")
        autor = st.text_input("Nome do autor:", placeholder="Nome autor")
        ano = st.date_input("Ano de lançamento:")

        submit_button = st.form_submit_button(label = "Finalizar de adicionar", type = "primary")

        if submit_button:
            adicionar = fun.cadastrar_livros(nome, autor, ano)

            st.spinner("Adicionando...")
            st.success("Livro adicionado com sucesso")


if menu == "Atualizar disponibilidade":
    with st.form(key = "Atualizacao_de_disponibilidade"):
        st.subheader("Atualização de disponibilidade")
        id_atualizar = st.text_input("Digite o id que queira modificar: ")
        nao_sim = st.number_input("Deseja disponibilizar (1) ou não disponibilizar (0): ")

        submit_button = st.form_submit_button(label= "Finalizar ação", type="primary")

        if submit_button:
            atualizar = fun.atualização_disponibilidade(id_atualizar, nao_sim)

            st.spinner("Atualizando...")
            st.success("Atualização feita com sucesso")


if menu == "Remover livros":
    with st.form(key = "Remover_livros"):
        st.subheader("Remoção de livros")
        id_livro = st.number_input("Digite o id do livro:")

        submit_button = st.form_submit_button(label= "Remover livros", type = "primary")
        
        if submit_button:
            remover = fun.remover_livro(id_livro)

            st.spinner("Removendo...")
            st.success("Remoção feita com sucesso")


