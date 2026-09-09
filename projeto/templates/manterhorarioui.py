import streamlit as st
import pandas as pd
from service import Service
import time
from datetime import datetime

class ManterHorarioUI:
    def main():
        st.header("CADASTRO DE HORÁRIOS")
        tab1, tab2, tab3, tab4 = st.tabs(["LISTAR", "INSERIR", "ATUALIZAR", "EXCLUIR"])
        with tab1: ManterHorarioUI.listar()
        with tab2: ManterHorarioUI.inserir()
        with tab3: ManterHorarioUI.atualizar()
        with tab4: ManterHorarioUI.excluir()

    def listar():
        horarios = Service.horario_listar()
        if len(horarios) == 0: st.write("NENHUM HORÁRIO CADASTRADO")
        else:
            dic = []
            for obj in horarios:
                cliente = Service.cliente_listar_id(obj.get_id_cliente())
                servico = Service.servico_listar_id(obj.get_id_servico())
                if cliente != None: cliente = cliente.get_nome()
                if servico != None: servico = servico.get_descricao()
                dic.append({"id" : obj.get_id(), "data" : obj.get_data(),
                "confirmado" : obj.get_confirmado(), "cliente" : cliente,
                "serviço" : servico})
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        clientes = Service.cliente_listar()
        servicos = Service.servico_listar()
        data = st.text_input("INFORME A DATA E HORÁRIO DO SERVIÇO", datetime.now().strftime("%d/%m/%Y %H:%M"))
        confirmado = st.checkbox("CONFIRMADO")
        cliente = st.selectbox("INFORME O CLIENTE", clientes, index = None)
        servico = st.selectbox("INFORME O SERVIÇO", servicos, index = None)
        if st.button("Inserir"):
            id_cliente = None
            id_servico = None
            if cliente != None: id_cliente = cliente.get_id()
            if servico != None: id_servico = servico.get_id()
            Service.horario_inserir(datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, id_cliente, id_servico)
            st.success("HORÁRIO INSERIDO COM SUCESSO")
            time.sleep(2)
            st.rerun()

    def atualizar():
        horarios = Service.horario_listar()
        if len(horarios) == 0: st.write("NENHUM HORÁRIO CADASTRADO")
        else:
            clientes = Service.cliente_listar()
            servicos = Service.servico_listar()
            op = st.selectbox("ATUALIZAÇÃODE HORÁRIOS", horarios)
            data = st.text_input("INFORME A NOVA DATA E HORÁRIO DO SERVIÇO", op.get_data().strftime("%d/%m/%Y %H:%M"))
            confirmado = st.checkbox("Nova confirmação", op.get_confirmado())
            id_cliente = None if op.get_id_cliente() in [0, None] else op.get_id_cliente()
            id_servico = None if op.get_id_servico() in [0, None] else op.get_id_servico()
            cliente = st.selectbox("INFORME O NOVO CLIENTE", clientes, next((i for i, c in enumerate(clientes) if c.get_id() == id_cliente), None))
            servico = st.selectbox("INFORME O NOVO SERVIÇO", servicos, next((i for i, s in enumerate(servicos) if s.get_id() == id_servico), None))
            if st.button("ATUALIZAR"):
                id_cliente = None
                id_servico = None
                if cliente != None: id_cliente = cliente.get_id()
                if servico != None: id_servico = servico.get_id()
                Service.horario_atualizar(op.get_id(), datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, id_cliente, id_servico)
                st.success("HORÁRIO ATUALIZADO COM SUCESSO")
                time.sleep(2)
                st.rerun()

    def excluir():
        horarios = Service.horario_listar()
        if len(horarios) == 0: st.write("NENHUM HORÁRIO CADASTRADO")
        else:
            op = st.selectbox("EXCLUSÃODE HORÁRIOS", horarios)
            if st.button("EXCLUIR"):
                Service.horario_excluir(op.get_id())
                st.success("HORÁRIO EXCLUIDO COM SUCESSO")
                time.sleep(2)
                st.rerun()