import math

def Diagonal(b, h):
    return math.sqrt(b**2 + h**2)

base = float(input("Base: "))
altura = float(input("Altura: "))

print("Diagonal =", Diagonal(base, altura))
