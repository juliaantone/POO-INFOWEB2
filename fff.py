import math

class Retangulo:
    def __init__(self, b, h):
        if b > 0 and h > 0:
            self.__b = b
            self.__h = h
        else:
            raise ValueError()

    def set_base(self, b):
        if b > 0:
            self.__b = b
        else:
            raise ValueError()

    def set_altura(self, h):
        if h > 0:
            self.__h = h
        else:
            raise ValueError()

    def get_base(self):
        return self.__b

    def get_altura(self):
        return self.__h

    def calc_area(self):
        return self.__b * self.__h

    def calc_diagonal(self):
        return math.sqrt(self.__b**2 + self.__h**2)

    def to_string(self):
        return f"Base: {self.__b}, Altura: {self.__h}"
    



class Frete:
    def __init__(self, d, p):
        if d > 0 and p > 0:
            self.__distancia = d
            self.__peso = p
        else:
            raise ValueError()

    def set_distancia(self, d):
        if d > 0:
            self.__distancia = d
        else:
            raise ValueError()

    def set_peso(self, p):
        if p > 0:
            self.__peso = p
        else:
            raise ValueError()

    def get_distancia(self):
        return self.__distancia

    def get_peso(self):
        return self.__peso

    def calc_frete(self):
        return self.__distancia * self.__peso * 0.01

    def to_string(self):
        return f"Distância: {self.__distancia} km, Peso: {self.__peso} kg"
    






# Testando Retangulo
r = Retangulo(10, 5)
print(r.to_string())
print("Área:", r.calc_area())
print("Diagonal:", r.calc_diagonal())

# Testando Frete
f = Frete(100, 50)
print(f.to_string())
print("Frete:", f.calc_frete())




import math

class Equacao2Grau:
    def __init__(self, a, b, c):
        self.set_a(a)
        self.set_b(b)
        self.set_c(c)

    # SETS
    def set_a(self, v):
        if v != 0:
            self.__a = v
        else:
            raise ValueError("a não pode ser 0")

    def set_b(self, v):
        self.__b = v

    def set_c(self, v):
        self.__c = v

    # GETS
    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    # DELTA
    def delta(self):
        return self.__b**2 - 4*self.__a*self.__c

    # TEM RAÍZES REAIS?
    def tem_raizes_reais(self):
        return self.delta() >= 0

    # RAIZ 1
    def raiz1(self):
        if self.tem_raizes_reais():
            return (-self.__b + math.sqrt(self.delta())) / (2*self.__a)
        else:
            return None

    # RAIZ 2
    def raiz2(self):
        if self.tem_raizes_reais():
            return (-self.__b - math.sqrt(self.delta())) / (2*self.__a)
        else:
            return None

    # TOSTRING
    def to_string(self):
        return f"a={self.__a}, b={self.__b}, c={self.__c}"
    



eq = Equacao2Grau(1, -3, 2)

print(eq.to_string())
print("Delta:", eq.delta())
print("Tem raízes reais?", eq.tem_raizes_reais())

if eq.tem_raizes_reais():
    print("Raiz 1:", eq.raiz1())
    print("Raiz 2:", eq.raiz2())






#-----------------------------------------
#|           Equacao2Grau               |
#-----------------------------------------
#| - a: double                         |
#| - b: double                         |
#| - c: double                         |
#-----------------------------------------
#| + Equacao2Grau(a,b,c): void         |
#| + set_a(v: double): void            |
#| + set_b(v: double): void            |
#| + get_a(): double                   |
#| + get_b(): double                   |
#| + get_c(): double                   |
#| + delta(): double                   |
#| + tem_raizes_reais(): boolean       |
#| + raiz1(): double                   |
#| + raiz2(): double                   |
#| + toString(): string                |
#-----------------------------------------









