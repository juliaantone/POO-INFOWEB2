from enum import Enum
from datetime import datetime

class Grupo(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7
    H = 8
    I = 9
    J = 10
    K = 11
    L = 12

class Fase(Enum):
    GRUPO = 1
    DEZESSEIS_AVOS = 2
    OITAVAS = 3
    QUARTAS = 4
    SEMIFINAIS = 5
    TERCEIRO_LUGAR = 6
    FINAL = 7

class Pais:
    def __init__(self, id, nome, sigla, grupo):
        self.__id = id
        self.__nome = nome
        self.__sigla = sigla
        self.__grupo = grupo
    def set_id(self, id):
        self.__id = id
    def set_nome(self, nome):
        self.__nome = nome
    def set_sigla(self, sigla):
        self.__sigla = sigla
    def set_grupo(self, grupo):
        self.__grupo = grupo
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_sigla(self): return self.__sigla
    def get_grupo(self): return self.__grupo
    def __str__(self):
        return f"ID: {self.__id} - NOME: {self.__nome} - SIGLA: {self.__sigla} - GRUPO: {self.__grupo}"
    
class Jogo:
    def __init__(self, id, pais1, pais2, gols1, gols2, fase, data_hora):
        self.__id = id
        self.__pais1 = pais1
        self.__pais2 = pais2
        self.__gols1 = gols1
        self.__gols2 = gols2
        self.__fase = fase
        self.__data_hora = data_hora
    def set_id(self, id):
        self.__id = id
    def set_pais1(self, pais):
        self.__pais1 = pais
    def set_pais2(self, pais):
        self.__pais2 = pais
    def set_gols1(self, gols):
        self.__gols1 = gols
    def set_gols2(self, gols):
        self.__gols2 = gols
    def set_fase(self, fase):
        self.__fase = fase
    def set_data_hora(self, data_hora):
        self.__data_hora = data_hora
    def get_id(self): return self.__id
    def get_pais1(self): return self.__pais1
    def get_pais2(self): return self.__pais2
    def get_gols1(self): return self.__gols1
    def get_gols2(self): return self.__gols2
    def get_fase(self): return self.__fase
    def get_data_hora(self): return self.__data_hora
    def __str__(self):
        f"JOGO: {self.__id}\n"
        f"{self.__pais1.get_nome()} {self.__gols1} x {self.__gols2} {self.__pais2.get_nome()}\n"
        f"FASE: {self.__fase.name}\n"
        f"DATA E HORA: {self.__data_hora.strftime('%d/%m/%Y %H:%H')}"


class JogosUI:
    __jogos = []
    @staticmethod
    def main():
        op = 0
        while op != 6:
            if op == 1: JogosUI.inserir()
            if op == 2: JogosUI.listar()
            if op == 3: JogosUI.atualizar()
            if op == 4: JogosUI.excluir()
    
    @staticmethod
    def menu():
        print("1-INSERIR, 2-LISTAR, 3-ATUALIZAR, 4-EXCLUIR, 5- FIM")
        return int(input("ESCOLHA UMA OPÇÃO:"))
    
    @classmethod
    def inserir(cls):
        id = int(input("ID do jogo: "))
        nome1 = input("País 1: ")
        sigla1 = input("Sigla: ")
        grupo1 = Grupo[input("Grupo(A-L): ").upper()]
        pais1 = Pais(1, nome1, sigla1, grupo1)

        nome2 = input("País 2: ")
        sigla2 = input("Sigla: ")
        grupo2 = Grupo[input("Grupo(A-L): ").upper()]
        pais2 = Pais(2, nome2, sigla2, grupo2)

        gols1 = int(input("Gols país 1: "))
        gols2 = int(input("Gols país 2: "))

        fase = Fase[input("Fase: ").upper()]
        data = input("Data e hora (dd/mm/aaaa hh:mm): ")
        data_hora = datetime.strptime(data,"%d/%m/%Y %H:%M")

        jogo = Jogo(
            id,
            pais1,
            pais2,
            gols1,
            gols2,
            fase,
            data_hora
        )
        cls.__jogos.append(jogo)


    @classmethod
    def listar(cls):
        for jogo in cls.__jogos:
            print(jogo)
            print("-" * 30)

    @classmethod
    def atualizar(cls):
        id = int(input("Informe o ID do jogo: "))

        for jogo in cls.__jogos:
            if jogo.get_id() == id:
                gols1 = int(input("Novo gol país 1: "))
                gols2 = int(input("Novo gol país 2: "))

                jogo.set_gols1(gols1)
                jogo.set_gols2(gols2)

                print("Atualizado!")
                return

        print("Jogo não encontrado")

    @classmethod
    def excluir(cls):
        id = int(input("Informe o ID do jogo: "))

        for jogo in cls.__jogos:
            if jogo.get_id() == id:
                cls.__jogos.remove(jogo)
                print("Removido!")
                return

        print("Jogo não encontrado")


JogosUI.main()


    