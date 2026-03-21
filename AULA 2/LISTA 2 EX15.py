def Primo(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# Exemplo de uso
num = int(input("Digite um número: "))

if Primo(num):
    print("É primo")
else:
    print("Não é primo")
