from models.servico import Servico
from models.servicodao import ServicoDAO

class Service:

    @staticmethod
    def servico_inserir(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        ServicoDAO().inserir(obj)

    @staticmethod
    def servico_listar():
        return ServicoDAO().listar()

    @staticmethod
    def servico_listar_id(id):
        return ServicoDAO().listar_id(id)

    @staticmethod
    def servico_atualizar(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        ServicoDAO().atualizar(obj)

    @staticmethod
    def servico_excluir(id):
        ServicoDAO().excluir(id)