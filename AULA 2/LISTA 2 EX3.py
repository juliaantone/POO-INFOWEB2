print("Digite quatro valores inteiros:")

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

# Verificar se são diferentes
if n1 == n2 or n1 == n3 or n1 == n4 or n2 == n3 or n2 == n4 or n3 == n4:
    print("Erro: os valores devem ser diferentes!")
else:
    lista = [n1, n2, n3, n4]
    lista.sort()

    menor = lista[0]
    segundo_menor = lista[1]
    segundo_maior = lista[2]
    maior = lista[3]

    soma = segundo_menor + segundo_maior

    print(f"Maior valor = {maior}")
    print(f"Menor valor = {menor}")
    print(f"A soma do segundo maior com o segundo menor = {soma}")
