#Dicinário são separados por vigula
#é uma coleção de itens
#cada item tem 'chave: valor'
x = { "RN": "NATAL", "PB": "JOÃO PESSOA", "PE": "RECIFE" }
y = [1, 2, 3, 4]
z = (1, 2, 3, 4)

x["AM"] = "MANAUS"
print(x)
x.pop("PB")

for item in x.items(): print(item) #método
print(*x)

print(type(x))
print(type(y))
print(type(z))