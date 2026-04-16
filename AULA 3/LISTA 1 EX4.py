class EntradaCinema:
    def __init__(self, dia, hora):
        self.dia = dia.lower()
        self.hora = hora
    def valor_base(self):
        if self.dia in ["segunda", "terça", "terca", "quinta"]:
            return 16
        elif self.dia == "quarta":
            return 8
        elif self.dia in ["sexta", "sábado", "sabado", "domingo"]:
            return 20
        else:
            return 0
    def valor_inteira(self):
        base = self.valor_base()
        if self.dia == "quarta":
            return base
        if 17 <= self.hora <= 23:
            base *= 1.5
        return base
    def valor_meia(self):
        if self.dia == "quarta":
            return self.valor_base()
        return self.valor_inteira() / 2

dia = input("Digite o dia da semana: ")
hora = int(input("Digite a hora da sessão (0-23): "))
entrada = EntradaCinema(dia, hora)
print(f"Valor da entrada inteira: R${entrada.valor_inteira():.2f}")
print(f"Valor da meia-entrada: R${entrada.valor_meia():.2f}")