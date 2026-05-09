class Time:
    def __init__(self, id, nome, estado):
        self.set_id(id)             
        self.set_nome(nome)
        self.set_estado(estado)
    def set_id(self, id):
       if id < 0: raise ValueError()
       self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError()
        self.__nome = nome 
    def set_estado(self, estado):
        if estado == "": raise ValueError()
        self.__estado = estado
    def get_id(self): 
        return self.__id
    def get_nome(self): 
        return self.__nome
    def get_estado(self): 
        return self.__estado
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__estado}"
    

class Jogador:
    def __init__(self, id, nome, camisa, idTime):
        self.set_id(id)             
        self.set_nome(nome)
        self.set_camisa(camisa)
        self.set_idTime(idTime)
    def set_id(self, id):
        if id < 0: raise ValueError()
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError()
        self.__nome = nome 
    def set_camisa(self, camisa):
        if camisa < 0: raise ValueError()
        self.__camisa = camisa
    def set_idTime(self, idTime):
        if idTime < 0: raise ValueError()
        self.__idTime = idTime
    def get_id(self): 
        return self.__id
    def get_nome(self): 
        return self.__nome
    def get_camisa(self):
        return self.__camisa
    def get_idTime(self):
        return self.__idTime
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__camisa} - {self.__idTime}" 
    
class FutebolUI:
    times = []
    jogadores = []

    @staticmethod
    def main():
        op = 0
        while op != 11:
            op = FutebolUI.menu()
            if op == 1: FutebolUI.inserir_time()
            if op == 2: FutebolUI.listar_time()
            if op == 3: FutebolUI.atualizar_time()
            if op == 4: FutebolUI.excluir_time()
            if op == 5: FutebolUI.inserir_jogador()
            if op == 6: FutebolUI.listar_jogador()
            if op == 7: FutebolUI.atualizar_jogador()
            if op == 8: FutebolUI.excluir_jogador()
            if op == 9: FutebolUI.listar_jogadores_do_time()
            if op == 10: FutebolUI.transferir_jogador()

    @staticmethod
    def menu():
        print("-" * 50)
        print("1- INSERIR TIME")
        print("2- LISTAR TIME")
        print("3- ATUALIZAR TIME")
        print("4- EXCLUIR TIME")
        print("5- INSERIR JOGADOR")
        print("6- LISTAR JOGADOR")
        print("7- ATUALIZAR JOGADOR")
        print("8- EXCLUIR JOGADOR")
        print("9- LISTAR JOGADORES DO TIME")
        print("10- TRANSFERIR JOGADOR")
        print("11- FIM")
        return int(input("INFORME UMA OPÇÃO: "))

    @classmethod
    def inserir_time(cls):
        id = int(input("INFORME O ID: "))
        nome = input("INFORME O NOME: ")
        estado = input("INFORME O ESTADO: ")
        x = Time(id, nome, estado)
        cls.times.append(x)

    @classmethod
    def listar_time(cls):
        if len(cls.times) == 0: print("NENHUM TIME CADASTRADO")
        else:
            for x in cls.times: print(x)

    @classmethod
    def listar_id(cls, id):
        for x in cls.times:
            if x.get_id() == id: return x 
        return None

    @classmethod
    def atualizar_time(cls):
        FutebolUI.listar_time()
        id = int(input("INFORME O ID DO TIME A SER ATULIZADO: "))
        x = FutebolUI.listar_id(id)
        if x != None:
            nome = input("NOVO NOME: ")
            estado = input("NOVO ESTADO: ")
            cls.times.remove(x)
            x = Time(id, nome, estado)
            cls.times.append(x)
        else:
            print("ESSE TIME NÃO EXISTE")

    @classmethod
    def excluir_time(cls):
        FutebolUI.listar_time()
        id = int(input("INFORME O ID DO TIME: "))
        x = FutebolUI.listar_id(id)
        if x != None:
            cls.times.remove(x)
        else:
            print("TIME NÃO ENCONTRADO")

    @classmethod
    def inserir_jogador(cls):
        id = int(input("INFORME O ID: "))
        nome = input("INFORME O NOME: ")
        camisa = int(input("INFORME A CAMISA: "))
        idTime = int(input("INFORME O ID DO TIME: "))

        x = Jogador(id, nome, camisa, idTime)
        cls.jogadores.append(x)

    @classmethod
    def listar_jogador(cls):
        if len(cls.jogadores) == 0:
            print("NENHUM JOGADOR CADASTRADO")
        else:
            for x in cls.jogadores:
                print(x)

    @classmethod
    def listar_id_jogador(cls, id):
        for x in cls.jogadores:
            if x.get_id() == id:
                return x
        return None

    @classmethod
    def atualizar_jogador(cls):
        FutebolUI.listar_jogador()
        id = int(input("INFORME O ID DO JOGADOR: "))
        x = FutebolUI.listar_id_jogador(id)
        if x != None:
            nome = input("NOVO NOME: ")
            camisa = int(input("NOVA CAMISA: "))
            idTime = int(input("NOVO ID TIME: "))
            cls.jogadores.remove(x)
            x = Jogador(id, nome, camisa, idTime)
            cls.jogadores.append(x)
        else:
            print("JOGADOR NÃO ENCONTRADO")

    @classmethod
    def excluir_jogador(cls):
        FutebolUI.listar_jogador()
        id = int(input("INFORME O ID DO JOGADOR: "))
        x = FutebolUI.listar_id_jogador(id)
        if x != None:
            cls.jogadores.remove(x)
        else:
            print("JOGADOR NÃO ENCONTRADO")

    @classmethod
    def listar_jogadores_do_time(cls):
        idTime = int(input("INFORME O ID DO TIME: "))
        achou = False
        for x in cls.jogadores:
            if x.get_idTime() == idTime:
                print(x)
                achou = True
        if achou == False:
            print("NENHUM JOGADOR NESSE TIME")

    @classmethod
    def transferir_jogador(cls):
        FutebolUI.listar_jogador()
        id = int(input("INFORME O ID DO JOGADOR: "))
        x = FutebolUI.listar_id_jogador(id)
        if x != None:
            novoTime = int(input("NOVO ID DO TIME: "))
            x.set_idTime(novoTime)
            print("JOGADOR TRANSFERIDO")
        else:
            print("JOGADOR NÃO ENCONTRADO")

if __name__ == "__main__":
    FutebolUI.main()