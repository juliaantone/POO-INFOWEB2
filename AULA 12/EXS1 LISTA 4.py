class Time:
    def __init__(self, id, nome, estado):
        self.set_id(id)             
        self.set_nome(nome)
        self.set_estado(estado)
    def set_id(self, id):
       if id < 0: raise ValueError()
       self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError()
        self.__nome = nome 
    def set_estado(self, estado):
        if estado == "": raise ValueError()
        self.__estado = estado
    def get_id(self): 
        return self.__id
    def get_nome(self): 
        return self.__nome
    def get_estado(self): 
        return self.__estado
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__estado}"
    

class Jogador:
    def __init__(self, id, nome, camisa, idTime):
        self.set_id(id)             
        self.set_nome(nome)
        self.set_camisa(camisa)
        self.set_idTime(idTime)
    def set_id(self, id):
        if 0 > id < 99: raise ValueError()
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError()
        self.__nome = nome 
    def set_camisa(self, camisa):
        if camisa == "": raise ValueError()
    def set_idTime(self, idTime):
        if idTime < 0: raise ValueError()
        self.__idTime = idTime
    def get_id(self): 
        return self.__id
    def get_nome(self): 
        return self.__nome
    def get_camisa(self):
        return self.__camisa
    def get_idTime(self):
        return self.__idTime
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__camisa} - {self.__idTime}" 