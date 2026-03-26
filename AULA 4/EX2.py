#EXERCÍCIO 2

expressao = input("Digite a operação tipo 20+100: ")

if '+' in expressao:
    a, b = expressao.split('+')
    resultado = int(a) + int(b)
elif '-' in expressao:
    a, b = expressao.split('-')
    resultado = int(a) - int(b)
elif '*' in expressao:
    a, b = expressao.split('*')
    resultado = int(a) * int(b)
elif '/' in expressao:
    a, b = expressao.split('/')
    resultado = int(a) / int(b)
print("Resultado =", resultado)
