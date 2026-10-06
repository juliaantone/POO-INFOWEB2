import streamlit as st
import time
from service import Service

class AlterarSenhaUI:
    def main():
        st.header("ALTERAR SENHA")
        nova_senha = st.text_input("INFORME A NOVA SENHA",type="password")
        confirmar_senha = st.text_input("CONFIRME A NOVA SENHA",type="password")
        if st.button("ALTERAR SENHA"):
            if nova_senha == "":st.warning("Informe a nova senha.")
            elif nova_senha != confirmar_senha:
                st.warning("As senhas não são iguais.")
            else:
                Service.cliente_alterar_senha(
                    st.session_state["usuario_id"],nova_senha)
                st.success(
                    "SENHA ALTERADA COM SUCESSO")
                time.sleep(2)
                st.rerun()