"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

    A) salário bruto.
    B) quanto pagou ao INSS.
    C) quanto pagou ao sindicato.
    D) o salário líquido.
    E) calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

    Obs.: Salário Bruto - Descontos = Salário Líquido.
"""


def calcula_salario(valor_hora, horas_trabalhadas):
    """Função que calcula o salário bruto, o valor pago ao INSS, o valor pago ao sindicato e o salário líquido."""
    salario_bruto = valor_hora * horas_trabalhadas
    ir = salario_bruto * 0.11
    inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05
    salario_liquido = salario_bruto - ir - inss - sindicato
    return f'''+ Salário Bruto : R$ {salario_bruto:.2f}
- IR (11%) : R$ {ir:.2f}
- INSS (8%) : R$ {inss:.2f}
- Sindicato (5%) : {sindicato:.2f}
= Salário Liquido : R$ {salario_liquido:.2f}'''


valor = float(input("Informe quanto você ganha por hora: "))
horas = float(input("Informe a quantidade de horas trabalhadas: "))
print(calcula_salario(valor, horas))
