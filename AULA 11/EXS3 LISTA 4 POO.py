class Pais:
    def __init__(self, i, n, p, a):
        self.__id = i
        self.__nome = n
        self.__populacao = p
        self.__area = a
    def set_nome(self, n): self.__nome = n
    def set_populacao(self, p): self.__populacao = p
    def set_area(self, a): self.__area = a
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_populacao(self): return self.__populacao
    def get_area(self): return self.__area
    def densidade(self):
        if self.__area == 0:
            return 0
        return self.__populacao / self.__area
    def __str__(self):
        return (f"{self.__id} - {self.__nome} - "
                f"Pop: {self.__populacao} - Área: {self.__area} - "
                f"Densidade: {self.densidade():.2f}")

class PaisUI:
    paises = []
    @staticmethod
    def main():
        op = 0
        while op != 7:
            op = PaisUI.menu()
            if op == 1: PaisUI.inserir()
            if op == 2: PaisUI.listar()
            if op == 3: PaisUI.atualizar()
            if op == 4: PaisUI.excluir()
            if op == 5: PaisUI.mais_populoso()
            if op == 6: PaisUI.mais_povoado()

    @staticmethod
    def menu():
        print("-" * 50)
        print("1- INSERIR")
        print("2- LISTAR")
        print("3- ATUALIZAR")
        print("4- EXCLUIR")
        print("5- MAIS POPULOSO")
        print("6- MAIS POVOADO")
        print("7- FIM")
        return int(input("INFORME UMA OPÇÃO: "))

    @classmethod
    def inserir(cls):
        id = int(input("ID: "))
        nome = input("NOME: ")
        pop = int(input("POPULAÇÃO: "))
        area = float(input("ÁREA: "))
        p = Pais(id, nome, pop, area)
        cls.paises.append(p)

    @classmethod
    def listar(cls):
        if len(cls.paises) == 0:
            print("NENHUM PAÍS CADASTRADO")
        else:
            for p in cls.paises:
                print(p)

    @classmethod
    def atualizar(cls):
        id = int(input("ID DO PAÍS: "))
        for p in cls.paises:
            if p.get_id() == id:
                nome = input("NOVO NOME: ")
                pop = int(input("NOVA POPULAÇÃO: "))
                area = float(input("NOVA ÁREA: "))
                p.set_nome(nome)
                p.set_populacao(pop)
                p.set_area(area)
                print("ATUALIZADO!")
                return
        print("PAÍS NÃO ENCONTRADO!")

    @classmethod
    def excluir(cls):
        id = int(input("ID DO PAÍS: "))
        for p in cls.paises:
            if p.get_id() == id:
                cls.paises.remove(p)
                print("EXCLUÍDO!")
                return
        print("PAÍS NÃO ENCONTRADO!")

    @classmethod
    def mais_populoso(cls):
        if len(cls.paises) == 0:
            print("NENHUM PAÍS CADASTRADO")
            return
        maior = cls.paises[0]
        for p in cls.paises:
            if p.get_populacao() > maior.get_populacao():
                maior = p
        print("MAIS POPULOSO:")
        print(maior)

    @classmethod
    def mais_povoado(cls):
        if len(cls.paises) == 0:
            print("NENHUM PAÍS CADASTRADO")
            return
        maior = cls.paises[0]
        for p in cls.paises:
            if p.densidade() > maior.densidade():
                maior = p
        print("MAIS POVOADO:")
        print(maior)


if __name__ == "__main__":
    PaisUI.main()