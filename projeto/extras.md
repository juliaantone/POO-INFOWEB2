# 2. Como os arquivos se comunicam?
Imagine que um cliente queira agendar um serviço.
Ele abre o sistema, seleciona um profissional, escolhe um horário e seleciona o serviço desejado.
Para realizar essa operação, diferentes arquivos trabalham juntos.
O caminho é este:
1. AGENDAR SERVIÇO
   agendarservicoui.py
          |
          v
2. SERVICE
   service.py
          |
          v
3. DAO
   horariosdao.py
          |
          v
4. ARMAZENAMENTO
   horarios.json
Vamos entender o que cada um faz.
# Primeiro: a interface.
O arquivo agendarservicoui.py exibe as opções e recebe as escolhas do cliente. Ele utiliza componentes do Streamlit, como st.selectbox() e st.button()
# Segundo: o Service.
O arquivo service.py recebe a solicitação, executa o método responsável pelo agendamento e chama o DAO.
# Terceiro: o DAO.
O HorariosDAO localiza o horário e salva as alterações.
# Quarto: o JSON.
O arquivo horarios.json armazena os dados do horário, incluindo o cliente, o serviço, o profissional e a confirmação.
Essa divisão é importante porque cada arquivo possui uma responsabilidade específica.
Por exemplo, a interface não precisa saber como o JSON é gravado. Ela apenas chama o método do Service responsável pela operação.

# 3. Entendendo as classes dos modelos
Agora vamos estudar os arquivos da pasta models.
Eles definem os objetos que o sistema utiliza.
Os atributos são:

Atributo - Significado
id	    Identificador do cliente
nome	Nome do cliente
email	E-mail utilizado no acesso
fone	Telefone do cliente
senha	Senha de acesso