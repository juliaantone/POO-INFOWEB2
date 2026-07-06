from service import Service

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            #if op == 2: UI.cliente_listar()
            #if op == 3: UI.cliente_atualizar()
            #if op == 4: UI.cliente_excluir()
            if op == 1: UI.servico_inserir()
            if op == 2: UI.servico_listar()
            if op == 3: UI.servico_atualizar()
            if op == 4: UI.servico_excluir()

    @staticmethod
    def menu():
        print("1- Inserir Serviço")
        print("2- Listar Serviço")
        print("3- Atualizar Serviço")
        print("4- Excluir Serviço")
        print("9- Fim")
        return int(input("Informe uma opção: "))

    @staticmethod
    def servico_inserir():
        id = int(input("Informe o id: "))
        descricao = input("Informe a descrição: ")
        valor = float(input("Informe o valor: "))
        Service.servico_inserir(id,descricao,valor)

    @staticmethod
    def servico_listar():
        for obj in Service.servico_listar():
            print(obj)

    @staticmethod
    def servico_atualizar():
        for obj in Service.servico_listar():
            print(obj)
        id = int(input("Informe o id: "))
        descricao = input("Nova descrição: ")
        valor = float(input("Novo valor: "))
        Service.servico_atualizar(id,descricao,valor)

    @staticmethod
    def servico_excluir():
        for obj in Service.servico_listar():
            print(obj)
        id = int(input("Informe o id: "))
        Service.servico_excluir(id)

UI.main()