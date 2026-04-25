class Triangulo:
    def __init__(self, b, h):
        self.set_base(b)           
        self.set_altura(h)
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
    def __str__(self):
        return f"Eu sou um triângulo, minha base é {self.__b} e minha altura é {self.__h}"
    

import math
class Retangulo:
    def __init__(self, b, h):
        self.set_base(b)
        self.set_altura(h)
    def set_base(self, v):
        if v > 0: self.__b = v
        else: raise ValueError()
    def set_altura(self, v):
        if v > 0: self.__h = v
        else: raise ValueError()
    def get_base(self):
        return self.__b

    def get_altura(self):
        return self.__h

    def calc_area(self):
        return self.__b * self.__h

    def calc_diagonal(self):
        return math.sqrt(self.__b**2 + self.__h**2)

    def __str__(self):
        return f"Retângulo: base={self.__b}, altura={self.__h}"


class Frete:
    def __init__(self, d, p):
        self.set_distancia(d)
        self.set_peso(p)

    def set_distancia(self, v):
        if v > 0: self.__d = v
        else: raise ValueError("Distância deve ser positiva")

    def set_peso(self, v):
        if v > 0: self.__p = v
        else: raise ValueError("Peso deve ser positivo")

    def get_distancia(self):
        return self.__d

    def get_peso(self):
        return self.__p

    def calc_frete(self):
        return 0.01 * self.__d * self.__p

    def __str__(self):
        return f"Frete: distância={self.__d} km, peso={self.__p} kg"

class Equacao2Grau:
    def __init__(self, a, b, c):
        self.set_a(a)
        self.set_b(b)
        self.set_c(c)

    def set_a(self, v):
        if v != 0: self.__a = v
        else: raise ValueError("A não pode ser zero")

    def set_b(self, v):
        self.__b = v

    def set_c(self, v):
        self.__c = v

    def get_a(self): return self.__a
    def get_b(self): return self.__b
    def get_c(self): return self.__c

    def delta(self):
        return self.__b**2 - 4*self.__a*self.__c

    def tem_raizes_reais(self):
        return self.delta() >= 0

    def raiz1(self):
        if self.tem_raizes_reais():
            return (-self.__b + math.sqrt(self.delta())) / (2*self.__a)

    def raiz2(self):
        if self.tem_raizes_reais():
            return (-self.__b - math.sqrt(self.delta())) / (2*self.__a)

    def __str__(self):
        return f"Equação: {self.__a}x² + {self.__b}x + {self.__c}"




class UI:
    @staticmethod
    def main():
        op = 0
        while op != 0:
            op = UI.menu()

            if op == 1:
                UI.triangulo()
            elif op == 2:
                UI.retangulo()
            elif op == 3:
                UI.frete()
            elif op == 4:
                UI.equacao()
    
    def menu():
        print("-" * 50)
        print("ESCOLHA UMA OPÇÃO: ")
        print("-" * 50)
        print("1. TRIÂNGULO")
        print("2. RETÂNGULO ")
        print("3. FRETE ")
        print("4. EQUAÇÃO 2º GRAU ")
        print("0. SAIR")
        print("-" * 50)
        op = int(input("ESCOLHA UMA OPÇÃO: "))
        return op
    
    @staticmethod
    def triangulo():
        print("Calculo da área de um triângulo")
        b = (float(input("Informe o valor da base: ")))
        h = (float(input("Informe o valor da altura: ")))
        x = Triangulo(b, h)
        print(x)
        area = x.calc_area()
        print(f"Um triângulo com base {x.get_base()} e altura \ {x.get_altura()} tem área = {area}")

    @staticmethod
    def retangulo():
        b = float(input("Base: "))
        h = float(input("Altura: "))
        x = Retangulo(b, h)
        print(x)
        print("Área:", x.calc_area())
        print("Diagonal:", x.calc_diagonal())

    @staticmethod
    def frete():
        d = float(input("Distância (km): "))
        p = float(input("Peso (kg): "))
        x = Frete(d, p)
        print(x)
        print("Valor do frete: R$", x.calc_frete())

    @staticmethod
    def equacao():
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        x = Equacao2Grau(a, b, c)
        print(x)
        print("Delta:", x.delta())

        if x.tem_raizes_reais():
            print("Raiz 1:", x.raiz1())
            print("Raiz 2:", x.raiz2())
        else:
            print("Não possui raízes reais")





UI.main()