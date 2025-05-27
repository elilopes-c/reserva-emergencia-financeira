# Desafio: Calculadora de Reserva de Emergência Financeira

## Visão Geral do Projeto

Este projeto consiste em uma aplicação interativa desenvolvida com **Streamlit** que visa auxiliar no planejamento financeiro pessoal. A ferramenta calcula o valor ideal para a reserva de emergência e estima o tempo necessário para atingir esse objetivo, considerando o aporte mensal e o rendimento dos juros compostos da taxa SELIC informada pelo usuário.

## Desafio e Funcionalidades

O programa foi desenvolvido em Python e apresenta as seguintes funcionalidades principais:

1.  **Coleta de Dados do Usuário via Interface Web:**
    * **Despesas Mensais:** O valor total das despesas fixas e variáveis que o usuário possui por mês.
    * **Tipo de Renda:** Seleção se a renda do usuário é "Previsível" (ex: salário fixo) ou "Imprevisível" (ex: autônomo com renda variável).
    * **Aporte Mensal:** O valor que o usuário pode economizar e investir mensalmente para a reserva de emergência.
    * **Taxa SELIC Anual:** O usuário informa a taxa SELIC anual atual (em percentual, ex: 10.5 para 10.5%).
    * **Validação de Entradas:** Todas as entradas numéricas são validadas para garantir que sejam valores positivos, e o tipo de renda é validado para ser uma das opções permitidas.

2.  **Cálculo do Valor da Reserva de Emergência:**
    * Se o tipo de renda for "Previsível", a reserva ideal é equivalente a **6 vezes** as despesas mensais.
    * Se o tipo de renda for "Imprevisível", a reserva ideal é equivalente a **12 vezes** as despesas mensais.

3.  **Simulação e Estimativa do Tempo para Atingir a Reserva:**
    * O programa simula o crescimento da reserva mês a mês.
    * Considera o aporte mensal informado pelo usuário.
    * Aplica o rendimento da **taxa SELIC mensal (calculada a partir da anual informada)** sobre o saldo acumulado, utilizando o conceito de juros compostos.
    * Calcula o número total de meses e a conversão para anos e meses para atingir o valor da reserva.

## Saída e Relatório Detalhado

Após o usuário clicar no botão "Calcular Reserva de Emergência", o programa apresenta um relatório claro e detalhado na própria interface web, exibindo as seguintes informações:

* **Resumo Geral:**
    * Despesas Mensais Informadas.
    * Tipo de Renda (Previsível/Imprevisível).
    * Aporte Mensal.
    * Taxa SELIC Anual Utilizada no cálculo.
    * **Valor Total Necessário para a Reserva de Emergência.**
    * **Tempo Estimado para Atingir a Reserva** (em anos e meses).
* **Evolução Mensal Detalhada:**
    * Uma tabela interativa mostrando o progresso da reserva mês a mês, incluindo:
        * Número do Mês.
        * Saldo Inicial do Mês.
        * Aporte Mensal Realizado.
        * Juros Recebidos no Mês.
        * Saldo Final do Mês.

## Como Acessar e Utilizar

Este programa está hospedado gratuitamente no **Streamlit Community Cloud**, tornando-o acessível a qualquer pessoa com conexão à internet.

* **Acesse a Aplicação:** [Clicando aqui](https://reserva-emergencia-rotainvest.streamlit.app/)

* **Instruções de Uso:**
   1.  Acesse o link acima.
   2.  No painel lateral, preencha os campos com suas despesas mensais, escolha seu tipo de renda, informe seu aporte mensal para a reserva e digite a taxa SELIC anual atual.
   3.  Clique no botão "Calcular Reserva de Emergência".
   4.  O relatório detalhado e a tabela de evolução aparecerão na tela principal.
