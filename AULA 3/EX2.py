class Triangulo:
    #atributo - dados que vão ser armazenados: b - base, h - altura
    def __init__(self):
        self.b = 0
        self.h = 0
    # método - cálculo que vão ser feitos
    def calc_area(self):
        return self.b * self.h / 2

x = Triangulo()
print("Informe a base do triângulo")
x.b = float(input())
print("Informe a base do triângulo")
x.h = float(input())
a = x.calc_area()
print(f"A área do triângulo é {a:.2f}")

y = Triangulo()
print("Informe a base do triângulo")
y.b = float(input())
print("Informe a base do triângulo")
y.h = float(input())
a = y.calc_area()
print(f"A área do triângulo é {a:.2f}")

print(f"Primeiro triângulo: base = {x.b}, altura = {x.h}, área = {x.calc_area()}")
print(f"Primeiro triângulo: base = {y.b}, altura = {y.h}, área = {y.calc_area()}")