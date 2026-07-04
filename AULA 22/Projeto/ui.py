@staticmethod
def menu():
    print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 9-Fim")
    return int(input("Informe uma opção: "))

@staticmethod
def cliente_inserir():
    id = int(input("Informe o id: "))
    nome = input("Informe o nome: ")
    email = input("Informe o e-mail: ")
    fone = input("Informe o telefone: ")
    Service.cliente_inserir(id, nome, email, fone)

@staticmethod
def cliente_listar():
    for obj in Service.cliente_listar(): print(obj)

@staticmethod
def cliente_atualizar():
    for obj in Service().cliente_listar(): print(obj)
    id = int(input("Informe o id do cliente a ser atualizado: "))
    nome = input("Informe o novo nome: ")
    email = input("Informe o novo e-mail: ")
    fone = input("Informe o novo telefone: ")
    Service.cliente_atualizar(id, nome, email, fone)

@staticmethod
def cliente_excluir():
    for obj in Service().cliente_listar(): print(obj)
    id = int(input("Informe o id do cliente a ser excluído: "))
    Service.cliente_excluir(id)

UI.main()