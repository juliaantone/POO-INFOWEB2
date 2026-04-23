class Triangulo:
    def __init__(self, b, h):  #coloca tal na memória
        self.__b = b
        self.__h = h
    def __str__(self):  #retorna um texto
        return f"Óla eu sou um triângulo, minha base é {self.__b} e minha altura é {self.__h}"

x = Triangulo(10, 20)
print(x)