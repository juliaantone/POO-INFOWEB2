def RemoverEspacos(texto):
    return " ".join(texto.split())

frase = input("Digite um texto: ")
print(RemoverEspacos(frase))
