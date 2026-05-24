from datetime import datetime
from enum import Enum


class Pagamento(Enum):
    EmAberto = 1
    PagoParcial = 2
    Pago = 3


class Boleto:
    def __init__(self, codBarras, dataEmissao, dataVencimento, valorBoleto):
        self.set_codBarras(codBarras)
        self.set_dataEmissao(dataEmissao)
        self.set_dataVencimento(dataVencimento)
        self.set_valorBoleto(valorBoleto)

        self.__valorPago = 0
        self.__dataPagto = None
        self.__situacaoPagamento = Pagamento.EmAberto

    # SETTERS

    def set_codBarras(self, codBarras):
        if codBarras == "":
            raise ValueError("Código de barras inválido")
        self.__codBarras = codBarras

    def set_dataEmissao(self, dataEmissao):
        self.__dataEmissao = dataEmissao

    def set_dataVencimento(self, dataVencimento):
        self.__dataVencimento = dataVencimento

    def set_valorBoleto(self, valorBoleto):
        if valorBoleto <= 0:
            raise ValueError("Valor inválido")
        self.__valorBoleto = valorBoleto

    # GETTERS

    def get_codBarras(self):
        return self.__codBarras

    def get_dataEmissao(self):
        return self.__dataEmissao

    def get_dataVencimento(self):
        return self.__dataVencimento

    def get_valorBoleto(self):
        return self.__valorBoleto

    def get_valorPago(self):
        return self.__valorPago

    def get_dataPagto(self):
        return self.__dataPagto

    # MÉTODO PAGAR

    def pagar(self, valorPago):
        if valorPago <= 0:
            raise ValueError("Valor inválido")

        if self.__valorPago + valorPago > self.__valorBoleto:
            raise ValueError("Pagamento maior que o valor do boleto")

        self.__valorPago += valorPago
        self.__dataPagto = datetime.now()

        if self.__valorPago == 0:
            self.__situacaoPagamento = Pagamento.EmAberto

        elif self.__valorPago < self.__valorBoleto:
            self.__situacaoPagamento = Pagamento.PagoParcial

        else:
            self.__situacaoPagamento = Pagamento.Pago

    # SITUAÇÃO

    def situacao(self):
        return self.__situacaoPagamento

    # TO STRING

    def __str__(self):

        if self.__dataPagto is None:
            pagamento = "Sem pagamento"
        else:
            pagamento = self.__dataPagto.strftime("%d/%m/%Y")

        return (
            f"Código: {self.__codBarras} | "
            f"Emissão: {self.__dataEmissao.strftime('%d/%m/%Y')} | "
            f"Vencimento: {self.__dataVencimento.strftime('%d/%m/%Y')} | "
            f"Valor: R$ {self.__valorBoleto:.2f} | "
            f"Pago: R$ {self.__valorPago:.2f} | "
            f"Data Pagamento: {pagamento} | "
            f"Situação: {self.__situacaoPagamento.name}"
        )


class BoletoUI:
    __boletos = []

    @staticmethod
    def main():
        print("\n1 - Inserir")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("5 - Boletos em Aberto")
        print("6 - Boletos Pagos")
        print("7 - Boletos a Vencer")
        print("8 - Boletos Vencidos")
        print("9 - Pagar Boleto")
        print("10 - Sair")

        return int(input("Escolha uma opção: "))

    @staticmethod
    def menu():
        op = 0

        while op != 10:

            op = BoletoUI.main()

            if op == 1:
                BoletoUI.inserir()

            elif op == 2:
                BoletoUI.listar()

            elif op == 3:
                BoletoUI.atualizar()

            elif op == 4:
                BoletoUI.excluir()

            elif op == 5:
                BoletoUI.boletosEmAberto()

            elif op == 6:
                BoletoUI.boletosPagos()

            elif op == 7:
                BoletoUI.boletosAVencer()

            elif op == 8:
                BoletoUI.boletosVencidos()

            elif op == 9:
                BoletoUI.pagarBoleto()

            elif op == 10:
                print("Sistema encerrado!")

            else:
                print("Opção inválida!")

    @classmethod
    def inserir(cls):

        cod = input("Código de barras: ")

        emissao = datetime.strptime(
            input("Data emissão (dd/mm/aaaa): "),
            "%d/%m/%Y"
        )

        vencimento = datetime.strptime(
            input("Data vencimento (dd/mm/aaaa): "),
            "%d/%m/%Y"
        )

        valor = float(input("Valor do boleto: "))

        x = Boleto(cod, emissao, vencimento, valor)

        cls.__boletos.append(x)

        print("Boleto cadastrado!")

    @classmethod
    def listar(cls):

        if len(cls.__boletos) == 0:
            print("Nenhum boleto cadastrado")

        else:
            for x in cls.__boletos:
                print(x)

    @classmethod
    def atualizar(cls):

        cod = input("Informe o código de barras: ")

        for x in cls.__boletos:

            if x.get_codBarras() == cod:

                novoValor = float(input("Novo valor: "))

                novoVencimento = datetime.strptime(
                    input("Nova data de vencimento: "),
                    "%d/%m/%Y"
                )

                x.set_valorBoleto(novoValor)
                x.set_dataVencimento(novoVencimento)

                print("Boleto atualizado!")
                return

        print("Boleto não encontrado!")

    @classmethod
    def excluir(cls):

        cod = input("Informe o código de barras: ")

        for x in cls.__boletos:

            if x.get_codBarras() == cod:

                cls.__boletos.remove(x)

                print("Boleto removido!")
                return

        print("Boleto não encontrado!")

    @classmethod
    def boletosEmAberto(cls):

        encontrou = False

        for x in cls.__boletos:

            if x.situacao() == Pagamento.EmAberto:

                print(x)
                encontrou = True

        if encontrou == False:
            print("Nenhum boleto em aberto!")

    @classmethod
    def boletosPagos(cls):

        encontrou = False

        for x in cls.__boletos:

            if (
                x.situacao() == Pagamento.Pago or
                x.situacao() == Pagamento.PagoParcial
            ):

                print(x)
                encontrou = True

        if encontrou == False:
            print("Nenhum boleto pago!")

    @classmethod
    def boletosAVencer(cls):

        hoje = datetime.now()

        encontrou = False

        for x in cls.__boletos:

            if (
                x.get_dataVencimento() >= hoje and
                x.situacao() != Pagamento.Pago
            ):

                print(x)
                encontrou = True

        if encontrou == False:
            print("Nenhum boleto a vencer!")

    @classmethod
    def boletosVencidos(cls):

        hoje = datetime.now()

        encontrou = False

        for x in cls.__boletos:

            if (
                x.get_dataVencimento() < hoje and
                x.situacao() != Pagamento.Pago
            ):

                print(x)
                encontrou = True

        if encontrou == False:
            print("Nenhum boleto vencido!")

    @classmethod
    def pagarBoleto(cls):

        cod = input("Informe o código de barras: ")

        for x in cls.__boletos:

            if x.get_codBarras() == cod:

                valor = float(input("Valor do pagamento: "))

                x.pagar(valor)

                print("Pagamento realizado!")
                return

        print("Boleto não encontrado!")


BoletoUI.menu()