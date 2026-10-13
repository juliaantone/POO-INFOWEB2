from avaliacaocliente import AvaliacaoCliente
from avaliacaoclientedao import AvaliacaoClienteDAO

# AVALIAÇÃO DO CLIENTE

@staticmethod
def avaliacao_inserir(nota, comentario, id_atendimento, id_cliente):
    obj = AvaliacaoCliente(
        0,
        nota,
        comentario,
        id_atendimento,
        id_cliente
    )
    AvaliacaoClienteDAO().inserir(obj)

@staticmethod
def avaliacao_listar():
    return AvaliacaoClienteDAO().listar()

@staticmethod
def avaliacao_listar_id(id):
    return AvaliacaoClienteDAO().listar_id(id)

@staticmethod
def avaliacao_atualizar(id, nota, comentario, id_atendimento, id_cliente):
    obj = AvaliacaoCliente(
        id,
        nota,
        comentario,
        id_atendimento,
        id_cliente
    )
    AvaliacaoClienteDAO().atualizar(obj)

@staticmethod
def avaliacao_excluir(id):
    AvaliacaoClienteDAO().excluir(id)




# Acrescente este método logo depois de horario_excluir():

    @staticmethod
    def horario_cancelar(id, id_cliente):

        horario = Service.horario_listar_id(id)

        if horario == None:
            return False

        if horario.get_id_cliente() != id_cliente:
            return False

        if horario.get_data() < datetime.now():
            return False

        horario.set_id_cliente(0)
        horario.set_id_servico(0)
        horario.set_confirmado(False)

        HorariosDAO().atualizar(horario)

        return True