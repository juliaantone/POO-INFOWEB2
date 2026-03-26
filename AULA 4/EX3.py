#EXERCÍCIO 3

frase = input("Digite uma frase: ")
soma = 0
for c in frase:
    if c.isdigit():
        soma += int(c)
print("Soma dos algarismos =", soma)