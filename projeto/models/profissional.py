class Profissional:
    def __init__(self, id, nome, email, fone, senha, especialidade):
        self.id(id)
        self.nome(nome)
        self.email(email)
        self.fone(fone)
        self.senha(senha)
        self.especialidade(especialidade)

    def get_id(self):
        return self.id
    def get_nome(self):
        return self.nome
    def get_email(self):
        return self.email
    def get_fone(self):
        return self.fone
    def get_senha(self):
        return self.senha
    def get_especialidade(self):
        return self.especialidade

    def set_id(self, id):
        self.id = id
    def set_nome(self, nome):
        self.nome = nome
    def set_email(self, email):
        self.email = email
    def set_fone(self, fone):
        self.fone = fone
    def set_senha(self, senha):
        self.senha = senha
    def set_especialidade(self, especialidade):
        self.especialidade = especialidade
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone} - {self.especialidade}"