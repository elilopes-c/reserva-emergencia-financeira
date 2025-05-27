# Desafio: Cálculo de Reserva de Emergência Financeira

## Visão Geral do Projeto

Este projeto tem como objetivo auxiliar no planejamento financeiro pessoal, calculando o valor ideal para a reserva de emergência e estimando o tempo necessário para atingir esse objetivo, considerando um aporte mensal e o rendimento da taxa SELIC.

## Desafio

Crie um programa em Python que solicite ao usuário as seguintes informações e realize os cálculos necessários:

1.  **Despesas Mensais:** O valor total das despesas fixas e variáveis que o usuário possui por mês.
2.  **Tipo de Renda:** Se a renda do usuário é "previsível" (por exemplo, salário fixo) ou "imprevisível" (por exemplo, autônomo com renda variável).
3.  **Aporte Mensal:** O valor que o usuário pode economizar e investir mensalmente para a reserva de emergência.

Com base nessas entradas, o programa deverá:

* **Calcular o Valor da Reserva de Emergência:**
    * Se o tipo de renda for "previsível", a reserva será equivalente a **6 vezes** as despesas mensais.
    * Se o tipo de renda for "imprevisível", a reserva será equivalente a **12 vezes** as despesas mensais.
* **Estimar o Tempo para Atingir a Reserva:**
    * Considerar o aporte mensal informado.
    * Considerar o rendimento da taxa SELIC (utilize um valor fixo de 12% ao ano para este desafio - *Este valor será atualizado no código com a taxa atual para um cálculo mais realista*).
    * O cálculo deve considerar o efeito dos juros compostos sobre o saldo da reserva.

## Saída

O programa deverá apresentar um relatório claro e detalhado, exibindo as seguintes informações:

* **Despesas Mensais Informadas:**
* **Tipo de Renda:**
* **Aporte Mensal:**
* **Valor Total Necessário para a Reserva de Emergência:**
* **Tempo Estimado para Atingir a Reserva:** (Em meses e/ou anos, da forma mais compreensível possível)

## Exemplo de Interação (Entrada/Saída)

**Entrada:**

```
Digite suas despesas mensais: 2000
Sua renda é previsível ou imprevisível? (P/I): P
Digite seu aporte mensal para a reserva: 300
```

**Saída:**

```
--- Relatório da Reserva de Emergência ---
Despesas Mensais: R$ 2000.00
Tipo de Renda: Previsível
Aporte Mensal: R$ 300.00

Valor Total Necessário para a Reserva de Emergência: R$ 12000.00
Tempo Estimado para Atingir a Reserva: Aproximadamente 37 meses (3 anos e 1 mês)
```
