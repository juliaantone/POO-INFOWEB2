class PlayList:
    def __init__(self, id, nome, descricao):
        self.set_id(id)             
        self.set_nome(nome)
        self.set_descricao(descricao)
    def set_id(self, id):
       if id < 0: raise ValueError()
       self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError()
        self.__nome = nome
    def set_descricao(self, descricao):
        if descricao == "": raise ValueError()
        self.__descricao = descricao
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_descricao(self):
        return self.__descricao
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__descricao}"
    

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
        if sequencia < 0: raise ValueError()
        self.__sequencia = sequencia
    def get_id(self):
        return self.__id
    def get_idPlayList(self):
        return self.__idPlayList
    def get_idMusica(self):
        return self.__idMusica 
    def get_sequencia(self):
        return self.__sequencia
    def __str__(self):
        return f"{self.__id} - {self.__idPlayList} - {self.__idMusica} - {self.__sequencia}"
    
class PlayListUI:
    playlists = []
    musicas = []
    itens = []

    @staticmethod
    def main():
        op = 0
        while op != 10:
            op = PlayListUI.menu()
            if op == 1: PlayListUI.inserir_playlist()
            if op == 2: PlayListUI.listar_playlist()
            if op == 3: PlayListUI.inserir_musica()
            if op == 4: PlayListUI.listar_musica()
            if op == 5: PlayListUI.inserir_item()
            if op == 6: PlayListUI.listar_itens()
            if op == 7: PlayListUI.listar_musicas_da_playlist()
            if op == 8: PlayListUI.atualizar_item()
            if op == 9: PlayListUI.excluir_item()

    @staticmethod
    def menu():
        print("-" * 50)
        print("1- INSERIR PLAYLIST")
        print("2- LISTAR PLAYLISTS")
        print("3- INSERIR MÚSICA")
        print("4- LISTAR MÚSICA")
        print("5- INSERIR ITEM NA PLAYLIST")
        print("6- LISTAR ITENS")
        print("7- VER UMA MÚSICA DA PLAYLIST")
        print("8- ATUALIZAR ITEM")
        print("9- EXCLUIR ITEM")
        print("10- FIM")
        return int(input("INFORME UMA OPÇÃO: "))
    
    @classmethod
    def inserir_playlist(cls):
        id = int(input("INFORME O ID: "))
        nome = input("INFORME O NOME: ")
        descricao = input("INFORME A DESCRIÇÃO: ")
        x = PlayList(id, nome, descricao)
        cls.playlists.append(x)

    @classmethod
    def listar_playlist(cls):
        if len(cls.playlists) == 0: print("NENHUMA PLAYLIST CADASTRADA")
        else:
            for x in cls.playlists: print(x)

    @classmethod
    def listar_id(cls, id):
        for x in cls.playlists:
            if x.get_id() == id: return x 
        return None

    @classmethod
    def inserir_musica(cls):
        id = int(input("INFORME O ID: "))
        titulo = input("INFORME O TÍTULO: ")
        artista = input("INFORME O ARTISTA: ")
        album = input("INFORME O ÁLBUM: ")
        x = Musica(id, titulo, artista, album)
        cls.musicas.append(x)

    @classmethod
    def listar_musica(cls):
        if len(cls.musicas) == 0:
            print("NENHUMA MÚSICA CADASTRADA")
        else:
            for x in cls.musicas:
                print(x)

    @classmethod
    def listar_id_musica(cls, id):
        for x in cls.musicas:
            if x.get_id() == id:
                return x
        return None

    @classmethod
    def inserir_item(cls):
        id = int(input("ID ITEM: "))
        idPlaylist = int(input("ID PLAYLIST: "))
        idMusica = int(input("ID MÚSICA: "))
        sequencia = int(input("SEQUÊNCIA: "))
        x = PlayListItem(id, idPlaylist, idMusica, sequencia)
        cls.itens.append(x)

    @classmethod
    def listar_itens(cls):
        if len(cls.itens) == 0:
            print("NENHUM ITEM CADASTRADO")
        else:
            for x in cls.itens:
                print(x)

    @classmethod
    def listar_id_item(cls, id):
        for x in cls.itens:
            if x.get_id() == id:
                return x
        return None

    @classmethod
    def listar_musicas_da_playlist(cls):
        idPlaylist = int(input("INFORME O ID DA PLAYLIST: "))
        achou = False
        for item in cls.itens:
            if item.get_idPlayList() == idPlaylist:
                musica = cls.listar_id_musica(item.get_idMusica())
                if musica != None:
                    print(f"SEQ {item.get_sequencia()} - {musica}")
                    achou = True
        if achou == False:
            print("NENHUMA MÚSICA NA PLAYLIST")

    @classmethod
    def atualizar_item(cls):
        cls.listar_itens()
        id = int(input("INFORME O ID DO ITEM: "))
        x = cls.listar_id_item(id)
        if x != None:
            idPlaylist = int(input("NOVO ID PLAYLIST: "))
            idMusica = int(input("NOVO ID MÚSICA: "))
            sequencia = int(input("NOVA SEQUÊNCIA: "))
            cls.itens.remove(x)
            x = PlayListItem(id, idPlaylist, idMusica, sequencia)
            cls.itens.append(x)
            print("ITEM ATUALIZADO")
        else:
            print("ITEM NÃO ENCONTRADO")

    @classmethod
    def excluir_item(cls):
        cls.listar_itens()
        id = int(input("INFORME O ID DO ITEM: "))
        x = cls.listar_id_item(id)
        if x != None:
            cls.itens.remove(x)
            print("ITEM EXCLUÍDO")
        else:
            print("ITEM NÃO ENCONTRADO")

if __name__ == "__main__":
    PlayListUI.main()