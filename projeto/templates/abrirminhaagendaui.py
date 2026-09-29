import streamlit as st
from service import Service
from datetime import datetime, time

class AbrirMinhaAgendaUI:
    def main():
        st.header("ABRIR MINHA AGENDA")
        data = st.text_input("Informe a data e hora: ", datetime.now().strftime("%d/%m/%Y"))
        hora_inicio = st.text_input("Informe o inicio horário: ")
        hora_fim = st.text_input("Informe o fim horário:")
        intervalo = st.text_input("Informe o intervalo entre os horários:")
        #senha = st.text_input("INFORME A SENHA", type="password")
        if st.button("ABRIR AGENDA"):
            Service.horario_abrir_agenda(data, hora_inicio, hora_fim, int(intervalo), None)
            st.success("HORÁRIOS CADASTRADOS COM SUCESSO")
            time.sleep(2)
            st.rerun()

               

