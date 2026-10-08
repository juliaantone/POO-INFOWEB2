import streamlit as st
import time
from service import Service

class PagarAtendimentoUI:
    def main():
        st.header("PAGAR ATENDIMENTO")
        atendimentos = []
        for a in Service.atendimento_listar():
            horario = Service.horario_listar_id(
                a.get_id_horario())
            if horario != None:
                if horario.get_id_cliente() == st.session_state["usuario_id"]:
                    if a.get_pago() == False:
                        atendimentos.append(a)
        if len(atendimentos) == 0:
            st.write("Nenhum atendimento pendente")
            return
        atendimento = st.selectbox("Selecione",atendimentos)
        st.write(
            f"Valor: R$ {atendimento.get_total():.2f}")
        if st.button("Pagar"):
            Service.atendimento_pagar(
                atendimento.get_id())
            st.success("Pagamento realizado")
            time.sleep(2)
            st.rerun()