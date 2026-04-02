entrada = input("Digite números separados por vírgula: ")

numeros = entrada.split(',')
soma = 0
for n in numeros:
    soma += int(n)
print("Soma =", soma)