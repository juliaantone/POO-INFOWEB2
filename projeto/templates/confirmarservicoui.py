import streamlit as st
import time
from service import Service

class ConfirmarServicoUI:
    def main():
        st.header("CONFIRMAR SERVIÇO")
        id_profissional = st.session_state["usuario_id"]
        horarios = Service.horario_listar_profissional(id_profissional)
        horarios_agendados = []
        for h in horarios:
            if (
                h.get_id_cliente() != 0
                and h.get_id_servico() != 0
                and h.get_confirmado() == False
            ):
                horarios_agendados.append(h)
        if len(horarios_agendados) == 0:
            st.write("NENHUM SERVIÇO AGUARDANDO CONFIRMAÇÃO")
        else:
            op = st.selectbox("SELECIONE O SERVIÇO",horarios_agendados)
            cliente = Service.cliente_listar_id(op.get_id_cliente())
            servico = Service.servico_listar_id(op.get_id_servico())
            if cliente != None:
                st.write("CLIENTE:",cliente.get_nome())
            if servico != None:
                st.write("SERVIÇO:",servico.get_descricao())
            st.write("DATA:",op.get_data())
            if st.button("CONFIRMAR"):
                Service.horario_confirmar(op.get_id())
                st.success("SERVIÇO CONFIRMADO COM SUCESSO")
                time.sleep(2)
                st.rerun()