"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:

Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""


def calcula_peso_ideal(altura, sexo):
    if sexo == "M" or sexo == "m":
        return 72.7 * altura - 58
    else:
        return 62.1 * altura - 44.7


print("M - Masculino")
print("F - Feminino")
sexo_pessoa = input("Informe o sexo da pessoa: ")
altura_pessoa = float(input("Informe a altura da pessoa: "))

print(f"Peso ideal: {calcula_peso_ideal(sexo_pessoa, altura_pessoa)}")
