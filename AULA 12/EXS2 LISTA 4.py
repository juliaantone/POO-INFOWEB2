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
    
class PlayListItem:
    def __init__(self, id, idPlayList, idMusica, sequencia):
        self.set_id(id)             
        self.set_idPlayList(idPlayList)
        self.set_idMusica(idMusica)
        self.set_sequencia(sequencia)
    def set_id(self, id):
       if id < 0: raise ValueError()
       self.__id = id
    def set_idPlayList(self, idPlayList):
        if idPlayList < 0: raise ValueError()
        self.__idPlayList = idPlayList
    def set_idMusica(self, idMusica):
        if idMusica < 0: raise ValueError()
        self.__idMusica = idMusica
    def set_sequencia(self, sequencia):
        if sequencia == "": raise ValueError()
        self.__sequencia = sequencia
    def get_id(self):
        return self.__id
    def get_idPlayList(self):
        return self.__idPlayLis
    def get_idMusica(self):
        return self.__idMusica 
    def get_sequencia(self):
        return self.__sequencia
    def __str__(self):
        return f"{self.__id} - {self.__idPlayList} - {self.__idMusica} - {self.__sequencia}"
    
class Musica:
    def __init__(self, id, titulo, artista, album):
        self.set_id(id)             
        self.set_titulo(titulo)
        self.set_artista(artista)
        self.set_album(album)
    def set_id(self, id):
       if id < 0: raise ValueError()
       self.__id = id
    def set_titulo(self, titulo):
        if titulo == "": raise ValueError()
        self.__titulo = titulo
    def set_artista(self, artista):
        if artista == "": raise ValueError()
        self.__artista = artista
    def set_album(self, album):
        if album == "": raise ValueError()
        self.__album = album
    def get_id(self): 
        return self.__id
    def get_titulo(self): 
        return self.__titulo
    def get_artista(self):
        return self.__artista
    def get_album(self):
        return self.__album
    def __str__(self):
        return f"{self.__id} - {self.__titulo} - {self.__artista} - {self.__album}" 