from models.cliente import Cliente
from models.clientedao import ClienteDAO
from models.servico import Servico
from models.servicodao import ServicoDAO
from models.horario import Horario
from models.horariosdao import HorariosDAO
from models.profissional import Profissional
from models.profissionaldao import ProfissionalDAO
from models.atendimento import Atendimento
from models.atendimentodao import AtendimentoDAO
from datetime import datetime, timedelta

class Service:
    #CLIENTE
    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        obj = Cliente(0, nome, email, fone, senha)
        ClienteDAO().inserir(obj)
    @staticmethod
    def cliente_listar():
        r = ClienteDAO().listar()
        r.sort(key = lambda obj : obj.get_nome().casefold())
        return r
    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)
    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        obj = Cliente(id, nome, email, fone, senha)
        ClienteDAO().atualizar(obj)
    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)
    @staticmethod
    def cliente_criar_admin():
        for c in Service.cliente_listar():
            if c.get_email() == "admin": return
        Service.cliente_inserir("admin", "admin", "fone", "1234")
    @staticmethod
    def cliente_autenticar(email, senha):
        for c in Service.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return{"id": c.get_id(), "nome": c.get_nome()}
        return None
    @staticmethod
    def horario_listar_cliente(id_cliente):
        r = []
        for h in Service.horario_listar():
            if h.get_id_cliente() == id_cliente:
                r.append(h)
        return r
    @staticmethod
    def cliente_alterar_senha(id, senha):
        cliente = Service.cliente_listar_id(id)
        if cliente != None:
            cliente.set_senha(senha)
            ClienteDAO().atualizar(cliente)

    #SERVIÇO
    @staticmethod
    def servico_inserir(descricao, valor):
        obj = Servico(0, descricao, valor)
        ServicoDAO().inserir(obj)
    @staticmethod
    def servico_listar():
        r = ServicoDAO().listar()
        r.sort(key = lambda obj : obj.get_descricao().casefold())
        return r
    @staticmethod
    def servico_listar_id(id):
        return ServicoDAO().listar_id(id)
    @staticmethod
    def servico_atualizar(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        ServicoDAO().atualizar(obj)
    @staticmethod
    def servico_excluir(id):
        ServicoDAO().excluir(id)

    #HORÁRIO
    @staticmethod
    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        obj = Horario(0, data)
        obj.set_confirmado(confirmado)
        obj.set_id_cliente(id_cliente)
        obj.set_id_servico(id_servico)
        obj.set_id_profissional(id_profissional)
        HorariosDAO().inserir(obj)
    @staticmethod
    def horario_listar():
        r = HorariosDAO().listar()
        r.sort(key = lambda obj : obj.get_data())
        return r
    @staticmethod
    def horario_listar_id(id):
          return HorariosDAO().listar_id(id)
    @staticmethod
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        obj = Horario(id, data)
        obj.set_confirmado(confirmado)
        obj.set_id_cliente(id_cliente)
        obj.set_id_servico(id_servico)
        obj.set_id_profissional(id_profissional)
        HorariosDAO().atualizar(obj)
    @staticmethod
    def horario_excluir(id):
        HorariosDAO().excluir(id)
    @staticmethod
    def horario_listar_disponiveis(id_profissional):
        r = []
        agora= datetime.now()
        for h in Service.horario_listar():
            if h.get_data() >= agora and h.get_confirmado() == False and h.get_id_cliente() == 0 and h.get_id_profissional() == id_profissional:
                r.append(h)
                r.sort(key = lambda h : h.get_data())
                return r
    @staticmethod
    def horario_abrir_agenda(data, hora_inicial, hora_final, intervalo, id_profissional):
        inicio = datetime.combine(data, hora_inicial)
        fim = datetime.combine(data, hora_final)
        while inicio < fim:
            Service.horario_inserir(inicio, False, 0, 0, id_profissional)
            inicio = inicio + timedelta(minutes=intervalo)
    @staticmethod
    def horario_confirmar(id):
        horario = Service.horario_listar_id(id)
        if horario != None:
            horario.set_confirmado(True)
            HorariosDAO().atualizar(horario)

    #PROFISSIONAL
    @staticmethod
    def profissional_inserir(nome, email, especialidade, senha):
        obj = Profissional(0, nome, email, especialidade, senha)
        ProfissionalDAO().inserir(obj)
    @staticmethod
    def profissional_listar():
        r = ProfissionalDAO().listar()
        r.sort(key = lambda obj : obj.get_nome ().casefold())
        return r
    @staticmethod
    def profissional_listar_id(id):
        return ProfissionalDAO().listar_id(id)
    @staticmethod
    def profissional_atualizar(id, nome, email, especialidade, senha):
        obj = Profissional(id, nome, email, especialidade, senha)
        ProfissionalDAO().atualizar(obj)
    @staticmethod
    def profissional_excluir(id):
        ProfissionalDAO().excluir(id)
    @staticmethod
    def profissional_autenticar(email, senha):
        for c in Service.profissional_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None
    @staticmethod
    def horario_listar_profissional(id_profissional):
        r = []
        for h in Service.horario_listar():
            if h.get_id_profissional() == id_profissional:
                r.append(h)
        return r
    @staticmethod
    def profissional_alterar_senha(id, senha):
        profissional = Service.profissional_listar_id(id)
        if profissional != None:
            profissional.set_senha(senha)
            ProfissionalDAO().atualizar(profissional)

        #ATENDIMENTO
    @staticmethod
    def atendimento_inserir(data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario):
        obj = Atendimento(0, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario)
        AtendimentoDAO().inserir(obj)
    @staticmethod
    def atendimento_listar():
        return AtendimentoDAO().listar()
    @staticmethod
    def atendimento_listar_id(id):
        return AtendimentoDAO().listar_id(id)
    @staticmethod
    def atendimento_atualizar(id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario):
        obj = Atendimento(id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario)
        AtendimentoDAO().atualizar(obj)
    @staticmethod
    def atendimento_excluir(id):
        AtendimentoDAO().excluir(id) 