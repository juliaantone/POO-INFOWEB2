from service import Service
@staticmethod
def menu():
    print("1- Inserir Cliente")
    print("2- Listar Cliente")
    print("3- Atualizar Cliente")
    print("4- Excluir Cliente")
    print("5- Inserir Serviço")
    print("6- Listar Serviço")
    print("7- Atualizar Serviço")
    print("8- Excluir Serviço")
    print("9- Fim")

    return int(input("Informe uma opção: "))

@staticmethod
def servico_inserir():
    id = int(input("Informe o id: "))
    descricao = input("Informe a descrição: ")
    valor = float(input("Informe o valor: "))

    Service.servico_inserir(
        id,
        descricao,
        valor
    )

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

    Service.servico_atualizar(
        id,
        descricao,
        valor
    )

@staticmethod
def servico_excluir():
    for obj in Service.servico_listar():
        print(obj)

    id = int(input("Informe o id: ")

    Service.servico_excluir(id)

UI.mani()