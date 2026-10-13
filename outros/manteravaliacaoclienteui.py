import streamlit as st
import pandas as pd
import time

from service import Service


class ManterAvaliacaoClienteUI:

    def main():

        st.header("AVALIAÇÕES DE ATENDIMENTOS")

        tab1, tab2 = st.tabs(["LISTAR", "INSERIR"])

        with tab1:
            ManterAvaliacaoClienteUI.listar()

        with tab2:
            ManterAvaliacaoClienteUI.inserir()

    def listar():

        avaliacoes = Service.avaliacao_listar()

        if len(avaliacoes) == 0:
            st.write("NENHUMA AVALIAÇÃO CADASTRADA")

        else:
            list_dic = []

            for obj in avaliacoes:
                list_dic.append(obj.to_json())

            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():

        atendimentos = Service.atendimento_listar()

        if len(atendimentos) == 0:
            st.write("NENHUM ATENDIMENTO CADASTRADO")
            return

        atendimento = st.selectbox(
            "SELECIONE O ATENDIMENTO",
            atendimentos
        )

        nota = st.selectbox(
            "INFORME A NOTA",
            [1, 2, 3, 4, 5]
        )

        comentario = st.text_input(
            "INFORME O COMENTÁRIO"
        )

        if st.button("AVALIAR"):

            Service.avaliacao_inserir(
                nota,
                comentario,
                atendimento.get_id(),
                st.session_state["usuario_id"]
            )

            st.success("AVALIAÇÃO CADASTRADA COM SUCESSO")

            time.sleep(2)
            st.rerun()