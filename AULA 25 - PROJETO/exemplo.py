#pagamento: 
class Pagamento:

    def __init__(self, id, valor, forma, id_atendimento):
        self.set_id(id)
        self.set_valor(valor)
        self.set_forma(forma)
        self.set_id_atendimento(id_atendimento)

    # GETS

    def get_id(self):
        return self.__id

    def get_valor(self):
        return self.__valor

    def get_forma(self):
        return self.__forma

    def get_id_atendimento(self):
        return self.__id_atendimento

    # SETS

    def set_id(self, id):
        if id < 0:
            raise ValueError("Id deve ser positivo")
        self.__id = id

    def set_valor(self, valor):
        if valor < 0:
            raise ValueError("Valor deve ser positivo")
        self.__valor = valor

    def set_forma(self, forma):
        if forma == "":
            raise ValueError("A forma de pagamento deve ser informada")
        self.__forma = forma

    def set_id_atendimento(self, id_atendimento):
        if id_atendimento < 0:
            raise ValueError("Id do atendimento deve ser positivo")
        self.__id_atendimento = id_atendimento

    def to_json(self):
        return {
            "id": self.get_id(),
            "valor": self.get_valor(),
            "forma": self.get_forma(),
            "id_atendimento": self.get_id_atendimento()
        }

    @staticmethod
    def from_json(dic):
        return Pagamento(
            dic["id"],
            dic["valor"],
            dic["forma"],
            dic["id_atendimento"]
        )

    def __str__(self):
        return f"{self.get_id()} - {self.get_valor()} - {self.get_forma()}"
    #pagamentodao

from models.pagamento import Pagamento
import json


class PagamentoDAO:

    def __init__(self):
        self.__arquivo = "pagamentos.json"
        self.__objetos = []
        self.__abrir()

    def inserir(self, obj):

        id = 0

        if len(self.__objetos) > 0:
            for aux in self.__objetos:
                if aux.get_id() > id:
                    id = aux.get_id()

        obj.set_id(id + 1)

        self.__objetos.append(obj)

        self.__salvar()

    def listar(self):
        return self.__objetos

    def listar_id(self, id):

        for obj in self.__objetos:
            if obj.get_id() == id:
                return obj

        return None

    def atualizar(self, obj):

        aux = self.listar_id(obj.get_id())

        if aux != None:
            self.__objetos.remove(aux)
            self.__objetos.append(obj)
            self.__salvar()

    def excluir(self, id):

        aux = self.listar_id(id)

        if aux != None:
            self.__objetos.remove(aux)
            self.__salvar()

    def __abrir(self):

        try:
            arquivo = open(self.__arquivo, mode="r")

            list_dic = json.load(arquivo)

            arquivo.close()

            self.__objetos = []

            for dic in list_dic:
                obj = Pagamento.from_json(dic)
                self.__objetos.append(obj)

        except FileNotFoundError:
            pass

    def __salvar(self):

        arquivo = open(self.__arquivo, mode="w")

        json.dump(
            self.__objetos,
            arquivo,
            default=Pagamento.to_json,
            indent=2
        )

        arquivo.close()

#service
from models.pagamento import Pagamento
from models.pagamentodao import PagamentoDAO
# PAGAMENTO

@staticmethod
def pagamento_inserir(valor, forma, id_atendimento):
    obj = Pagamento(0, valor, forma, id_atendimento)
    PagamentoDAO().inserir(obj)

@staticmethod
def pagamento_listar():
    return PagamentoDAO().listar()

@staticmethod
def pagamento_listar_id(id):
    return PagamentoDAO().listar_id(id)

@staticmethod
def pagamento_atualizar(id, valor, forma, id_atendimento):
    obj = Pagamento(id, valor, forma, id_atendimento)
    PagamentoDAO().atualizar(obj)

@staticmethod
def pagamento_excluir(id):
    PagamentoDAO().excluir(id)

    #manterpagamento
import streamlit as st

import pandas as pd

import time

from service import Service


class ManterPagamentoUI:

    def main():

        st.header("CADASTRO DE PAGAMENTOS")

        tab1, tab2, tab3, tab4 = st.tabs(
            ["LISTAR", "INSERIR", "ATUALIZAR", "EXCLUIR"]
        )

        with tab1:
            ManterPagamentoUI.listar()

        with tab2:
            ManterPagamentoUI.inserir()

        with tab3:
            ManterPagamentoUI.atualizar()

        with tab4:
            ManterPagamentoUI.excluir()

    def listar():

        pagamentos = Service.pagamento_listar()

        if len(pagamentos) == 0:
            st.write("NENHUM PAGAMENTO CADASTRADO")

        else:

            list_dic = []

            for obj in pagamentos:
                list_dic.append(obj.to_json())

            df = pd.DataFrame(list_dic)

            st.dataframe(df)

    def inserir():

        valor = st.number_input(
            "INFORME O VALOR",
            min_value=0.0
        )

        forma = st.text_input(
            "INFORME A FORMA DE PAGAMENTO"
        )

        id_atendimento = st.number_input(
            "INFORME O ID DO ATENDIMENTO",
            min_value=0,
            step=1
        )

        if st.button("INSERIR"):

            Service.pagamento_inserir(
                valor,
                forma,
                id_atendimento
            )

            st.success(
                "PAGAMENTO INSERIDO COM SUCESSO"
            )

            time.sleep(2)

            st.rerun()

    def atualizar():

        pagamentos = Service.pagamento_listar()

        if len(pagamentos) == 0:
            st.write("NENHUM PAGAMENTO CADASTRADO")

        else:

            op = st.selectbox(
                "ATUALIZAÇÃO DE PAGAMENTO",
                pagamentos
            )

            valor = st.number_input(
                "NOVO VALOR",
                value=op.get_valor()
            )

            forma = st.text_input(
                "NOVA FORMA DE PAGAMENTO",
                op.get_forma()
            )

            id_atendimento = st.number_input(
                "NOVO ID DO ATENDIMENTO",
                min_value=0,
                step=1,
                value=op.get_id_atendimento()
            )

            if st.button("ATUALIZAR"):

                id = op.get_id()

                Service.pagamento_atualizar(
                    id,
                    valor,
                    forma,
                    id_atendimento
                )

                st.success(
                    "PAGAMENTO ATUALIZADO COM SUCESSO"
                )

    def excluir():

        pagamentos = Service.pagamento_listar()

        if len(pagamentos) == 0:
            st.write("NENHUM PAGAMENTO CADASTRADO")

        else:

            op = st.selectbox(
                "EXCLUSÃO DE PAGAMENTOS",
                pagamentos
            )

            if st.button("EXCLUIR"):

                id = op.get_id()

                Service.pagamento_excluir(id)

                st.success(
                    "PAGAMENTO EXCLUÍDO COM SUCESSO"
                )

#index.py
from templates.manterpagamentoui import ManterPagamentoUI


#avalicao]
class Avaliacao:

    def __init__(self, id, nota, comentario, id_atendimento):
        self.set_id(id)
        self.set_nota(nota)
        self.set_comentario(comentario)
        self.set_id_atendimento(id_atendimento)
def get_id(self):
    return self.__id

def get_nota(self):
    return self.__nota

def get_comentario(self):
    return self.__comentario

def get_id_atendimento(self):
    return self.__id_atendimento
def set_id(self, id):
    self.__id = id

def set_nota(self, nota):
    self.__nota = nota

def set_comentario(self, comentario):
    self.__comentario = comentario

def set_id_atendimento(self, id_atendimento):
    self.__id_atendimento = id_atendimento


#agendamento
class Agendamento:

    def __init__(self, id, data, confirmado, id_cliente,
                 id_servico, id_profissional):

        self.set_id(id)
        self.set_data(data)
        self.set_confirmado(confirmado)
        self.set_id_cliente(id_cliente)
        self.set_id_servico(id_servico)
        self.set_id_profissional(id_profissional)

    # GETS

    def get_id(self):
        return self.__id

    def get_data(self):
        return self.__data

    def get_confirmado(self):
        return self.__confirmado

    def get_id_cliente(self):
        return self.__id_cliente

    def get_id_servico(self):
        return self.__id_servico

    def get_id_profissional(self):
        return self.__id_profissional

    # SETS

    def set_id(self, id):
        if id < 0:
            raise ValueError("Id deve ser positivo")
        self.__id = id

    def set_data(self, data): #usar o datetime
        self.__data = data

    def set_confirmado(self, confirmado):
        self.__confirmado = confirmado

    def set_id_cliente(self, id_cliente):
        if id_cliente < 0:
            raise ValueError("Id do cliente deve ser positivo")
        self.__id_cliente = id_cliente

    def set_id_servico(self, id_servico):
        if id_servico < 0:
            raise ValueError("Id do serviço deve ser positivo")
        self.__id_servico = id_servico

    def set_id_profissional(self, id_profissional):
        if id_profissional < 0:
            raise ValueError("Id do profissional deve ser positivo")
        self.__id_profissional = id_profissional

    # JSON

    def to_json(self):
        return {
            "id": self.get_id(),
            "data": self.get_data(),
            "confirmado": self.get_confirmado(),
            "id_cliente": self.get_id_cliente(),
            "id_servico": self.get_id_servico(),
            "id_profissional": self.get_id_profissional()
        }

    @staticmethod
    def from_json(dic):
        return Agendamento(
            dic["id"],
            dic["data"],
            dic["confirmado"],
            dic["id_cliente"],
            dic["id_servico"],
            dic["id_profissional"]
        )

    def __str__(self):
        return f"{self.get_id()} - {self.get_data()}"


    #dao
    from models.agendamento import Agendamento
import json


class AgendamentoDAO:

    def __init__(self):
        self.__arquivo = "agendamentos.json"
        self.__objetos = []
        self.__abrir()

    def inserir(self, obj):

        id = 0

        if len(self.__objetos) > 0:
            for aux in self.__objetos:
                if aux.get_id() > id:
                    id = aux.get_id()

        obj.set_id(id + 1)

        self.__objetos.append(obj)

        self.__salvar()

    def listar(self):
        return self.__objetos

    def listar_id(self, id):

        for obj in self.__objetos:
            if obj.get_id() == id:
                return obj

        return None

    def atualizar(self, obj):

        aux = self.listar_id(obj.get_id())

        if aux != None:
            self.__objetos.remove(aux)
            self.__objetos.append(obj)
            self.__salvar()

    def excluir(self, id):

        aux = self.listar_id(id)

        if aux != None:
            self.__objetos.remove(aux)
            self.__salvar()

    def __abrir(self):

        try:

            arquivo = open(self.__arquivo, mode="r")

            list_dic = json.load(arquivo)

            arquivo.close()

            self.__objetos = []

            for dic in list_dic:
                obj = Agendamento.from_json(dic)
                self.__objetos.append(obj)

        except FileNotFoundError:
            pass

    def __salvar(self):

        arquivo = open(self.__arquivo, mode="w")

        json.dump(
            self.__objetos,
            arquivo,
            default=Agendamento.to_json,
            indent=2
        )

        arquivo.close()


        #service
    from models.agendamento import Agendamento
from models.agendamentodao import AgendamentoDAO
# AGENDAMENTO

@staticmethod
def agendamento_inserir(
    data,
    confirmado,
    id_cliente,
    id_servico,
    id_profissional
):
    obj = Agendamento(
        0,
        data,
        confirmado,
        id_cliente,
        id_servico,
        id_profissional
    )

    AgendamentoDAO().inserir(obj)


@staticmethod
def agendamento_listar():
    return AgendamentoDAO().listar()


@staticmethod
def agendamento_listar_id(id):
    return AgendamentoDAO().listar_id(id)


@staticmethod
def agendamento_atualizar(
    id,
    data,
    confirmado,
    id_cliente,
    id_servico,
    id_profissional
):
    obj = Agendamento(
        id,
        data,
        confirmado,
        id_cliente,
        id_servico,
        id_profissional
    )

    AgendamentoDAO().atualizar(obj)


@staticmethod
def agendamento_excluir(id):
    AgendamentoDAO().excluir(id)

    #manter
    import streamlit as st

import pandas as pd

import time

from service import Service


class ManterAgendamentoUI:

    def main():

        st.header("CADASTRO DE AGENDAMENTOS")

        tab1, tab2, tab3, tab4 = st.tabs(
            ["LISTAR", "INSERIR", "ATUALIZAR", "EXCLUIR"]
        )

        with tab1:
            ManterAgendamentoUI.listar()

        with tab2:
            ManterAgendamentoUI.inserir()

        with tab3:
            ManterAgendamentoUI.atualizar()

        with tab4:
            ManterAgendamentoUI.excluir()

    def listar():

        agendamentos = Service.agendamento_listar()

        if len(agendamentos) == 0:
            st.write("NENHUM AGENDAMENTO CADASTRADO")

        else:

            list_dic = []

            for obj in agendamentos:
                list_dic.append(obj.to_json())

            df = pd.DataFrame(list_dic)

            st.dataframe(df)

    def inserir():

        data = st.text_input("INFORME A DATA")

        confirmado = st.checkbox("CONFIRMADO")

        id_cliente = st.number_input(
            "INFORME O ID DO CLIENTE",
            min_value=0,
            step=1
        )

        id_servico = st.number_input(
            "INFORME O ID DO SERVIÇO",
            min_value=0,
            step=1
        )

        id_profissional = st.number_input(
            "INFORME O ID DO PROFISSIONAL",
            min_value=0,
            step=1
        )

        if st.button("INSERIR"):

            Service.agendamento_inserir(
                data,
                confirmado,
                id_cliente,
                id_servico,
                id_profissional
            )

            st.success(
                "AGENDAMENTO INSERIDO COM SUCESSO"
            )

            time.sleep(2)

            st.rerun()

    def atualizar():

        agendamentos = Service.agendamento_listar()

        if len(agendamentos) == 0:
            st.write("NENHUM AGENDAMENTO CADASTRADO")

        else:

            op = st.selectbox(
                "ATUALIZAÇÃO DE AGENDAMENTO",
                agendamentos
            )

            data = st.text_input(
                "NOVA DATA",
                op.get_data()
            )

            confirmado = st.checkbox(
                "CONFIRMADO",
                op.get_confirmado()
            )

            id_cliente = st.number_input(
                "NOVO ID DO CLIENTE",
                min_value=0,
                step=1,
                value=op.get_id_cliente()
            )

            id_servico = st.number_input(
                "NOVO ID DO SERVIÇO",
                min_value=0,
                step=1,
                value=op.get_id_servico()
            )

            id_profissional = st.number_input(
                "NOVO ID DO PROFISSIONAL",
                min_value=0,
                step=1,
                value=op.get_id_profissional()
            )

            if st.button("ATUALIZAR"):

                id = op.get_id()

                Service.agendamento_atualizar(
                    id,
                    data,
                    confirmado,
                    id_cliente,
                    id_servico,
                    id_profissional
                )

                st.success(
                    "AGENDAMENTO ATUALIZADO COM SUCESSO"
                )

    def excluir():

        agendamentos = Service.agendamento_listar()

        if len(agendamentos) == 0:
            st.write("NENHUM AGENDAMENTO CADASTRADO")

        else:

            op = st.selectbox(
                "EXCLUSÃO DE AGENDAMENTOS",
                agendamentos
            )

            if st.button("EXCLUIR"):

                id = op.get_id()

                Service.agendamento_excluir(id)

                st.success(
                    "AGENDAMENTO EXCLUÍDO COM SUCESSO"
                )  


#produto
class Produto:

    def __init__(self, id, descricao, valor, quantidade):

        self.set_id(id)
        self.set_descricao(descricao)
        self.set_valor(valor)
        self.set_quantidade(quantidade)

    # GETS

    def get_id(self):
        return self.__id

    def get_descricao(self):
        return self.__descricao

    def get_valor(self):
        return self.__valor

    def get_quantidade(self):
        return self.__quantidade

    # SETS

    def set_id(self, id):
        if id < 0:
            raise ValueError("Id deve ser positivo")
        self.__id = id

    def set_descricao(self, descricao):
        if descricao == "":
            raise ValueError("A descrição deve ser informada")
        self.__descricao = descricao

    def set_valor(self, valor):
        if valor < 0:
            raise ValueError("O valor deve ser positivo")
        self.__valor = valor

    def set_quantidade(self, quantidade):
        if quantidade < 0:
            raise ValueError("A quantidade deve ser positiva")
        self.__quantidade = quantidade

    # JSON

    def to_json(self):

        return {
            "id": self.get_id(),
            "descricao": self.get_descricao(),
            "valor": self.get_valor(),
            "quantidade": self.get_quantidade()
        }

    @staticmethod
    def from_json(dic):

        return Produto(
            dic["id"],
            dic["descricao"],
            dic["valor"],
            dic["quantidade"]
        )

    def __str__(self):
        return f"{self.get_id()} - {self.get_descricao()}"

    #dao
    from models.produto import Produto
import json


class ProdutoDAO:

    def __init__(self):
        self.__arquivo = "produtos.json"
        self.__objetos = []
        self.__abrir()

    def inserir(self, obj):

        id = 0

        if len(self.__objetos) > 0:
            for aux in self.__objetos:
                if aux.get_id() > id:
                    id = aux.get_id()

        obj.set_id(id + 1)

        self.__objetos.append(obj)

        self.__salvar()

    def listar(self):
        return self.__objetos

    def listar_id(self, id):

        for obj in self.__objetos:
            if obj.get_id() == id:
                return obj

        return None

    def atualizar(self, obj):

        aux = self.listar_id(obj.get_id())

        if aux != None:
            self.__objetos.remove(aux)
            self.__objetos.append(obj)
            self.__salvar()

    def excluir(self, id):

        aux = self.listar_id(id)

        if aux != None:
            self.__objetos.remove(aux)
            self.__salvar()

    def __abrir(self):

        try:

            arquivo = open(self.__arquivo, mode="r")

            list_dic = json.load(arquivo)

            arquivo.close()

            self.__objetos = []

            for dic in list_dic:
                obj = Produto.from_json(dic)
                self.__objetos.append(obj)

        except FileNotFoundError:
            pass

    def __salvar(self):

        arquivo = open(self.__arquivo, mode="w")

        json.dump(
            self.__objetos,
            arquivo,
            default=Produto.to_json,
            indent=2
        )

        arquivo.close()

    #
    from models.produto import Produto
from models.produtodao import ProdutoDAO
# PRODUTO

@staticmethod
def produto_inserir(descricao, valor, quantidade):
    obj = Produto(
        0,
        descricao,
        valor,
        quantidade
    )

    ProdutoDAO().inserir(obj)


@staticmethod
def produto_listar():
    return ProdutoDAO().listar()


@staticmethod
def produto_listar_id(id):
    return ProdutoDAO().listar_id(id)


@staticmethod
def produto_atualizar(id, descricao, valor, quantidade):

    obj = Produto(
        id,
        descricao,
        valor,
        quantidade
    )

    ProdutoDAO().atualizar(obj)


@staticmethod
def produto_excluir(id):
    ProdutoDAO().excluir(id)

#manter
import streamlit as st

import pandas as pd

import time

from service import Service


class ManterProdutoUI:

    def main():

        st.header("CADASTRO DE PRODUTOS")

        tab1, tab2, tab3, tab4 = st.tabs(
            ["LISTAR", "INSERIR", "ATUALIZAR", "EXCLUIR"]
        )

        with tab1:
            ManterProdutoUI.listar()

        with tab2:
            ManterProdutoUI.inserir()

        with tab3:
            ManterProdutoUI.atualizar()

        with tab4:
            ManterProdutoUI.excluir()

    def listar():

        produtos = Service.produto_listar()

        if len(produtos) == 0:
            st.write("NENHUM PRODUTO CADASTRADO")

        else:

            list_dic = []

            for obj in produtos:
                list_dic.append(obj.to_json())

            df = pd.DataFrame(list_dic)

            st.dataframe(df)

    def inserir():

        descricao = st.text_input(
            "INFORME A DESCRIÇÃO"
        )

        valor = st.number_input(
            "INFORME O VALOR",
            min_value=0.0
        )

        quantidade = st.number_input(
            "INFORME A QUANTIDADE",
            min_value=0,
            step=1
        )

        if st.button("INSERIR"):

            Service.produto_inserir(
                descricao,
                valor,
                quantidade
            )

            st.success(
                "PRODUTO INSERIDO COM SUCESSO"
            )

            time.sleep(2)

            st.rerun()

    def atualizar():

        produtos = Service.produto_listar()

        if len(produtos) == 0:
            st.write("NENHUM PRODUTO CADASTRADO")

        else:

            op = st.selectbox(
                "ATUALIZAÇÃO DE PRODUTO",
                produtos
            )

            descricao = st.text_input(
                "NOVA DESCRIÇÃO",
                op.get_descricao()
            )

            valor = st.number_input(
                "NOVO VALOR",
                min_value=0.0,
                value=float(op.get_valor())
            )

            quantidade = st.number_input(
                "NOVA QUANTIDADE",
                min_value=0,
                step=1,
                value=op.get_quantidade()
            )

            if st.button("ATUALIZAR"):

                id = op.get_id()

                Service.produto_atualizar(
                    id,
                    descricao,
                    valor,
                    quantidade
                )

                st.success(
                    "PRODUTO ATUALIZADO COM SUCESSO"
                )

    def excluir():

        produtos = Service.produto_listar()

        if len(produtos) == 0:
            st.write("NENHUM PRODUTO CADASTRADO")

        else:

            op = st.selectbox(
                "EXCLUSÃO DE PRODUTOS",
                produtos
            )

            if st.button("EXCLUIR"):

                id = op.get_id()

                Service.produto_excluir(id)

                st.success(
                    "PRODUTO EXCLUÍDO COM SUCESSO"
                )

from templates.manterprodutoui import ManterProdutoUI
