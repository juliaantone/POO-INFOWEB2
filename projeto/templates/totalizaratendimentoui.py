import streamlit as st
import pandas as pd
from datetime import date
from service import Service

class TotalizarAtendimentosUI:
    def main():
        st.header("TOTALIZAR ATENDIMENTOS DOS PROFISSIONAIS")
        data_inicial = st.date_input(
            "INFORME A DATA INICIAL",
            value=date.today() )
        data_final = st.date_input(
            "INFORME A DATA FINAL",
            value=date.today() )
        if st.button("TOTALIZAR"):
            if data_inicial > data_final:
                st.warning(
                    "A data inicial não pode ser posterior à data final.")
            else:
                resultado = Service.atendimento_totalizar_profissionais(
                    data_inicial, data_final)
                if len(resultado) == 0:
                    st.write("NENHUM PROFISSIONAL CADASTRADO")
                else:
                    df = pd.DataFrame(resultado)
                    st.dataframe(df, use_container_width=True)