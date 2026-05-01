class Pais():
    def __init__(self, n, p, a):
        self.set_nome(n)
        self.set_populacao(p)
        self.set_area(a)
    def set_nome(self, nome):
        if len(nome) >= 3:
            self.__nome = nome
        else: raise ValueError()
    def set_populacao(self, populacao):
        if populacao > 0:
            self.__populacao = populacao
        else: raise ValueError()
    def set_area(self, area):
        if area > 0:
            self.__area = area
        else: raise ValueError()
    def get_nome(self):
        return self.__nome
    def get_populacao(self):
        return self.__populacao
    def get_area(self):
        return self.__area
    def densidade(self):
        return self.__populacao / self.__area
    def __str__(self):
        return (f"PAÍS: {self.__nome}\n"
                f"POPULAÇÃO: {self.__populacao}\n"
                f"ÁREA: {self.__area:.2f} km²")

class PaisUI:
    @staticmethod
    def main():
        op = 0
        while op != 2:
            op = PaisUI.menu()
            if op == 1:
                PaisUI.calculo()

    @staticmethod
    def menu():
        print("-" * 50)
        print("1 - CALCULAR DENSIDADE")
        print("2 - FIM")
        return int(input("ESCOLHA UMA OPÇÃO: "))

    @staticmethod
    def calculo():
        nome = input("NOMEDO PAÍS: ")
        populacao = int(input("POPULAÇÃO: "))
        area = float(input("ÁREA (km²): "))
        p = Pais(nome, populacao, area)
        print("DADOS DO PAÍS:")
        print(p)
        print(f"DENSIDADE DEMOGRÁFICA: {p.densidade():.2f} hab/km²")

PaisUI.main()