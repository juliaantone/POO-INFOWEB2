class Agua:
    def __init__(self, mes, ano, consumo):
        self.mes = mes
        self.ano = ano
        self.consumo = consumo
    def calcular_conta(self):
        if self.consumo <= 10:
            return 38.00
        elif self.consumo <= 20:
            a = self.consumo - 10
            return 38.00 + (a * 5)
        else:
            b = 10 * 5 
            c = (self.consumo - 20) * 6
            return 38.00 + b + c

mes = input("Digite o mês por extenso: ")
ano = int(input("Digite o ano por extenso: "))
consumo = float(input("Digite o consumo em metros quadrado: "))
conta = Agua(mes, ano, consumo)
valor = conta.calcular_conta()

print(f"Valor da sua conta de água: R$ {valor:.2f}")