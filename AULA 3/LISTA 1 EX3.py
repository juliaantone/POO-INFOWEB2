class ContaBancaria:
    def __init__(self, titular, numero_conta, saldo=0):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido.")
    def mostrar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

titular = input("Digite o nome do titular: ")
numero = input("Digite o número da conta: ")
conta = ContaBancaria(titular, numero)

while True:
    print("\n1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        valor = float(input("Digite o valor para depósito: "))
        conta.depositar(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor para saque: "))
        conta.sacar(valor)
    elif opcao == "3":
        conta.mostrar_saldo()
    elif opcao == "4":
        print("Encerrando...")
        break
    else:
        print("Opção inválida!")