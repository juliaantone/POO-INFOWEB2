from templates.manterclienteui import ManterclienteUI
from templates.manterservicoui import ManterservicoUI
import streamlit as st

class IndexUI:
    def main():
        op = st.sidebar.selectbox("MENU", ['CLIENTES', 'SERVIÇOS'])
        if op  == "CLIENTES": ManterclienteUI.main()
        if op  == "SERVIÇOS": ManterservicoUI.main()

IndexUI.main()