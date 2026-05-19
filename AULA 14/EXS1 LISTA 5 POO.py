class Paciente:
    def __int__(self, nome, cpf, telefone, nascimento):
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.set_nascimento(nascimento)
    def set_nome(self, nome):
        if nome == "": raise ValueError()
        self.__nome = nome
    def set_cpf(self, cpf):
        if cpf < 0 or cpf > 12: raise ValueError()
        self.__cpf = cpf
    def set_telefone(self, te):
        if cpf < 0 or cpf > 12: raise ValueError()
        self.__cpf = cpf
    def set_cpf(self, cpf):
        if cpf < 0 or cpf > 12: raise ValueError()
        self.__cpf = cpf
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_descricao(self):
        return self.__descricao