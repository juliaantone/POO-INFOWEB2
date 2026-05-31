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
        self.set_valor_botelo(valor)
        # ATRIBUTOS COM VALOR INICIAL DEFINIDO
        self.__data_pagamento = None
        self.__valor_pago = 0
        self.__situacao_pagamentos = Pagamento.EM_ABERTO
    def set_cod_barras(self, cod):
        # SUPONDO QUE O BOLETO DEVE TER 10 DÍGITOS
        if len(cod) != 10: raise ValueError("Código deve ter 10 dígitos")
        self.cod_barras = cod
    def set_data_emissao(self, emissao):
        if emissao > datetime.now(): raise ValueError("Data não pode estar no futuro")
        self.__data_emissao = emissao
    def set_data_vencimento(self, venc):
        if venc < datetime.now(): raise ValueError("Data não pode estar no passado")
        self.__data_vencimento = venc
    def set_valor_boleto(self, valor):
        if valor < 0: raise ValueError("Valor não pode ser negativo")
        self.__valor_botelo = valor
    def pagar(self, valor_pago):
        if valor_pago < 0: raise ValueError("Valor não pode ser negativo")
        if self.__situacao_pagamentos != Pagamento.EM_ABERTO: raise ValueError("Boleto já foi pago")
        self.__valor_pago = valor_pago
        self.__data_pagamento = datetime.now()
        if self.__valor_pago == self.__valor_boleto: self.__situacao_pagamentos = Pagamento.PAGO
        else: self.__situacao_pagamentos = Pagamento.PAGO_PARCIAL
    def get_cod_barras(self): return self.__cod_barras
    def get_data_emissao(self): return self.__data_emissao
    def get_data_vencimento(self): return self.__data_venciemnto
    def get_data_pagamento(self): return self.__data_pagamento
    def get_valor_boleto(self): return self.__valor_botelo
    def get_situacao_pagamentos(self): return self.__situacao_pagamentos
    # no diagrama
    def get_situacao(self): return self.__situacao_pagamentos
    def __str__(self):
        s = f"Boeto: {self.__cod_barras} - Emissão {self.__data_emissao.strftime('%d/%m/%Y')}"
        s += f"Vencimento: {self.__data_vencimento.strftime('%d/%m/%Y')}"
        s += f"Valor Boleto R$: {self.__valor_botelo:.2f}"
        s += f"Valor Pago R$: {self.__valor_pago:.2f}"
        s += f"Pagamento: {self.__data_pagamento}"
        s += f"{self.__situacao_pagamentos}"
        return s