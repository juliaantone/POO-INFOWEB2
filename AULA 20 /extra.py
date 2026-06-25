from enum import Enum
from datetime import datetime


# ==========================
# ENUMERAÇÕES
# ==========================

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
    GRUPOS = 1
    DEZESSEIS_AVOS = 2
    OITAVAS = 3
    QUARTAS = 4
    SEMIFINAIS = 5
    TERCEIRO_LUGAR = 6
    FINAL = 7


# ==========================
# CLASSE PAÍS
# ==========================

class Pais:

    def __init__(self, id, nome, sigla, grupo):
        self.__id = id
        self.__nome = nome
        self.__sigla = sigla
        self.__grupo = grupo

    # Getters
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_sigla(self):
        return self.__sigla

    def get_grupo(self):
        return self.__grupo

    # Setters
    def set_id(self, id):
        self.__id = id

    def set_nome(self, nome):
        self.__nome = nome

    def set_sigla(self, sigla):
        self.__sigla = sigla

    def set_grupo(self, grupo):
        self.__grupo = grupo

    def __str__(self):
        return (f"ID: {self.__id} | "
                f"País: {self.__nome} | "
                f"Sigla: {self.__sigla} | "
                f"Grupo: {self.__grupo.name}")


# ==========================
# CLASSE JOGO
# ==========================

class Jogo:

    def __init__(self, id, pais1, pais2, gols1,
                 gols2, fase, data_hora):

        self.__id = id
        self.__pais1 = pais1
        self.__pais2 = pais2
        self.__gols1 = gols1
        self.__gols2 = gols2
        self.__fase = fase
        self.__data_hora = data_hora

    # Getters
    def get_id(self):
        return self.__id

    def get_pais1(self):
        return self.__pais1

    def get_pais2(self):
        return self.__pais2

    def get_gols1(self):
        return self.__gols1

    def get_gols2(self):
        return self.__gols2

    def get_fase(self):
        return self.__fase

    def get_data_hora(self):
        return self.__data_hora

    # Setters
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

    def __str__(self):
        return (
            f"Jogo {self.__id}\n"
            f"{self.__pais1.get_nome()} {self.__gols1} x "
            f"{self.__gols2} {self.__pais2.get_nome()}\n"
            f"Fase: {self.__fase.name}\n"
            f"Data/Hora: {self.__data_hora.strftime('%d/%m/%Y %H:%M')}"
        )


# ==========================
# CLASSE UI
# ==========================

class UI:

    def __init__(self):
        self.jogos = []

    def cadastrar_jogo(self):

        nome1 = input("Nome do país 1: ")
        sigla1 = input("Sigla do país 1: ")

        nome2 = input("Nome do país 2: ")
        sigla2 = input("Sigla do país 2: ")

        pais1 = Pais(1, nome1, sigla1, Grupo.A)
        pais2 = Pais(2, nome2, sigla2, Grupo.A)

        gols1 = int(input("Gols do país 1: "))
        gols2 = int(input("Gols do país 2: "))

        jogo = Jogo(
            len(self.jogos) + 1,
            pais1,
            pais2,
            gols1,
            gols2,
            Fase.GRUPOS,
            datetime.now()
        )

        self.jogos.append(jogo)

        print("\nJogo cadastrado com sucesso!\n")

    def listar_jogos(self):

        if len(self.jogos) == 0:
            print("\nNenhum jogo cadastrado.\n")
            return

        print("\nLISTA DE JOGOS\n")

        for jogo in self.jogos:
            print(jogo)
            print("-" * 40)

    def menu(self):

        while True:

            print("\n=== COPA DO MUNDO 2026 ===")
            print("1 - Cadastrar jogo")
            print("2 - Listar jogos")
            print("0 - Sair")

            opcao = input("Opção: ")

            if opcao == "1":
                self.cadastrar_jogo()

            elif opcao == "2":
                self.listar_jogos()

            elif opcao == "0":
                print("Encerrando...")
                break

            else:
                print("Opção inválida!")


# Programa principal
ui = UI()
ui.menu()