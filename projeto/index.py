from templates.manterclienteui import ManterclienteUI
from templates.manterservicoui import ManterservicoUI
from templates.manterhorarioui import ManterHorarioUI
from templates.manterprofissionalui import ManterProfissionalUI
#from templates.manteratenimentoui import ManterAtendimentoUI
import streamlit as st

class IndexUI:
    def menu_admin():
        op = st.sidebar.selectbox("MENU", ['CLIENTES', 'SERVIÇOS', 'HORÁRIOS', "PROFISSIONAIS", "ATENDIMENTOS"])
        if op  == "CLIENTES": ManterclienteUI.main()
        if op  == "SERVIÇOS": ManterservicoUI.main()
        if op  == "HORÁRIOS": ManterHorarioUI.main()
        if op  == "PROFISSIONAIS": ManterProfissionalUI.main()
        #if op  == "ATENDIMENTOS": ManterAtendimentoUI.main()
    def siderar():
        IndexUI.menu_admin()
    def main():
        IndexUI.siderar()
        
IndexUI.main()