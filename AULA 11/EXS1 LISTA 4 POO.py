import random
class Bingo:
    def __init__(self, numBolas):
        self.__numBolas = numBolas
        self.__bolas = []
    def sortear(self):
        if len(self.__bolas) == self.__numBolas:
            return -1
        while True:
            n = random.randint(1, self.__numBolas)
            if n not in self.__bolas:
                self.__bolas.append(n)
                return n
    def sorteados(self):
        return self.__bolas

class BingoUI:
    bingo = None
    @staticmethod
    def main():
        op = 0
        while op != 4:
            op = BingoUI.menu()
            if op == 1:
                BingoUI.iniciarJogo()
            elif op == 2:
                BingoUI.sortear()
            elif op == 3:
                BingoUI.sorteados()

    @staticmethod
    def menu():
        print("-" * 50)
        print("1 - INICIAR NOVO JOGO")
        print("2 - SORTEAR")
        print("3 - VER SORTEADOS")
        print("4 - SAIR")
        return int(input("INFORME UMA OPÇÃO: "))

    @staticmethod
    def iniciarJogo():
        num = int(input("INFORME A QUANTIDADE DE BOLAS: "))
        BingoUI.bingo = Bingo(num)
        print("JOGO INICIADO!")

    @staticmethod
    def sortear():
        if BingoUI.bingo is None:
            print("INICIE UM JOGO PRIMEIRO!")
            return
        n = BingoUI.bingo.sortear()
        if n == -1:
            print("TODAS AS BOLAS JÁ FORAM SORTEADAS!")
        else:
            print(f"NÚMERO SORTEADO: {n}")

    @staticmethod
    def sorteados():
        if BingoUI.bingo is None:
            print("INICIE UM JOGO PRIMEIRO!")
        else:
            print("NÚMEROS SORTEADOS:")
            print(BingoUI.bingo.sorteados())


if __name__ == "__main__":
    BingoUI.main()