from templates.manterclienteui import ManterClienteUI
from templates.manterservicoui import ManterServicoUI
from templates.manterhorarioui import ManterHorarioUI
from templates.manterprofissionalui import ManterProfissionalUI
from templates.manteratenimentoui import ManterAtendimentoUI
from templates.perfilclienteui import PerfilClienteUI
from templates.loginui import LoginUI
from templates.abrircontaui import AbrirContaUI
import streamlit as st
from service import Service

class IndexUI:
    def menu_visitante():
        op = st.sidebar.selectbox("MENU", ['ENTRAR NO SISTEMA', 'ABRIR CONTA'])
        if op == "ENTRAR NO SISTEMA": LoginUI.main()
        if op == "ABRIRIR CONTA": AbrirContaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("MENU", ['MEUS DADOS'])
        if op == "MEUS DADOS": PerfilClienteUI.main()

    def sair_do_sistema():
        if st.sidebar.button("SAIR"):
            del st.session_state["usuaria_id"]
            del st.session_state["usuaris_nome"]
            st.rerun()

    def menu_admin():
        Service.cliente_criar_admin()
        op = st.sidebar.selectbox("MENU", ['CLIENTES', 'SERVIÇOS', 'HORÁRIOS', "PROFISSIONAIS", "ATENDIMENTOS"])
        if op  == "CLIENTES": ManterClienteUI.main()
        if op  == "SERVIÇOS": ManterServicoUI.main()
        if op  == "HORÁRIOS": ManterHorarioUI.main()
        if op  == "PROFISSIONAIS": ManterProfissionalUI.main()
        if op  == "ATENDIMENTOS": ManterAtendimentoUI.main()
    def siderar():
        IndexUI.menu_admin()
    def main():
        IndexUI.siderar()
        
IndexUI.main()