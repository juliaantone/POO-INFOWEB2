import streamlit as st
import time
from datetime import datetime
from service import Service

class RegistrarAtendimentoUI:
    def main():
        st.header("REGISTRAR ATENDIMENTO")
        horarios = []
        for h in Service.horario_listar_profissional(
            st.session_state["usuario_id"]
        ):
            if h.get_confirmado():
                horarios.append(h)
        if len(horarios) == 0:
            st.write("Nenhum serviço confirmado")
            return
        horario = st.selectbox("Selecione o horário", horarios)
        queixa = st.text_input("Queixa principal")
        historico = st.text_input("Histórico de saúde")
        avaliacao = st.text_input("Avaliação")
        prescricao = st.text_input("Prescrição")
        if st.button("Registrar Atendimento"):
            Service.atendimento_inserir(
                datetime.now(),
                queixa,
                historico,
                avaliacao,
                prescricao,
                horario.get_id()
            )
            st.success("Atendimento registrado com sucesso")
            time.sleep(2)
            st.rerun()