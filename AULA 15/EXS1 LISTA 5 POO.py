from datetime import datetime

class Paciente:
    def __init__(self, id, nome, cpf, telefone, nascimento):
        self.set_id(id)
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.set_nascimento(nascimento)
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id 
    def set_nome(self, nome):
        if nome == "": raise ValueError("Não pode ser vazio")
        self.__nome = nome
    def set_cpf(self, cpf):
        if cpf == "": raise ValueError("CPF não pode ser vazio")
        self.__cpf = cpf
    def set_telefone(self, telefone):
        if telefone == "": raise ValueError("Telefone não pode ser vazio")
        self.__telefone = telefone
    def set_nascimento(self, nascimento):
        if nascimento > datetime.now() : raise ValueError("Data não pode ser no futuro")
        self.__nascimento = nascimento
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_telefone(self):
        return self.__telefone
    def get_cpf(self):
        return self.__cpf
    def get_nascimento(self):
        return self.__nascimento
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__cpf} - {self.__telefone} - {self.__nascimento.strftime("%d/%m/%Y")}"
    def idade(self):
        tempo = datetime.now() - self.__nascimento     #medidos em dias, horas, ... timedelta
        anos = tempo.days // 365
        meses = tempo.days % 365 // 30 # maior valor possível 364
        return f"{anos} ano(s) e {meses} mes(es)"
    
class PacienteUI:
    __pacientes = []   # atributo - fora do init - não tem objetos de PacienteUI
    @staticmethod      # quando não tem acessa o atributo
    def main():
        print("1- INSERIR, 2-LISTAR, 3-ATUALIZAR, 4-EXCLUIR, 5-PESQUISAR, 6-ANIVERSARIANTE, 7-SAIR")
        return int(input("ESCOLHA UMA OPÇÃO: "))
    @staticmethod
    def menu():
        op = 0
        while op != 6:
            if op == 1: PacienteUI.inserir()
            if op == 2: PacienteUI.listar()
            if op == 3: PacienteUI.atualizar()
            if op == 4: PacienteUI.excluir()
            if op == 5: PacienteUI.pesquisar()
            if op == 6: PacienteUI.anivesariantes()
            
    @classmethod
    def inserir(cls):
        id = int(input("INFORME O ID: "))
        nome = input("INFORME O NOME: ")
        cpf = input("INFORME O CPF: ")
        telefone = input("INFORME O TELEFONE: ")
        nascimento = datetime.strptime(input("INFORME O NOME: "), "%d/%m/%Y")
        x = Paciente(id, nome, cpf, telefone, nascimento)
        cls.__pacientes.append(x)

    @classmethod
    def listar(cls):
        if len(cls.__pacientes) == 0: print("Nenhum paciente cadastrado")
        else: 
            for x in cls.__pacientes: print(x, x.idade())

    @classmethod
    def atualizar(cls):
        for x in cls.__pacientes:
            id = int(input("INFORME O ID DO PACIENTE A SER ATUALIZADO: "))
            for x in cls.__pacientes:
                if x.get_id() == id:
                    nome = input("NOVO NOME: ")
                    cpf = input("NOVO CPF: ")
                    telefone = input("NOVO CPF: ")
                    nascimento = datetime.strptime(input("INFORME A NOVA DATA DE NASCIMENTO: "))
                    x.set_nome(nome)
                    x.set_cpf(cpf)
                    x.set_telefone(telefone)
                    x.set_nascimento(nascimento)
                    
    @classmethod
    def excluir(cls):
        for x in cls.__pacientes:
            id = int(input("INFORME O ID: "))
            for x in cls.__pacientes:
                if x.get_id() == id:
                    cls.__pacientes.remove(x)

    @classmethod
    def pesquisar(cls):
        s = input("INFORME AS INICIAIS DO NOME: ")
        for x in cls.__pacientes:
                if x.get_nome().startwith(s):
                    print(x)

    @classmethod
    def anivesariantes(cls):
        m = input("INFORME O MÊS PARA LISTAR ANIVERSARIANTE: ")
        for x in cls.__pacientes:
                if x.get_nascimento().month == m: print(x)

PacienteUI.main()