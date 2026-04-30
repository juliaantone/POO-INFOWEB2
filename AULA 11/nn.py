@classmethod
    def atualizar(cls):
        i = int(input("ID DO CONTATO: "))
        for c in ContatoUI.contatos:
            if c.get_id() == i:
                c.set_nome = input("NOVO NOME: ")
                c.set_email = input("NOVO EMAIL: ")
                c.set_fone = input("NOVO TELEFONE: ")
                return
        print("CONTATO NÃO ENCONTRADO")

    @classmethod
    def excluir(cls):
        i = int(input("ID DO CONTATO: "))
        for c in ContatoUI.contatos:
            if c.get_id() == i:
                ContatoUI.contatos.remove(c)
                return
        print("CONTATO NÃO ENCONTRADO")

    