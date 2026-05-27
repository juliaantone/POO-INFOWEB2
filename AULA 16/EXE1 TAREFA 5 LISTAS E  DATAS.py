from datetime import datetime, timedelta

class Treino:
    def __init__(self, id, data, distancia, tempo):
        self.set_id(id)
        self.set_data(data)
        self.set_distancia(distancia)
        self.set_tempo(tempo)
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id 
    def set_data(self, data):
        if data > datetime.now() : raise ValueError("Data não pode ser no futuro")
        self.__data = data
    def set_distancia(self, distancia):
        if distancia > 0: raise ValueError("A distância deve ser positiva")
        self.__distancia = distancia 
    def set_tempo(self, tempo):
        if tempo < timedelta(0): raise ValueError("O tempo deve ser positivo")
    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_distancia(self): return self.__distancia
    def get_tempo(self): return self.__tempo
    def __str__(self):
        return f"{self.__id} - {self.__data} - {self.__distancia} - {self.__tempo}"



class TreinoUI:
    _lista = []
    @staticmethod      
    def main():
        print("1-INSERIR, 2-LISTAR, 3-ATUALIZAR, 4-EXCLUIR, 5-MAIS RÁPIDO 6-SAIR")
        return int(input("ESCOLHA UMA OPÇÃO: "))
    @staticmethod
    def menu():
        op = 0
        while op != 6:
            if op == 1: TreinoUI.inserir()
            if op == 2: TreinoUI.listar()
            if op == 3: TreinoUI.atualizar()
            if op == 4: TreinoUI.excluir()
            if op == 5: TreinoUI.maisrapido()

            
    @classmethod
    def inserir(cls):
        id = int(input("INFORME O ID: "))
        data = input("INFORME A DATA: ")
        distancia = input("INFORME A DISTÂNCIA: ")
        tempo = input("INFORME O TEMPO: ")
        x = Treino(id, data, distancia, tempo)
        cls.__lista.append(x)

    @classmethod
    def listar(cls):
        if len(cls.__lista) == 0: print("Nenhum paciente cadastrado")
        else: 
            for x in cls.__lista: print(x, x.idade())

    @classmethod
    def atualizar(cls):
        for x in cls.__lista:
            id = int(input("INFORME O ID DO PACIENTE A SER ATUALIZADO: "))
            for x in cls.__lista:
                if x.get_id() == id:
                    data = input("INFORME A DATA: ")
                    distancia = input("INFORME A DISTÂNCIA: ")
                    tempo = input("INFORME O TEMPO: ")
                    x.set_data(data)
                    x.set_distancia(cpf)
                    x.set_telefone(telefone)
                    
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