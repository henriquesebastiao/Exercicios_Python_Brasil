"""
Faça um Programa para um caixa eletrônico.
O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.

    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
    uma nota de 50, uma nota de 5 e uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
    uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""


def saque(valor, quantidade_notas):
    """
    Função que calcula a quantidade de notas de cada valor serão fornecidas para um saque

    :param valor: Quantia a ser sacada
    :param quantidade_notas: Quantidade de notas disponíveis
    :return: Quantidade de notas de cada valor serão fornecidas para um saque
    """
    if quantidade_notas[0] >= valor // 100:
        cem = valor // 100
    else:
        cem = 0
    novo_valor = valor - cem * 100
    if quantidade_notas[1] >= novo_valor // 50:
        cinquenta = novo_valor // 50
    else:
        cinquenta = 0
    novo_valor -= cinquenta * 50
    if quantidade_notas[2] >= novo_valor // 10:
        dez = novo_valor // 10
    else:
        dez = 0
    novo_valor -= dez * 10
    if quantidade_notas[3] >= novo_valor // 5:
        cinco = novo_valor // 5
    else:
        cinco = 0
    novo_valor -= cinco * 5
    if quantidade_notas[4] >= novo_valor:
        um = novo_valor
    else:
        um = 0

    return cem, cinquenta, dez, cinco, um


if __name__ == '__main__':
    quantia_sacar = int(input("Valor: "))
    if quantia_sacar not in range(10, 601):
        print('Valor de saque fora do limite!')
    else:
        notas = saque(quantia_sacar, [100, 100, 100, 100, 100])  # Notas disponíveis de: 100, 50, 10, 5, 1
        if sum(notas) == 0:
            print('Não há notas suficientes para o saque!')
        else:
            print(f'Notas de R$ 100: {notas[0]}')
            print(f'Notas de R$ 50: {notas[1]}')
            print(f'Notas de R$ 10: {notas[2]}')
            print(f'Notas de R$ 5: {notas[3]}')
            print(f'Notas de R$ 1: {notas[4]}')
