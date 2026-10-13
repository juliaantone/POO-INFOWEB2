class AvaliacaoCliente:

    def __init__(self, id, nota, comentario, id_atendimento, id_cliente):
        self.set_id(id)
        self.set_nota(nota)
        self.set_comentario(comentario)
        self.set_id_atendimento(id_atendimento)
        self.set_id_cliente(id_cliente)

    # SETS

    def set_id(self, id):
        if id < 0:
            raise ValueError("Id deve ser positivo")
        self.__id = id

    def set_nota(self, nota):
        if nota < 1 or nota > 5:
            raise ValueError("A nota deve estar entre 1 e 5")
        self.__nota = nota

    def set_comentario(self, comentario):
        if comentario == "":
            raise ValueError("O comentário deve ser informado")
        self.__comentario = comentario

    def set_id_atendimento(self, id_atendimento):
        if id_atendimento < 0:
            raise ValueError("Id do atendimento deve ser positivo")
        self.__id_atendimento = id_atendimento

    def set_id_cliente(self, id_cliente):
        if id_cliente < 0:
            raise ValueError("Id do cliente deve ser positivo")
        self.__id_cliente = id_cliente

    # GETS

    def get_id(self):
        return self.__id

    def get_nota(self):
        return self.__nota

    def get_comentario(self):
        return self.__comentario

    def get_id_atendimento(self):
        return self.__id_atendimento

    def get_id_cliente(self):
        return self.__id_cliente

    # JSON

    def to_json(self):
        return {
            "id": self.__id,
            "nota": self.__nota,
            "comentario": self.__comentario,
            "id_atendimento": self.__id_atendimento,
            "id_cliente": self.__id_cliente
        }

    @staticmethod
    def from_json(dic):
        return AvaliacaoCliente(
            dic["id"],
            dic["nota"],
            dic["comentario"],
            dic["id_atendimento"],
            dic["id_cliente"]
        )

    def __str__(self):
        return f"{self.__id} - Nota: {self.__nota}"