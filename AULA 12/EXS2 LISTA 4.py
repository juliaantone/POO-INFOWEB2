class PlayList:
    def __init__(self, id, nome, discricao):
        self.set_id(id)             
        self.set_nome(nome)
        self.set_discricao(discricao)
    def set_id(self, id):
       if id < 0: raise ValueError()
       self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError()
        self.__nome = nome
    def set_discricao(self, discricao):
        if discricao == "": raise ValueError()
        self.__discricao = discricao
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_discricao(self):
        return self.__discricao
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__discricao}"