"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58.
"""


def calcula_peso_ideal(altura):
    return 72.7 * altura - 58


altura_pessoa = float(input("Informe a altura da pessoa: "))
print(f"O peso ideal é de: {calcula_peso_ideal(altura_pessoa)}")
