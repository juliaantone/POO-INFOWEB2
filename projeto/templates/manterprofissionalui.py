
import streamlit as st
import pandas as pd
import time
from service import Service

class ManterProfissionalUI:
    def main():
        st.header("CADASTRO DE PROFISSIONAIS")
        tab1, tab2, tab3, tab4 = st.tabs(
            ["LISTAR", "INSERIR", "ATUALIZAR", "EXCLUIR"]
        )
        with tab1:ManterProfissionalUI.listar()
        with tab2:ManterProfissionalUI.inserir()
        with tab3:ManterProfissionalUI.atualizar()
        with tab4:ManterProfissionalUI.excluir()

    def listar():
        profissionais = Service.profissional_listar()
        if len(profissionais) == 0:
            st.write("NENHUM PROFISSIONAL CADASTRADO")
        else:
            list_dic = []
            for obj in profissionais:
                list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("INFORME O NOME")
        email = st.text_input("INFORME O E-MAIL")
        fone = st.text_input("INFORME O TELEFONE")
        senha = st.text_input("INFORME A SENHA", type="password")
        especialidade = st.text_input("INFORME A ESPECIALIDADE")
        if st.button("INSERIR"):
            Service.profissional_inserir(
                nome,
                email,
                fone,
                senha,
                especialidade
            )
            st.success("PROFISSIONAL INSERIDO COM SUCESSO")
            time.sleep(2)
            st.rerun()

    def atualizar():
        profissionais = Service.profissional_listar()
        if len(profissionais) == 0:
            st.write("NENHUM PROFISSIONAL CADASTRADO")
        else:
            op = st.selectbox(
                "ATUALIZAÇÃO DE PROFISSIONAL",
                profissionais
            )
            nome = st.text_input(
                "NOVO NOME",
                op.get_nome()
            )
            email = st.text_input(
                "NOVO E-MAIL",
                op.get_email()
            )
            fone = st.text_input(
                "NOVO TELEFONE",
                op.get_fone()
            )
            senha = st.text_input(
                "NOVA SENHA",
                op.get_senha(),
                type="password"
            )
            especialidade = st.text_input(
                "NOVA ESPECIALIDADE",
                op.get_especialidade()
            )
            if st.button("ATUALIZAR"):
                id = op.get_id()
                Service.profissional_atualizar(
                    id,
                    nome,
                    email,
                    fone,
                    senha,
                    especialidade
                )
                st.success("PROFISSIONAL CADASTRADO COM SUCESSO")

    def excluir():
        profissionais = Service.profissional_listar()
        if len(profissionais) == 0:
            st.write("NENHUM PROFISSIONAL CADASTRADO")
        else:
            op = st.selectbox(
                "EXCLUSÃO DE PROFISSIONAIS",
                profissionais
            )
            if st.button("EXCLUIR"):
                id = op.get_id()
                Service.profissional_excluir(id)
                st.success("PROFISSIONAL EXCLUÍDO COM SUCESSO")