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
        if len(clientes) == 0: st.write("NENHUM CLIENTE CADASTRADO")
        else: 
            list_dic = [] 
            for obj in clientes: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    def inserir():
        nome = st.text_input("INFORME O NOME")
        email = st.text_input("INFORME O E-MAIL")
        fone = st.text_input("INFORM O TELEFONE")
        if st.button("INSERIR"):
            Service.cliente_inserir(nome, email, fone)
            st.success("CLIENTE INSERIDO COM SUCESSO")
            time.sleep(2)
            st.rerun()
    def atualizar():
        clientes = Service.cliente_listar()
        if len(clientes) == 0: st.write("NENHUM CLIENTE CADASTRADO")
        else:
            op = st.selectbox("ATUALIZAÇÃO DE CLIENTE", clientes)
            nome = st.text_input("NOVO NOME", op.get_nome())
            email = st.text_input("NOVO E-MAIL", op.get_email())
            fone = st.text_input("NOVO TELEFONE", op.get_fone())
            if st.button("ATUALIZAR"):
                id = op.get_id()
                Service.cliente_atualizar(id, nome, email, fone)
                st.success("CLIENTE CADSTRADO COM SUCESSO")
    def excluir():
        clientes = Service.cliente_listar()
        if len(clientes) == 0: st.write("NENHUM CLIENTE CADASTRADO")
        else:
            op = st.selectbox("EXCLUSÃO DE CLIENTES", clientes)
            if st.button("EXCLUIR"):
                id = op.get_id()
                Service.cliente_excluir(id) 
                st.success("CLIENTE EXCLUÍDO COM SUCESSO")