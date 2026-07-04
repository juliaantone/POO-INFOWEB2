from models.cliente import Cliente
from models.clientedao import ClienteDAO

class Service:
    @staticmethod
    def cliente_inserir(id, nome, email, fone):
        obj = Cliente(id, nome, email, fone)
        ClienteDAO().inserir(obj)

    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()
    
    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        obj = Cliente(id, nome, email, fone)
        ClienteDAO().atualizar(obj)

    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)

from service import Service
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI. menu()
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()