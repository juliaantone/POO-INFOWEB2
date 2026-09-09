import streamlit as st
import pandas as pd
import time
from datetime import datetime
from service import Service

class ManterAtendimentoUI:
   def main():
        st.header("CADASTRO DE ATENDIMENTOS")
        tab1, tab2, tab3, tab4 = st.tabs(
            ["LISTAR", "INSERIR", "ATUALIZAR", "EXCLUIR"])
        with tab1:ManterAtendimentoUI.listar()
        with tab2:ManterAtendimentoUI.inserir()
        with tab3:ManterAtendimentoUI.atualizar()
        with tab4:ManterAtendimentoUI.excluir()

   def listar():
        atendimentos = Service.atendimento_listar()
        if len(atendimentos) == 0:
            st.write("NENHUM ATENDIMENTO CADASTRADO")
        else:
            list_dic = []
            for obj in atendimentos:
                list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

   def inserir():
        data = st.date_input("INFORME A DATA")
        hora = st.time_input("INFORME A HORA")
        queixa_principal = st.text_input(
            "INFORME A QUEIXA PRINCIPAL")
        historico_saude = st.text_input(
            "INFORME O HISTÓRICO DE SAÚDE")
        avaliacao = st.text_input(
            "INFORME A AVALIAÇÃO")
        prescricao = st.text_input(
            "INFORME A PRESCRIÇÃO")
        id_horario = st.number_input(
            "INFORME O ID DO HORÁRIO",
            min_value=0,
            step=1)
        if st.button("INSERIR"):
            data_hora = datetime.combine(data, hora)
            Service.atendimento_inserir(
                data_hora,
                queixa_principal,
                historico_saude,
                avaliacao,
                prescricao,
                id_horario
            )
            st.success(
                "ATENDIMENTO INSERIDO COM SUCESSO")
            time.sleep(2)
            st.rerun()

   def atualizar():
        atendimentos = Service.atendimento_listar()
        if len(atendimentos) == 0:
            st.write("NENHUM ATENDIMENTO CADASTRADO")
        else:
            op = st.selectbox(
                "ATUALIZAÇÃO DE ATENDIMENTO",
                atendimentos)
            data = st.date_input(
                "NOVA DATA",
                op.get_data().date()
            )
            hora = st.time_input(
                "NOVA HORA",
                op.get_data().time()
            )
            queixa_principal = st.text_input(
                "NOVA QUEIXA PRINCIPAL",
                op.get_queixa_principal()
            )
            historico_saude = st.text_input(
                "NOVO HISTÓRICO DE SAÚDE",
                op.get_historico_saude()
            )
            avaliacao = st.text_input(
                "NOVA AVALIAÇÃO",
                op.get_avaliacao()
            )
            prescricao = st.text_input(
                "NOVA PRESCRIÇÃO",
                op.get_prescricao()
            )
            id_horario = st.number_input(
                "NOVO ID DO HORÁRIO",
                min_value=0,
                step=1,
                value=op.get_id_horario()
            )
            if st.button("ATUALIZAR"):
                id = op.get_id()
                data_hora = datetime.combine(data, hora)
                Service.atendimento_atualizar(
                    id,
                    data_hora,
                    queixa_principal,
                    historico_saude,
                    avaliacao,
                    prescricao,
                    id_horario
                )
                st.success(
                    "ATENDIMENTO ATUALIZADO COM SUCESSO"
                )

   def excluir():
        atendimentos = Service.atendimento_listar()
        if len(atendimentos) == 0:
            st.write("NENHUM ATENDIMENTO CADASTRADO")
        else:
            op = st.selectbox(
                "EXCLUSÃO DE ATENDIMENTOS",
                atendimentos
            )
            if st.button("EXCLUIR"):
                id = op.get_id()
                Service.atendimento_excluir(id)
                st.success(
                    "ATENDIMENTO EXCLUÍDO COM SUCESSO")
