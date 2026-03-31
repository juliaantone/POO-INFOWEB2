class Pais:
    def __init__(self, nome, populacao, area):
        self.nome = nome
        self.populacao = populacao
        self.area = area
    def densidade_demografica(self):
        return self.populacao / self.area

paises = []
for i in range(10):
    print(f"\nPaís {i+1}:")
    nome = input("Nome: ")
    populacao = float(input("População: "))
    area = float(input("Área (km²): "))
    pais = Pais(nome, populacao, area)
    paises.append(pais)
maior_densidade = paises[0]
for pais in paises:
    if pais.densidade_demografica() > maior_densidade.densidade_demografica():
        maior_densidade = pais

print("\nPaís com maior densidade demográfica:")
print(f"Nome: {maior_densidade.nome}")
print(f"Densidade: {maior_densidade.densidade_demografica():.2f} hab/km²")