import streamlit as st
import pandas as pd
from service import Service

class MeusServicosUI:
    def main():
        st.header("MEUS SERVIÇOS")
        id_cliente = st.session_state["usuario_id"]
        horarios = Service.horario_listar_cliente(id_cliente)
        if len(horarios) == 0:
            st.write("NENHUM SERVIÇO AGENDADO")
        else:
            dados = []
            for h in horarios:
                profissional = Service.profissional_listar_id(h.get_id_profissional())
                servico = Service.servico_listar_id(h.get_id_servico())

                if profissional != None:
                    nome_profissional = profissional.get_nome()
                else:
                    nome_profissional = ""

                if servico != None:
                    descricao_servico = servico.get_descricao()
                else:
                    descricao_servico = ""
                dados.append({"DATA": h.get_data(),"PROFISSIONAL": nome_profissional,"SERVIÇO": descricao_servico,"CONFIRMADO": h.get_confirmado()})
            df = pd.DataFrame(dados)
            st.dataframe(df,use_container_width=True)