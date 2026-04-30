class Contato:
    def __init__(self, id, nome, email, fone):
        self.set_id(id)              #atributo de instância
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
    def set_id(self, id):
        if id < 0: raise ValueError("ID DEVE SER POSIVIVO")
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("NOME NÃO PODE SER VAZIO")
        self.__nome = nome 
    def set_email(self, email): self.__email = email
    def set_fone(self, fone): self.__fone = fone
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

class ContatoUI:
    contatos = []   #atributo de class
    @staticmethod
    def main():
        op = 0
        while op != 6:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()
            if op == 3: ContatoUI.atualizar()
            if op == 4: ContatoUI.excluir()
            if op == 5: ContatoUI.pesquisar()
            #if op == 6: ContatoUI.fim()

    @staticmethod
    def menu():
        print("1- INSERIR")
        print("2- LISTAR")
        print("3- ATUALIZAR")
        print("4- EXCLUIR")
        print("5- PESQUISAR")
        print("6- FIM")
        return int(input("INFORME UMA OPÇÃO: "))

    @classmethod
    def inserir(cls):
        id = int(input("INFORME O ID: "))
        nome = input("INFORME O NOME: ")
        email = input("INFORME O E-MAIL: ")
        fone = int(input("INFORME O TELEFONE: "))
        x = Contato(id, nome, email, fone)
        cls.contatos.append(x)

    @classmethod
    def listar(cls):
        if len(cls.contatos) == 0: print("NENHUM CONTATO CADASTRADO")
        else:
            for x in cls.contatos: print(x)

    @classmethod
    def atualizar(cls):
        pass

    @classmethod
    def excluir(cls):
        pass

    @classmethod
    def pesquisar(cla):
        pass

    

    
ContatoUI.main