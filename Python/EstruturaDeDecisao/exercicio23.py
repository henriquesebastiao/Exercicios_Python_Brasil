"""
Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento.
"""


def verifica_inteiro_ou_decimal(numero):
    if numero == round(numero):
        return f'{numero} é inteiro'
    else:
        return f'{numero} é decimal'


if __name__ == '__main__':
    numero_informado = float(input("Número: "))
    print(round(numero_informado))
    print(verifica_inteiro_ou_decimal(numero_informado))
