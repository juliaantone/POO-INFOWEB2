from models.cliente import Cliente         # entidade
from models.clientedao import ClienteDAO   # persistência
from models.servico import Servico
from models.servicodao import ServicoDAO
from models.profissional import Profissional
from models.profissionaldao import ProfissionalDAO

class Service:
    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        obj = Cliente(0, nome, email, fone, senha)
        ClienteDAO().inserir(obj)
    #def cliente_inserir(id, nome, email, fone):
        #obj = Cliente(id, nome, email, fone)
        #ClienteDAO().inserir(obj)
    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()
    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)
    @staticmethod
    def cliente_listar_nome(iniciais):
        return ClienteDAO().listar_nome(iniciais)
    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        obj = Cliente(id, nome, email, fone, senha)
        ClienteDAO().atualizar(obj)
    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)


    @staticmethod
    def servico_inserir(descricao, valor):
        obj = Servico(0, descricao, valor)
        ServicoDAO().inserir(obj)
    #def servico_inserir(id, descricao, valor):
        #obj = Servico(id, descricao, valor)
        #ServicoDAO().inserir(obj)
    @staticmethod
    def servico_listar():
        return ServicoDAO().listar()
    @staticmethod
    def servico_listar_id(id):
        return ServicoDAO().listar_id(id)
    @staticmethod
    def servico_listar_descricao(iniciais):
        return ServicoDAO().listar_descricao(iniciais)
    @staticmethod
    def servico_atualizar(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        ServicoDAO().atualizar(obj)
    @staticmethod
    def servico_excluir(id):
        ServicoDAO().excluir(id)


    @staticmethod
    def profissional_inserir(nome, email, senha, especialidade):
        obj = Profissional(0, nome, email, senha, especialidade)
        ProfissionalDAO().inserir(obj)
    @staticmethod
    def profissional_listar():
        return ProfissionalDAO().listar()
    @staticmethod
    def profissional_listar_nome(iniciais):
        return ProfissionalDAO().listar_nome(iniciais)
    @staticmethod
    def profissional_listar_id(id):
        return ProfissionalDAO().listar_id(id)
    @staticmethod
    def profissional_atualizar(id, nome, email, senha, especialidade):
        obj = Profissional(id, nome, email, senha, especialidade)
        ProfissionalDAO().atualizar(obj)
    @staticmethod
    def profissional_excluir(id):
        ProfissionalDAO().excluir(id)