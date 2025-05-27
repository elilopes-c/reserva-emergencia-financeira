import streamlit as st
import pandas as pd 
# Configuração da página
st.set_page_config(page_title="Calculadora de Reserva de Emergência Rota Invest", page_icon="💰")
st.title("💰 Calculadora de Reserva de Emergência Rota Invest")
st.write(
    """
    Use esta ferramenta para calcular o valor ideal da sua reserva de emergência
    e estimar o tempo necessário para atingir seu objetivo, considerando seus aportes
    mensais e a taxa SELIC atual.
    """
)

# -------------------------------------------------------------
# 1. Entradas do Usuário com Streamlit

st.header("1. Informe Seus Dados Financeiros")

despesas_mensais = st.number_input(
    "Digite suas despesas mensais (R$):",
    min_value=0.01, # Mínimo para ser um valor positivo
    value=1000.00, # Valor padrão para iniciar
    step=100.00, # Incremento/decremento do botão
    format="%.2f" # Formato para duas casas decimais
)

tipo_renda = st.radio(
    "Sua renda é:",
    ("Previsível", "Imprevisível") # Opções de seleção
)
# Internamente, vamos converter para 'P' ou 'I' para o cálculo
tipo_renda_calc = 'P' if tipo_renda == "Previsível" else 'I'


aporte_mensal = st.number_input(
    "Digite seu aporte mensal para a reserva (R$):",
    min_value=0.01,
    value=100.00,
    step=10.00,
    format="%.2f"
)

taxa_selic_anual_input = st.number_input(
    "Digite a taxa SELIC anual atual (%):",
    min_value=0.01,
    value=14.75, # Valor padrão para a SELIC
    step=0.10,
    format="%.2f",
    help="Exemplo: digite 14.75 para 14.75%"
)
taxa_selic_anual_informada = taxa_selic_anual_input / 100 # Converter para decimal

# Adicionar um botão para acionar o cálculo
calcular_button = st.button("Calcular Reserva de Emergência")

# -------------------------------------------------------------
# 2. Lógica de Cálculo (Encapsulada em uma Função)

# Criamos uma função para agrupar todo o cálculo.
# Ela recebe as entradas do Streamlit e retorna os resultados.
def calcular_reserva_emergencia(despesas_mensais, tipo_renda_calc, aporte_mensal, taxa_selic_anual_informada):
    # -------------------------------------------------------------
    # 2.1. Cálculo do Valor da Reserva de Emergência

    valor_reserva_emergencia = 0.0
    if tipo_renda_calc == 'P':
        valor_reserva_emergencia = despesas_mensais * 6
    elif tipo_renda_calc == 'I':
        valor_reserva_emergencia = despesas_mensais * 12

    # -------------------------------------------------------------
    # 2.2. Cálculo do Tempo para Atingir a Reserva (com Juros Compostos)

    TAXA_SELIC_MENSAL = (1 + taxa_selic_anual_informada)**(1/12) - 1

    saldo_atual_reserva = 0.0
    meses_para_atingir = 0
    evolucao_mensal = [] # Lista para armazenar a evolução mês a mês

    while saldo_atual_reserva < valor_reserva_emergencia:
        saldo_inicial_do_mes = saldo_atual_reserva
        saldo_apos_aporte = saldo_inicial_do_mes + aporte_mensal
        rendimento_juros = saldo_apos_aporte * TAXA_SELIC_MENSAL
        saldo_atual_reserva = saldo_apos_aporte + rendimento_juros
        meses_para_atingir += 1

        # Armazenar os dados para a tabela
        evolucao_mensal.append({
            'mes': meses_para_atingir,
            'saldo_inicial': saldo_inicial_do_mes,
            'aporte': aporte_mensal,
            'juros_recebidos': rendimento_juros,
            'saldo_final': saldo_atual_reserva
        })
        # Condição para sair do loop se a meta for atingida no mês atual
        if saldo_atual_reserva >= valor_reserva_emergencia:
            break

    # Converter meses totais para anos e meses
    anos = meses_para_atingir // 12
    meses_restantes = meses_para_atingir % 12

    # Retornar todos os valores calculados
    return valor_reserva_emergencia, meses_para_atingir, anos, meses_restantes, evolucao_mensal

# -------------------------------------------------------------
# 3. Exibição dos Resultados (acionado pelo botão)

# Este bloco só será executado quando o botão "Calcular Reserva de Emergência" for clicado.
if calcular_button:
    # Verifica se os aportes e despesas são válidos para evitar loops infinitos ou erros
    if aporte_mensal <= 0:
        st.error("O aporte mensal deve ser maior que zero para calcular o tempo da reserva.")
    elif despesas_mensais <= 0:
         st.error("As despesas mensais devem ser maiores que zero para calcular a reserva.")
    else:
        valor_reserva, meses_totais, anos_calc, meses_restantes_calc, evolucao_dados = \
            calcular_reserva_emergencia(despesas_mensais, tipo_renda_calc, aporte_mensal, taxa_selic_anual_informada)
    st.header("3. Relatório da Reserva de Emergência")

    # -------------------------------------------------------------
    # Parte 3.1. Resumo das Entradas e Resultados Principais

    st.subheader("Resumo Geral")
    st.write(f"**Despesas Mensais:** R$ {despesas_mensais:.2f}")
    st.write(f"**Tipo de Renda:** {tipo_renda}") # Usamos 'tipo_renda' direto do radio, que é "Previsível" ou "Imprevisível"
    st.write(f"**Aporte Mensal:** R$ {aporte_mensal:.2f}")
    st.write(f"**Taxa SELIC Anual Utilizada:** {taxa_selic_anual_informada * 100:.2f}%")

    st.markdown("---") # Adiciona uma linha divisória

    st.metric(label="Valor Total Necessário para a Reserva de Emergência", value=f"R$ {valor_reserva:.2f}")

    # Formatação do tempo para exibição
    tempo_str = ""
    if anos_calc > 0:
        tempo_str += f"{anos_calc} ano{'s' if anos_calc > 1 else ''}"
    if meses_restantes_calc > 0:
        if anos_calc > 0:
            tempo_str += " e "
        tempo_str += f"{meses_restantes_calc} mês{'es' if meses_restantes_calc > 1 else ''}"

    if tempo_str == "":
        tempo_str = "Menos de um mês (ou já atingida)"

    st.metric(label="Tempo Estimado para Atingir a Reserva", value=tempo_str)

    # -------------------------------------------------------------
    # Parte 3.2. Evolução Mensal da Reserva (Tabela)

    st.subheader("Evolução Mensal Detalhada")

    # Convertendo a lista de dicionários para um DataFrame do pandas
    df_evolucao = pd.DataFrame(evolucao_dados)

    # Renomear colunas para exibição mais amigável
    df_evolucao.columns = [
        "Mês",
        "Saldo Inicial (R$)",
        "Aporte (R$)",
        "Juros Recebidos (R$)",
        "Saldo Final (R$)"
    ]

    st.dataframe(df_evolucao, use_container_width=True)

    # Adicionar uma mensagem de sucesso
    st.success("Cálculo concluído! Planeje-se para alcançar sua reserva, conte com a Rota Invest!")
