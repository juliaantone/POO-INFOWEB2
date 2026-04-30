


class BingoUI:
@staticmethod
def menu():
print("\n1 - Novo jogo")
print("2 - Sortear número")
print("3 - Ver sorteados")
print("0 - Sair")
return int(input("Escolha: "))

@staticmethod
def main():
bingo = None

while True:
op = BingoUI.menu()

if op == 1:
n = int(input("Quantidade de bolas: "))
bingo = Bingo(n)

elif op == 2:
if bingo:
num = bingo.sortear()
if num:
print("Número sorteado:", num)
else:
print("Todos já foram sorteados!")
else:
print("Inicie um jogo primeiro!")

elif op == 3:
if bingo:
print("Sorteados:", bingo.sorteados())
else:
print("Inicie um jogo primeiro!")

elif op == 0:
break


# BingoUI.main()







class Contato:
def __init__(self, i, n, e, f):
self.id = i
self.nome = n
self.email = e
self.fone = f

def toString(self):
return f"ID: {self.id} | Nome: {self.nome} | Email: {self.email} | Fone: {self.fone}"


class ContatoUI:
contatos = []

@staticmethod
def menu():
print("\n1 - Inserir")
print("2 - Listar")
print("3 - Atualizar")
print("4 - Excluir")
print("5 - Pesquisar")
print("0 - Sair")
return int(input("Escolha: "))

@staticmethod
def inserir():
i = int(input("ID: "))
n = input("Nome: ")
e = input("Email: ")
f = input("Fone: ")
ContatoUI.contatos.append(Contato(i, n, e, f))

@staticmethod
def listar():
for c in ContatoUI.contatos:
print(c.toString())

@staticmethod
def atualizar():
i = int(input("ID do contato: "))
for c in ContatoUI.contatos:
if c.id == i:
c.nome = input("Novo nome: ")
c.email = input("Novo email: ")
c.fone = input("Novo fone: ")
return
print("Contato não encontrado!")

@staticmethod
def excluir():
i = int(input("ID do contato: "))
for c in ContatoUI.contatos:
if c.id == i:
ContatoUI.contatos.remove(c)
return
print("Contato não encontrado!")

@staticmethod
def pesquisar():
nome = input("Iniciais do nome: ")
for c in ContatoUI.contatos:
if c.nome.lower().startswith(nome.lower()):
print(c.toString())

@staticmethod
def main():
while True:
op = ContatoUI.menu()

if op == 1:
ContatoUI.inserir()
elif op == 2:
ContatoUI.listar()
elif op == 3:
ContatoUI.atualizar()
elif op == 4:
ContatoUI.excluir()
elif op == 5:
ContatoUI.pesquisar()
elif op == 0:
break


# ContatoUI.main()














class Pais:
def __init__(self, i, n, p, a):
self.id = i
self.nome = n
self.populacao = p
self.area = a

def densidade(self):
return self.populacao / self.area

def toString(self):
return f"{self.nome} | População: {self.populacao} | Área: {self.area} | Densidade: {self.densidade():.2f}"


class PaisUI:
paises = []

@staticmethod
def menu():
print("\n1 - Inserir")
print("2 - Listar")
print("3 - Atualizar")
print("4 - Excluir")
print("5 - Mais populoso")
print("6 - Mais povoado (densidade)")
print("0 - Sair")
return int(input("Escolha: "))

@staticmethod
def inserir():
i = int(input("ID: "))
n = input("Nome: ")
p = int(input("População: "))
a = float(input("Área: "))
PaisUI.paises.append(Pais(i, n, p, a))

@staticmethod
def listar():
for p in PaisUI.paises:
print(p.toString())

@staticmethod
def atualizar():
i = int(input("ID do país: "))
for p in PaisUI.paises:
if p.id == i:
p.nome = input("Novo nome: ")
p.populacao = int(input("Nova população: "))
p.area = float(input("Nova área: "))
return
print("País não encontrado!")

@staticmethod
def excluir():
i = int(input("ID do país: "))
for p in PaisUI.paises:
if p.id == i:
PaisUI.paises.remove(p)
return
print("País não encontrado!")

@staticmethod
def maisPopuloso():
if PaisUI.paises:
print(max(PaisUI.paises, key=lambda p: p.populacao).toString())

@staticmethod
def maisPovoado():
if PaisUI.paises:
print(max(PaisUI.paises, key=lambda p: p.densidade()).toString())

@staticmethod
def main():
while True:
op = PaisUI.menu()

if op == 1:
PaisUI.inserir()
elif op == 2:
PaisUI.listar()
elif op == 3:
PaisUI.atualizar()
elif op == 4:
PaisUI.excluir()
elif op == 5:
PaisUI.maisPopuloso()
elif op == 6:
PaisUI.maisPovoado()
elif op == 0:
break


# PaisUI.main()


