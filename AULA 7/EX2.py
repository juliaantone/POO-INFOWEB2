# Incompleta
# Entidade
class Triangulo:
    def __init__(self):
        self.__b = 0            # Não parecem no diagrama
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
    
    
# Interface de usuário
class UI:
    @staticmethod
    def main():
        op = 0
        while op == 2:
            op = UI.menu()
            if op == 1: UI.triangulo()
            if op == 2: UI.circulo()
            if op == 3: UI.viagem()
            if op == 4: UI.banca_bancaria()
            if op == 5: UI.ingresso()
            
    @staticmethod
    def menu():
        print("1-Triângulo 2-Circulo 3-Viagem 4-Conta Bancária 5-Ingresso")

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


UI.main()