mes = int(input("Informe o número do mês (1 a 12): "))

if mes == 1:
    nome = "janeiro"
elif mes == 2:
    nome = "fevereiro"
elif mes == 3:
    nome = "março"
elif mes == 4:
    nome = "abril"
elif mes == 5:
    nome = "maio"
elif mes == 6:
    nome = "junho"
elif mes == 7:
    nome = "julho"
elif mes == 8:
    nome = "agosto"
elif mes == 9:
    nome = "setembro"
elif mes == 10:
    nome = "outubro"
elif mes == 11:
    nome = "novembro"
elif mes == 12:
    nome = "dezembro"
else:
    print("Mês inválido!")
    exit()

# Verificar trimestre
if mes >= 1 and mes <= 3:
    trimestre = "primeiro"
elif mes >= 4 and mes <= 6:
    trimestre = "segundo"
elif mes >= 7 and mes <= 9:
    trimestre = "terceiro"
else:
    trimestre = "quarto"

print(f"O mês de {nome} é do {trimestre} trimestre do ano")
