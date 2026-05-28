
from datetime import datetime, timedelta

class Treino:
    def __init__(self, id, data, distancia, tempo):
        self.set_id(id)
        self.set_data(data)
        self.set_distancia(distancia)
        self.set_tempo(tempo)

    # SETS
    def set_id(self, id):
        if id < 0:
            raise ValueError("Id deve ser positivo")
        self.__id = id

    def set_data(self, data):
        if data > datetime.now():
            raise ValueError("Data não pode ser no futuro")
        self.__data = data

    def set_distancia(self, distancia):
        if distancia <= 0:
            raise ValueError("A distância deve ser positiva")
        self.__distancia = distancia

    def set_tempo(self, tempo):
        if tempo <= timedelta(0):
            raise ValueError("O tempo deve ser positivo")
        self.__tempo = tempo

    # GETS
    def get_id(self):
        return self.__id

    def get_data(self):
        return self.__data

    def get_distancia(self):
        return self.__distancia

    def get_tempo(self):
        return self.__tempo

    # PACE = tempo por km
    def pace(self):
        return self.__tempo / self.__distancia

    # TO STRING
    def __str__(self):
        return (
            f"ID: {self.__id} | "
            f"Data: {self.__data.strftime('%d/%m/%Y')} | "
            f"Distância: {self.__distancia} km | "
            f"Tempo: {self.__tempo} | "
            f"Pace: {self.pace()}"
        )


class TreinoUI:
    __lista = []

    @staticmethod
    def main():
        op = 0

        while op != 7:
            print("\n1- Inserir")
            print("2- Listar")
            print("3- Listar por ID")
            print("4- Atualizar")
            print("5- Excluir")
            print("6- Mais rápido")
            print("7- Sair")

            op = int(input("Escolha uma opção: "))

            if op == 1:
                TreinoUI.inserir()

            elif op == 2:
                TreinoUI.listar()

            elif op == 3:
                TreinoUI.listar_id()

            elif op == 4:
                TreinoUI.atualizar()

            elif op == 5:
                TreinoUI.excluir()

            elif op == 6:
                TreinoUI.maisrapido()

            elif op == 7:
                print("Programa encerrado!")

            else:
                print("Opção inválida!")

    @classmethod
    def inserir(cls):
        id = int(input("Informe o ID: "))

        data_str = input("Informe a data (dd/mm/aaaa): ")
        data = datetime.strptime(data_str, "%d/%m/%Y")

        distancia = float(input("Informe a distância em km: "))

        tempo_str = input("Informe o tempo (hh:mm:ss): ")
        h, m, s = map(int, tempo_str.split(":"))
        tempo = timedelta(hours=h, minutes=m, seconds=s)

        treino = Treino(id, data, distancia, tempo)

        cls.__lista.append(treino)

        print("Treino cadastrado com sucesso!")

    @classmethod
    def listar(cls):
        if len(cls.__lista) == 0:
            print("Nenhum treino cadastrado")

        else:
            for treino in cls.__lista:
                print(treino)

    @classmethod
    def listar_id(cls):
        id = int(input("Informe o ID: "))

        for treino in cls.__lista:
            if treino.get_id() == id:
                print(treino)
                return

        print("Treino não encontrado")

    @classmethod
    def atualizar(cls):
        id = int(input("Informe o ID do treino: "))

        for treino in cls.__lista:
            if treino.get_id() == id:

                data_str = input("Nova data (dd/mm/aaaa): ")
                data = datetime.strptime(data_str, "%d/%m/%Y")

                distancia = float(input("Nova distância: "))

                tempo_str = input("Novo tempo (hh:mm:ss): ")
                h, m, s = map(int, tempo_str.split(":"))
                tempo = timedelta(hours=h, minutes=m, seconds=s)

                treino.set_data(data)
                treino.set_distancia(distancia)
                treino.set_tempo(tempo)

                print("Treino atualizado!")
                return

        print("Treino não encontrado")

    @classmethod
    def excluir(cls):
        id = int(input("Informe o ID do treino: "))

        for treino in cls.__lista:
            if treino.get_id() == id:
                cls.__lista.remove(treino)
                print("Treino removido!")
                return

        print("Treino não encontrado")

    @classmethod
    def maisrapido(cls):
        if len(cls.__lista) == 0:
            print("Nenhum treino cadastrado")
            return

        mais_rapido = cls.__lista[0]

        for treino in cls.__lista:
            if treino.pace() < mais_rapido.pace():
                mais_rapido = treino

        print("\nTreino mais rápido:")
        print(mais_rapido)


TreinoUI.main()
