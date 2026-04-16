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
    def calc_cincunferencia(self):
        return 2 * math.pi * self.__r
    

class Viagem:
    def __init__(self):
        self.__d = 0
        self.__t = 0
    def set_distancia(self, v):
        if v >= 0: self.__d = v
        else: raise ValueError()
    def set_tempo(self, v):
        if v > 0: self.__t = v
        else: raise ValueError()
    def get_distancia(self):
        return self.__d
    def get_tempo(self):
        return self.__t
    def calc_velocidade(self):
        return self.__d / self.__t
    

class ContaBancaria:
    def __init__(self):
        self.__t = ""
        self.__n = 0
        self.__s = 0
    def set_titular(self, nome):
        self.__t = nome
    def set_numero(self, num):
        if num > 0:
            self.__n = num
        else:
            raise ValueError()
    def set_saldo(self, valor):
        if valor >= 0:
            self.__s = valor
        else:
            raise ValueError()
    def get_titular(self):
        return self.__t
    def get_numero(self):
        return self.__n
    def get_saldo(self):
        return self.__s
    def depositar(self, valor):
        if valor > 0:
            self.__s += valor
        else:
            raise ValueError()
    def sacar(self, valor):
        if valor > 0 and valor <= self.__s:
            self.__s -= valor
        else:
            raise ValueError()
    

class Ingresso:
    def __init__(self):
        self.__d = ""
        self.__h = 0
    def set_dia(self, d):
        self.__d = d.lower()
    def set_hora(self, h):
        if 0 <= h <= 23:
            self.__h = h
        else:
            raise ValueError()
    def get_dia(self):
        return self.__d
    def get_hora(self):
        return self.__h
    def __valor_base(self):
        if self.__d in ["segunda", "terça", "terca", "quinta"]:
            return 16
        elif self.__d == "quarta":
            return 8
        elif self.__d in ["sexta", "sábado", "sabado", "domingo"]:
            return 20
        else:
            raise ValueError()
    def valor_inteira(self):
        valor = self.__valor_base()
        if self.__d == "quarta":
            return valor
        if 17 <= self.__h <= 23:
            valor *= 1.5
        return valor
    def valor_meia(self):
        if self.__d == "quarta":
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
        x.set_base(float(input("INFORME A BASE: ")))
        x.set_altura(float(input("INFORME A ALTURA: ")))
        area = x.calc_area()
        print(f"UM TRIÂNGULO DE BASE {x.get_base()} E ALTURA {x.get_altura()} TEM ÁREA: {area}")

    @staticmethod
    def circulo():
        x = Circulo()
        x.set_raio(float(input("INFORME O RAIO: ")))
        area = x.calc_area
        circun = x.calc_cincunferencia
        print(f"ÁREA DO CÍRCULO: {x.calc_area()} {area}")
        print(f"CIRCUNFERÊNCIA: {x.calc_cincunferencia()} {circun}")

    @staticmethod
    def viagem():
        x = Viagem()
        x.set_distancia(float(input("INFORME A DISTÂNCIA: ")))
        x.set_tempo(float(input("TEMPO: ")))
        print(f"VELOCIDADE MÉDIA: {x.calc_velocidade()}")

    @staticmethod
    def conta_bancaria():
        x = ContaBancaria()
        x.set_titular(input("NOME DO TITULAR DA CONTA: "))
        x.set_numero(int(input("NÚMERO DA CONTA: ")))
        x.set_saldo(float(input("SALDO INICIAL: ")))
        x.depositar(float(input("VALOR PARA DEPÓSITO: ")))
        x.sacar(float(input("VALOR PRA SAQUE: ")))
        print(f"TITULAR: {x.get_titular()}")
        print(f"NÚMERO DA CONTA: {x.get_numero()}")
        print(f"SALDO FINAL: {x.get_saldo()}")

    @staticmethod
    def ingresso():
        x = Ingresso()
        x.set_dia(input("DIA DA SESSÃO: "))
        x.set_hora(int(input("HORÁRIO: ")))
        print(f"INTERIA: R$ {x.valor_inteira()}")
        print(f"MEIA: R$ {x.valor_meia()}")

UI.main()