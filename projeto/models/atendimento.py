from datetime import datetime

class Atendimento:
    def __init__(self, id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario):
        self.id(id)
        self.data(data)
        self.queixa_principal(queixa_principal)
        self.historico_saude(historico_saude)
        self.avaliacao(avaliacao)
        self.prescricao(prescricao)
        self.id_horario(id_horario)
        
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
    def set_id_horarios(self, id_horario):
        if id_horario == "": raise ValueError("O histórico de saúde deve ser informado")
        self.__id_horario = id_horario

        