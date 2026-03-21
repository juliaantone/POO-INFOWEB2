import math

def MenorInteiro(x):
    return math.ceil(x)


num = float(input("Digite um número: "))
print("Resultado =", MenorInteiro(num))
