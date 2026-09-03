from templates.manterclienteui import ManterclienteUI
from templates.manterservicoui import ManterservicoUI
from projeto.templates.manterhorarioui import ManterHorarioUI
import streamlit as st

class IndexUI:
    def menu_admin():
        op = st.sidebar.selectbox("MENU", ['CLIENTES', 'SERVIÇOS', 'HORÁRIOS'])
        if op  == "CLIENTES": ManterclienteUI.main()
        if op  == "SERVIÇOS": ManterservicoUI.main()
        if op  == "HORÁRIOS": ManterHorarioUI.main()
    def siderar():
        IndexUI.menu_admin()
    def main():
        IndexUI.siderar()
        
IndexUI.main()