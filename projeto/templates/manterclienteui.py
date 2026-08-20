import streamlit as st
import pandas as pd
import time
from service import Service

class ManterclienteUI:
    def main():
        st.header("CADASTRO DE CLIENTES")
        tab1, tab2, tab3, tab4 = st.tabs(["LISTAR", "INSERIR","ATUALIZAR", "EXCLUIR"])
        with tab1: ManterclienteUI.listar()
        with tab2: ManterclienteUI.inserir()
        with tab3: ManterclienteUI.atualizar()
        with tab4: ManterclienteUI.excluir()
    def listar():
        clientes = Service.cliente_listar()
        if len(clientes) == 0: st.write("NENHUM CLENTE CADASTRADO")
        else: 
            list_dic = [] 
            for obj in clientes: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    def inserir():
            pass
    def atualizar():
            pass
    def excluir():
            pass