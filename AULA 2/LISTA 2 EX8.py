frase = input("Digite uma frase: ")

atual = frase

for i in range(len(frase)):
    atual = atual[1:] + atual[0]
    print(atual)
