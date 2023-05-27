"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS
corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
    No exemplo o valor da hora é 5 e a quantidade de hora é 220.

            Salário Bruto: (5 * 220)        : R$ 1100,00
            (-) IR (5%)                     : R$   55,00
            (-) INSS ( 10%)                 : R$  110,00
            FGTS (11%)                      : R$  121,00
            Total de descontos              : R$  165,00
            Salário Liquido                 : R$  935,00
"""


def calcula_ir(salario):
    if salario <= 900:
        return 0, "ISENTO"
    elif 900 < salario <= 1500:
        return salario * 0.05, "5%"
    elif 1500 < salario <= 2500:
        return salario * 0.1, "10%"
    else:
        return salario * 0.2, "20%"


def calcula_inss(salario):
    return salario * 0.1


def calcula_fgts(salario):
    return salario * 0.11


def gerar_folha_pagamento(valor_hora, horas_trabalhadas):
    salario = valor_hora * horas_trabalhadas
    salario_bruto = salario
    ir = calcula_ir(salario)
    inss = calcula_inss(salario)
    fgts = calcula_fgts(salario)
    total_descontos = ir[0] + inss
    salario_liquido = salario_bruto - total_descontos
    return f'''Salário Bruto: ({valor_hora} * {horas_trabalhadas}) : R$ {salario_bruto:.2f}
(-) IR ({ir[1]}) : R$ {ir[0]:.2f}
(-) INSS (10%) : R$ {inss:.2f}
FGTS (11%) : R$ {fgts:.2f}
Total de descontos: R$ {total_descontos:.2f}
Salário Líquido: R$ {salario_liquido:.2f}'''


if __name__ == "__main__":
    horas = float(input("Informe a quantidade de horas trabalhadas: "))
    valor = float(input("Informe o valor da hora de trabalho: "))
    print(gerar_folha_pagamento(valor, horas))
