print("Digite 4 valores inteiros")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
pares = []
impares = []
if a % 2 == 0:
    pares.append(a)
else:
    impares.append(a)
if b % 2 == 0:
    pares.append(b)
else:
    impares.append(b)
if c % 2 == 0:
    pares.append(c)
else:
    impares.append(c)
if d % 2 == 0:
    pares.append(d)
else:
    impares.append(d)
soma_pares = sum(pares)
soma_impares = sum(impares)
print(soma_pares)
print(soma_impares)