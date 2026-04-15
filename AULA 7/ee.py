# Entidade
class Triangulo:
    def __init__(self):
        self.__b = 0            
        self.__h = 0
    def set_base(self, v):
        if v >= 0: self.__b = v
        else: raise ValueError()
    def set_altura(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError()
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    def calc_area(self):
        return self.__b * self.__h / 2
    

import math
class Circulo:
    def __init__(self):
        self.__r = 0
    def set_raio(self, v):
        if v >= 0: self.__r = v
        else: raise ValueError()
    def get_raio(self):
        return self.__r
    def calc_area(self):
        return math.pi * self.__r ** 2
    

class Viagem:
    def __init__(self):
        self.__dist = 0
        self.__tempo = 0
    def set_distancia(self, v):
        if v >= 0: self.__dist = v
        else: raise ValueError()
    def set_tempo(self, v):
        if v > 0: self.__tempo = v
        else: raise ValueError()
    def get_distancia(self):
        return self.__dist
    def get_tempo(self):
        return self.__tempo
    def calc_velocidade(self):
        return self.__dist / self.__tempo
    

class ContaBancaria:
    def __init__(self):
        self.__titular = ""
        self.__numero = 0
        self.__saldo = 0
    def set_titular(self, nome):
        self.__titular = nome
    def set_numero(self, num):
        if num > 0:
            self.__numero = num
        else:
            raise ValueError()
    def set_saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            raise ValueError()
    def get_titular(self):
        return self.__titular
    def get_numero(self):
        return self.__numero
    def get_saldo(self):
        return self.__saldo
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            raise ValueError()
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
        else:
            raise ValueError()
    

class Ingresso:
    def __init__(self):
        self.__dia = ""
        self.__hora = 0

    # SETS
    def set_dia(self, d):
        self.__dia = d.lower()

    def set_hora(self, h):
        if 0 <= h <= 23:
            self.__hora = h
        else:
            raise ValueError()

    # GETS
    def get_dia(self):
        return self.__dia

    def get_hora(self):
        return self.__hora

    # VALOR BASE
    def __valor_base(self):
        if self.__dia in ["segunda", "terça", "terca", "quinta"]:
            return 16
        elif self.__dia == "quarta":
            return 8  # já é meia
        elif self.__dia in ["sexta", "sábado", "sabado", "domingo"]:
            return 20
        else:
            raise ValueError()

    # INTEIRA
    def valor_inteira(self):
        valor = self.__valor_base()

        # quarta já é meia fixa
        if self.__dia == "quarta":
            return valor

        # acréscimo de 50% das 17h até 23h
        if 17 <= self.__hora <= 23:
            valor *= 1.5

        return valor

    # MEIA
    def valor_meia(self):
        # quarta já é meia para todos
        if self.__dia == "quarta":
            return 8

        return self.valor_inteira() / 2
    

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.triangulo()
            if op == 2: UI.circulo()
            if op == 3: UI.viagem()
            if op == 4: UI.conta_bancaria()
            if op == 5: UI.ingresso()
            
    @staticmethod
    def menu():
        print("-" * 50)
        print("ESCOLHA UMA OPÇÃO: ")
        print("-" * 50)
        print("1. TRIÂNGULO")
        print("2. CIRCULO")
        print("3. VIAGEM")
        print("4. CONTA BANCÁRIA")
        print("5. INGRESSO")
        print("-" * 50)
        return int(input("ESCOLHA: "))

    @staticmethod
    def triangulo():
        x = Triangulo()
        x.set_base(float(input("Informe o valor da base: ")))
        x.set_altura(float(input("Informe o valor da altura: ")))
        area = x.calc_area()
        print(f"Um triângulo com base {x.get_base()} e altura \ {x.get_altura()} tem área = {area}")

    @staticmethod
    def circulo():
        x = Circulo()
        x.set_raio(float(input("Informe o raio: ")))
        print(f"Área do círculo = {x.calc_area()}")

    @staticmethod
    def viagem():
        x = Viagem()
        x.set_distancia(float(input("Distância: ")))
        x.set_tempo(float(input("Tempo: ")))
        print(f"Velocidade média = {x.calc_velocidade()}")

    @staticmethod
    def conta_bancaria():
        x = ContaBancaria()
        
        x.set_titular(input("Nome do titular: "))
        x.set_numero(int(input("Número da conta: ")))
        x.set_saldo(float(input("Saldo inicial: ")))

        x.depositar(float(input("Valor para depósito: ")))
        x.sacar(float(input("Valor para saque: ")))

        print(f"Titular: {x.get_titular()}")
        print(f"Número da conta: {x.get_numero()}")
        print(f"Saldo final: {x.get_saldo()}")

    
    @staticmethod
    def ingresso():
        x = Ingresso()
        
        x.set_dia(input("Dia da sessão: "))
        x.set_hora(int(input("Hora (0-23): ")))

        print(f"Inteira: R$ {x.valor_inteira()}")
        print(f"Meia: R$ {x.valor_meia()}")

UI.main()
