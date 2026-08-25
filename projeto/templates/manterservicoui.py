import streamlit as st
import pandas as pd
import time
from service import Service

class ManterservicoUI:
    def main():
        st.header("CADASTRO DE SERVIÇOS")
        tab5, tab6, tab7, tab8 = st.tabs(["LISTAR", "INSERIR", "ATUALIZAR", "EXCLUIR"])
        with tab5: ManterservicoUI.listarser()
        with tab6:ManterservicoUI.inserirser()
        with tab7:ManterservicoUI.atualizarser()
        with tab8: ManterservicoUI.excluirser()
    def listarser():
        servicos = Service.servico_listar()
        if len(servicos) == 0: st.write("NENHUM SERVIÇO CADASTRADO")
        else:
            list_dic = []
            for obj in servicos: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    def inserirser():
        descricao = st.text_input("INFORME A DESCRIÇÃO")
        valor = st.number_input("INFORME O VALOR", min_value=0.0, step=0.01)
        if st.button("INSERIR"): Service.servico_inserir(descricao, valor)
        st.success("SERVIÇO INSERIDO COM SUCESSO")
        time.sleep(2)
        st.rerun()
    def atualizarser():
        servicos = Service.servico_listar()
        if len(servicos) == 0: st.write("NENHUM SERVIÇO CADASTRADO")
        else:
            op = st.selectbox("ATUALIZAÇÃO DE SERVIÇO", servicos)
            descricao = st.text_input("NOVA DESCRIÇÃO", op.get_descricao())
            valor = st.number_input("NOVO VALOR", min_value=0.0, value=float(op.get_valor()), step=0.01)
            if st.button("ATUALIZAR"): id = op.get_id()
            Service.servico_atualizar( id, descricao, valor)
            st.success("SERVIÇO ATUALIZADO COM SUCESSO")
    def excluirser():
        servicos = Service.servico_listar()
        if len(servicos) == 0:
            st.write("NENHUM SERVIÇO CADASTRADO")
        else:
            op = st.selectbox("EXCLUSÃO DE SERVIÇOS", servicos)
            if st.button("EXCLUIR"):
                id = op.get_id()
                Service.servico_excluir(id)
                st.success("SERVIÇO EXCLUÍDO COM SUCESSO")