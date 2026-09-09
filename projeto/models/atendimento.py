from datetime import datetime

class Atendimento:
    def __init__(self, id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario):
        self.set_id(id)
        self.set_data(data)
        self.set_queixa_principal(queixa_principal)
        self.set_historico_saude(historico_saude)
        self.set_avaliacao(avaliacao)
        self.set_prescricao(prescricao)
        self.set_id_horario(id_horario)
        
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_data(self, data):
        if data > datetime.now(): raise ValueError("Data não pode ser no futuro")
        self.__data = data
    def set_queixa_principal(self, queixa_principal):
        if queixa_principal == "": raise ValueError("A queixa principal deve ser informado")
        self.__queixa_principal = queixa_principal
    def set_historico_saude(self, historico_saude):
        if historico_saude == "": raise ValueError("O histórico de saúde deve ser informado")
        self.__historico_saude = historico_saude
    def set_avaliacao(self, avaliacao):
        if avaliacao == "": raise ValueError("A avaliação deve ser informado")
        self.__avaliacao = avaliacao
    def set_prescricao(self, prescriscao):
        if prescriscao == "": raise ValueError("A prescrição deve ser informado")
        self.__prescricao = prescriscao
    def set_id_horario(self, id_horario):
        if id_horario == "": raise ValueError("O id do horário de saúde deve ser informado")
        self.__id_horario = id_horario

    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_queixa_principal(self): return self.__queixa_principal
    def get_historico_saude(self): return self.__historico_saude
    def get_avaliacao(self): return self.__avaliacao
    def get_prescricao(self): return self.__prescricao
    def get_id_horario(self): return self.__id_horario

    def to_json(self):
        return {
            "id": self.get_id(),
            "data": self.get_data().isoformat(),
            "queixa_principal": self.get_queixa_principal(),
            "historico_saude": self.get_historico_saude(),
            "avaliacao": self.get_avaliacao(),
            "prescricao": self.get_prescricao(),
            "id_horario": self.get_id_horario()
        }
    @staticmethod
    def from_json(dic):
        return Atendimento(
            dic["id"],
            datetime.fromisoformat(dic["data"]),
            dic["queixa_principal"],
            dic["historico_saude"],
            dic["avaliacao"],
            dic["prescricao"],
            dic["id_horario"]
        )
    def __str__(self):
        return f"{self.get_id()} - {self.get_data()} - Horário {self.get_id_horario()}"

        