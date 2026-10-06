import streamlit as st
import pandas as pd
from service import Service

class MinhaAgendaUI:
    def main():
        st.header("MINHA AGENDA")
        id_profissional = st.session_state["usuario_id"]
        horarios = Service.horario_listar_profissional(id_profissional)
        if len(horarios) == 0:
            st.write("NENHUM HORÁRIO CADASTRADO")
        else:
            dados = []
            for h in horarios:
                cliente = Service.cliente_listar_id(h.get_id_cliente())
                servico = Service.servico_listar_id(
                    h.get_id_servico())
                if cliente != None:
                    nome_cliente = cliente.get_nome()
                else:
                    nome_cliente = ""
                if servico != None:
                    descricao_servico = servico.get_descricao()
                else:
                    descricao_servico = ""
                dados.append({"ID": h.get_id(), "DATA": h.get_data(),"CLIENTE": nome_cliente, "SERVIÇO": descricao_servico, "CONFIRMADO": h.get_confirmado()})
            df = pd.DataFrame(dados)
            st.dataframe(df,use_container_width=True)