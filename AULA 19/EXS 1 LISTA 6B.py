import json
from datetime import datetime
class Contato:
  def __init__(self, id, nome, email, fone, nasc):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_nasc(nasc)

def set_id(self, id):
    if id < 0: raise ValueError("Id deve ser positivo")
    self.__id = id
def set_nome(self, nome):
    if nome == "": raise ValueError("Nome deve ser informado")
    self.__nome = nome
def set_email(self, email):
    if email == "": raise ValueError("E-mail deve ser informado")
    self.__email = email
def set_fone(self, fone):
    if fone == "": raise ValueError("Fone deve ser informado")
    self.__fone = fone
def set_nasc(self, nasc):
    if nasc > datetime.now() : raise ValueError("Data não pode ser no futuro")
    self.__nasc = nasc
def get_id(self): return self.__id
def get_nome(self): return self.__nome
def get_email(self): return self.__email
def get_fone(self): return self.__fone
def get_nasc(self): return self.__nasc
def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

def to_json(self):
    return { "id":self.__id, "nome":self.__nome, "email":self.__email, "fone":self.__fone, "nascimento":self.__nascstrftime("%d/%m/%Y")}

@staticmethod
def from_json(dic):
    return Contato(dic["id"], dic["nome"], dic["email"], dic["fone"], dic["nascimento"])
   
class ContatoUI:
    __contatos = []    
    @staticmethod    
    def main():
        ContatoUI.abrir()
        op = 0
        while op != 9:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()
            if op == 3: ContatoUI.atualizar()
            if op == 4: ContatoUI.excluir()
            if op == 4: ContatoUI.excluir()
            if op == 4: ContatoUI.excluir()
            if op == 4: ContatoUI.excluir()
            if op == 4: ContatoUI.excluir()

    @staticmethod
    def menu():
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 9-Fim")
        return int(input("Escolha uma opção: "))
   
    @classmethod
    def salvar(cls):    
        arquivo = open("clientes.json", mode = "w")
        json.dump(cls.__objetos, arquivo, default = Cliente.to_json, indent = 2)
        arquivo.close()
        print("O arquivo clientes.json foi salvo")
