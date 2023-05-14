"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""


def calcula_salario_mensal(valor_hora, horas_trabalhadas):
    return valor_hora * horas_trabalhadas


valor = float(input("Informe quanto você ganha por hora: "))
horas = float(input("Informe a quantidade de horas trabalhadas: "))
print(f"Total do salário este mês: {calcula_salario_mensal(valor, horas)}")
