#EXERCÍCIO 2

expressao = input("Digite a operação tipo 20+100: ")

if '+' in expressao:
    n1, n2 = expressao.split('+')
    resultado = int(n1) + int(n2)
elif '-' in expressao:
    n1, n2 = expressao.split('-')
    resultado = int(n1) - int(n2)
elif '*' in expressao:
    n1, n2 = expressao.split('*')
    resultado = int(n1) * int(n2)
elif '/' in expressao:
    n1, n2 = expressao.split('/')
    resultado = int(n1) / int(n2)
print("Resultado =", resultado)
