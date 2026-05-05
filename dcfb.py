class Time:
    def __init__(self, i, n, e):
        self.__id = i
        self.__nome = n
        self.__estado = e

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_estado(self): return self.__estado

    def set_nome(self, n): self.__nome = n
    def set_estado(self, e): self.__estado = e

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__estado}"


class Jogador:
    def __init__(self, i, it, n, c):
        self.__id = i
        self.__idTime = it
        self.__nome = n
        self.__camisa = c

    def get_id(self): return self.__id
    def get_idTime(self): return self.__idTime
    def get_nome(self): return self.__nome
    def get_camisa(self): return self.__camisa

    def set_idTime(self, it): self.__idTime = it
    def set_nome(self, n): self.__nome = n
    def set_camisa(self, c): self.__camisa = c

    def __str__(self):
        return f"{self.__id} - {self.__nome} - Time:{self.__idTime} - Camisa:{self.__camisa}"


class FutebolUI:
    times = []
    jogadores = []

    @staticmethod
    def main():
        op = 0
        while op != 11:
            op = FutebolUI.menu()

            if op == 1: FutebolUI.inserir_time()
            elif op == 2: FutebolUI.listar_time()
            elif op == 3: FutebolUI.atualizar_time()
            elif op == 4: FutebolUI.excluir_time()
            elif op == 5: FutebolUI.inserir_jogador()
            elif op == 6: FutebolUI.listar_jogador()
            elif op == 7: FutebolUI.atualizar_jogador()
            elif op == 8: FutebolUI.excluir_jogador()
            elif op == 9: FutebolUI.listar_jogadores_do_time()
            elif op == 10: FutebolUI.transferir_jogador()

    @staticmethod
    def menu():
        print("\n1- Inserir Time")
        print("2- Listar Times")
        print("3- Atualizar Time")
        print("4- Excluir Time")
        print("5- Inserir Jogador")
        print("6- Listar Jogadores")
        print("7- Atualizar Jogador")
        print("8- Excluir Jogador")
        print("9- Listar Jogadores do Time")
        print("10- Transferir Jogador")
        print("11- Sair")
        return int(input("Opção: "))

    @classmethod
    def inserir_time(cls):
        id = int(input("ID: "))
        nome = input("Nome: ")
        estado = input("Estado: ")
        cls.times.append(Time(id, nome, estado))

    @classmethod
    def listar_time(cls):
        for t in cls.times:
            print(t)

    @classmethod
    def atualizar_time(cls):
        id = int(input("ID do Time: "))
        for t in cls.times:
            if t.get_id() == id:
                t.set_nome(input("Novo nome: "))
                t.set_estado(input("Novo estado: "))
                print("Atualizado!")
                return
        print("Time não encontrado")

    @classmethod
    def excluir_time(cls):
        id = int(input("ID do Time: "))
        for t in cls.times:
            if t.get_id() == id:
                cls.times.remove(t)
                print("Excluído!")
                return
        print("Time não encontrado")

    @classmethod
    def inserir_jogador(cls):
        id = int(input("ID Jogador: "))
        idTime = int(input("ID do Time: "))
        nome = input("Nome: ")
        camisa = int(input("Camisa: "))
        cls.jogadores.append(Jogador(id, idTime, nome, camisa))

    @classmethod
    def listar_jogador(cls):
        for j in cls.jogadores:
            print(j)

    @classmethod
    def atualizar_jogador(cls):
        id = int(input("ID do Jogador: "))
        for j in cls.jogadores:
            if j.get_id() == id:
                j.set_nome(input("Novo nome: "))
                j.set_camisa(int(input("Nova camisa: ")))
                print("Atualizado!")
                return
        print("Jogador não encontrado")

    @classmethod
    def excluir_jogador(cls):
        id = int(input("ID do Jogador: "))
        for j in cls.jogadores:
            if j.get_id() == id:
                cls.jogadores.remove(j)
                print("Excluído!")
                return
        print("Jogador não encontrado")

    @classmethod
    def listar_jogadores_do_time(cls):
        idTime = int(input("ID do Time: "))
        for j in cls.jogadores:
            if j.get_idTime() == idTime:
                print(j)

    @classmethod
    def transferir_jogador(cls):
        id = int(input("ID do Jogador: "))
        novoTime = int(input("Novo ID Time: "))
        for j in cls.jogadores:
            if j.get_id() == id:
                j.set_idTime(novoTime)
                print("Transferido!")
                return
        print("Jogador não encontrado")


if __name__ == "__main__":
    FutebolUI.main()