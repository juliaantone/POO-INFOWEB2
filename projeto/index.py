from templates.manterclienteui import ManterClienteUI
from templates.manterservicoui import ManterServicoUI
from templates.manterhorarioui import ManterHorarioUI
from templates.manterprofissionalui import ManterProfissionalUI
from templates.manteratenimentoui import ManterAtendimentoUI
from templates.perfilclienteui import PerfilClienteUI
from templates.perfilprofissionalui import PerfilProfissionalUI
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

    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados"])
        if op == "Meus Dados": PerfilProfissionalUI.main()


    def menu_admin():
        Service.cliente_criar_admin()
        op = st.sidebar.selectbox("MENU", ['CLIENTES', 'SERVIÇOS', 'HORÁRIOS', "PROFISSIONAIS", "ATENDIMENTOS"])
        if op  == "CLIENTES": ManterClienteUI.main()
        if op  == "SERVIÇOS": ManterServicoUI.main()
        if op  == "HORÁRIOS": ManterHorarioUI.main()
        if op  == "PROFISSIONAIS": ManterProfissionalUI.main()
        if op  == "ATENDIMENTOS": ManterAtendimentoUI.main()

    def menu_admin():
        Service.cliente_criar_admin()
        op = st.sidebar.selectbox("MENU", ['CLIENTES', 'SERVIÇOS', 'HORÁRIOS', "PROFISSIONAIS", "ATENDIMENTOS"])
        if op  == "CLIENTES": ManterClienteUI.main()
        if op  == "SERVIÇOS": ManterServicoUI.main()
        if op  == "HORÁRIOS": ManterHorarioUI.main()
        if op  == "PROFISSIONAIS": ManterProfissionalUI.main()
        if op  == "ATENDIMENTOS": ManterAtendimentoUI.main()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()

    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            admin = st.session_state["usuario_nome"] == "admin"
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            if admin: IndexUI.menu_admin()
            else:
                if st.session_state["usuario_tipo"] == "cliente": IndexUI.menu_cliente()
                else: IndexUI.menu_profissional()
            IndexUI.sair_do_sistema()

    def main():
        # verifica a existe o usuário admin
        Service.cliente_criar_admin()
        # monta o sidebar
        IndexUI.sidebar()
        
IndexUI.main()