"""
Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
Dica: utilize o operador módulo (resto da divisão).
"""


def verifica_paridade(numero):
    if numero % 2 == 0:
        return f'{numero} é par'
    else:
        return f'{numero} é ímpar'


if __name__ == '__main__':
    numero_informado = int(input("Número: "))
    print(verifica_paridade(numero_informado))
