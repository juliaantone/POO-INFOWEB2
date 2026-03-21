def MMC(x, y):
    maior = max(x, y)

    while True:
        if maior % x == 0 and maior % y == 0:
            return maior
        maior += 1

# Exemplo de uso
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

print("MMC =", MMC(a, b))
