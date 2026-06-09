from enum import Enum
from datetime import datetime

class Pagamento(Enum):
    EM_ABERTO = 1
    PAGO_PARCIAL = 2
    PAGO = 3

class Boleto:   
    def __init__(self, cod, emissao, venc, valor):
        # ATRIBUTOS QUE SERÃO VELIDADOS
        self.set_cod_barras(cod)
        self.set_data_emissao(emissao)
        self.set_data_vencimento(venc)
        self.set_valor_boleto(valor)
        # ATRIBUTOS COM VALOR INICIAL DEFINIDO
        self.__data_pagamento = None
        self.__valor_pago = 0
        self.__situacao_pagamentos = Pagamento.EM_ABERTO
    def set_cod_barras(self, cod):
        # SUPONDO QUE O BOLETO DEVE TER 10 DÍGITOS
        if len(cod) != 10: raise ValueError("Código deve ter 10 dígitos")
        self.__cod_barras = cod
    def set_data_emissao(self, emissao):
        if emissao > datetime.now(): raise ValueError("Data não pode estar no futuro")
        self.__data_emissao = emissao
    def set_data_vencimento(self, venc):
        #if venc < datetime.now(): raise ValueError("Data não pode estar no passado")
        self.__data_vencimento = venc
    def set_valor_boleto(self, valor):
        if valor < 0: raise ValueError("Valor não pode ser negativo")
        self.__valor_boleto = valor
    def pagar(self, valor_pago):
        if valor_pago < 0: raise ValueError("Valor não pode ser negativo")
        if self.__situacao_pagamentos != Pagamento.EM_ABERTO: raise ValueError("Boleto já foi pago")
        self.__valor_pago = valor_pago
        self.__data_pagamento = datetime.now()
        if self.__valor_pago == self.__valor_boleto: self.__situacao_pagamentos = Pagamento.PAGO
        else: self.__situacao_pagamentos = Pagamento.PAGO_PARCIAL
    def get_cod_barras(self): return self.__cod_barras
    def get_data_emissao(self): return self.__data_emissao
    def get_data_vencimento(self): return self.__data_vencimento
    def get_data_pagamento(self): return self.__data_pagamento
    def get_valor_boleto(self): return self.__valor_botelo
    def get_situacao_pagamentos(self): return self.__situacao_pagamentos
    # NO DIAGRAMA 'get_situacao_pagamentos' ESTÁ COMO 'situacao'
    def get_situacao(self): return self.__situacao_pagamentos
    def __str__(self):
        s = f"BOLETO: {self.__cod_barras} - EMISSÃO {self.__data_emissao.strftime('%d/%m/%Y')}"
        s += f"VENCIMENTO: {self.__data_vencimento.strftime('%d/%m/%Y')}\n"
        s += f"VALOR DO BOLETO R$: {self.__valor_botelo:.2f}\n"
        s += f"VALOR PAGO R$: {self.__valor_pago:.2f}\n"
        if self.__data_pagamento != None:
            s += f"DATA DE PAGAMENTO: {self.__data_pagamento.strftime('%d/%m/%Y')}\n"
        s += f"SITUAÇÃO: {self.__situacao_pagamentos}"
        return s

class BoletoUI:
    __boletos = []
    @staticmethod
    def main():
        op = 0
        while op != 10:
            if op == 1: BoletoUI.inserir()
            if op == 2: BoletoUI.listar()
            if op == 3: BoletoUI.atualizar()
            if op == 4: BoletoUI.excluir()
            if op == 5: BoletoUI.emaberto()
            if op == 6: BoletoUI.pagos()
            if op == 7: BoletoUI.avencer()
            if op == 8: BoletoUI.vencidos()
            if op == 9: BoletoUI.pagar()

    @staticmethod
    def menu():
        print("-" * 30)
        print("1-INSERIR, 2-LISTAR, 3-ATUALIZAR, 4-EXCLUIR")
        print("5-BOLETOS EM ABERTO, 6-BOLETOS PAGOS")
        print("7-BOLETOS A VENCER,  8-BOLETOS VENCIDOS")
        print("9-PAGAR BOLETOS,     10-FIM")
        print("-" * 30)
        return int(input("ECOLHA UMA OPÇÃO: "))

    @classmethod
    def inserir(cls):
        cod = input("INFORME O CÓDIGO COM 10 DÍGITO: ")
        emissao = datetime.strptime(input("INFORME A DATA DE EMISSÃO dd/mm/aa"), "%d/%m/%Y")
        venc = datetime.strptime(input("INFORME A DATA DE VENCIMENTO dd/mm/aa"), "%d/%m/%Y")
        valor = float(input("INFORME O VALOR: "))
        x = Boleto(cod, emissao, venc, valor)
        cls.__boletos.append(x)

    @classmethod
    def listar(cls):
        for x in cls.__boletos: print(x)

    @classmethod
    def atualizar(cls):
        for x in cls.__boletos:
            cod = input("INFORME O CÓDIGO DO BOLETO A SER ATUALIZADO: ")
            for x in cls.__boletos:
                if x.get_cod_barras() == cod:
                    emissao = datetime.strptime(input("INFORME A DATA DE EMISSÃO dd/mm/aa"), "%d/%m/%Y")
                    venc = datetime.strptime(input("INFORME A DATA DE VENCIMENTO dd/mm/aa"), "%d/%m/%Y")
                    valor = float(input("INFORME O VALOR: "))
                    x.set_data_emissao(emissao)
                    x.set_data_vencimento(venc)
                    x.set_valor_boleto(valor)

    @classmethod
    def excluir(cls):  
       for x in cls.__boletos:
            cod = int(input("INFORME O CÓDIGO: "))
            for x in cls.__boletos:
                if x.get_cod_barras() == cod:
                    cls.__boletos.remove(x)

    @classmethod
    def emaberto(cls):
        for x in cls.__boletos:
            if x.get_situacao_pagamentos() == Pagamento.EM_ABERTO:
                print(x)

    @classmethod
    def pagos(cls):
        for x in cls.__boletos:
            if x.get_situacao_pagamentos() != Pagamento.EM_ABERTO:
                print(x)

    @classmethod
    def avencer(cls):
        for x in cls.__boletos:
            if x.get_situacao_pagamentos() == Pagamento.EM_ABERTO and x.get_data_vencimento() >= datetime.now(): print(x)

    @classmethod
    def pagar(cls):
        cod = input("INFORME O CÓDIGO DO BOLETO: ")
        for x in cls.__boletos:
            if x.get_cod_barras() == cod:
                valor = float(input("INFORME O VALOR PAGO: "))
                x.pagar(valor)
                print("BOLETO PAGO")
                return
        print("BOLETO NÃO ENCONTRADO")

    @classmethod
    def vencidos(cls):
        for x in cls.__boletos:
            if x.get_situacao_pagamentos() == Pagamento.EM_ABERTO and x.get_data_vencimento() < datetime.now(): print(x)

BoletoUI.main()