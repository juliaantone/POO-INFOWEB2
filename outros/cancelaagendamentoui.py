import streamlit as st

import time

from datetime import datetime

from service import Service


class CancelarAgendamentoUI:

    def main():

        st.header("CANCELAR AGENDAMENTO")

        id_cliente = st.session_state["usuario_id"]

        horarios = []

        for h in Service.horario_listar():

            if (
                h.get_id_cliente() == id_cliente
                and h.get_data() >= datetime.now()
            ):
                horarios.append(h)

        if len(horarios) == 0:

            st.write("NENHUM AGENDAMENTO DISPONÍVEL PARA CANCELAMENTO")

            return

        op = st.selectbox(
            "SELECIONE O AGENDAMENTO",
            horarios
        )

        st.write(
            "DATA:",
            op.get_data().strftime("%d/%m/%Y %H:%M")
        )

        profissional = Service.profissional_listar_id(
            op.get_id_profissional()
        )

        servico = Service.servico_listar_id(
            op.get_id_servico()
        )

        if profissional != None:
            st.write(
                "PROFISSIONAL:",
                profissional.get_nome()
            )

        if servico != None:
            st.write(
                "SERVIÇO:",
                servico.get_descricao()
            )

        confirmar = st.checkbox(
            "CONFIRMO QUE DESEJO CANCELAR ESTE AGENDAMENTO"
        )

        if st.button("CANCELAR AGENDAMENTO"):

            if confirmar:

                resultado = Service.horario_cancelar(
                    op.get_id(),
                    id_cliente
                )

                if resultado:

                    st.success(
                        "AGENDAMENTO CANCELADO COM SUCESSO"
                    )

                    time.sleep(2)

                    st.rerun()

                else:

                    st.error(
                        "NÃO FOI POSSÍVEL CANCELAR O AGENDAMENTO"
                    )

            else:

                st.warning(
                    "CONFIRME O CANCELAMENTO ANTES DE CONTINUAR"
                )