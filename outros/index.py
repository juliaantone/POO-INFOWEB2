from templates.manteravaliacaoclienteui import ManterAvaliacaoClienteUI

op = st.sidebar.selectbox(
    "MENU",
    [
        "MEUS DADOS",
        "AGENDAR SERVIÇO",
        "MEUS SERVIÇOS",
        "AVALIAR ATENDIMENTO"
    ]
)

if op == "AVALIAR ATENDIMENTO":
    ManterAvaliacaoClienteUI.main()

# No seu index.py, localize o método menu_cliente().

# Ele já possui as opções de dados pessoais, agendamento e consulta dos serviços.

# Altere-o para incluir a nova opção:

def menu_cliente():

    op = st.sidebar.selectbox(
        "MENU",
        [
            "MEUS DADOS",
            "AGENDAR SERVIÇO",
            "MEUS SERVIÇOS",
            "PAGAR ATENDIMENTO",
            "CANCELAR AGENDAMENTO"
        ]
    )

    if op == "MEUS DADOS":
        PerfilClienteUI.main()

    if op == "AGENDAR SERVIÇO":
        AgendarServicoUI.main()

    if op == "MEUS SERVIÇOS":
        MeusServicosUI.main()

    if op == "PAGAR ATENDIMENTO":
        PagarAtendimentoUI.main()

    if op == "CANCELAR AGENDAMENTO":
        CancelarAgendamentoUI.main()