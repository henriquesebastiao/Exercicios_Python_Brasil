"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax^2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências,
informando ao usuário nas seguintes situações:

    A) Se o usuário informar o valor de A igual a zero,
    a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
    B) Se o delta calculado for negativo, a equação não possui raízes reais.
    Informe ao usuário e encerre o programa;
    C) Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    D) Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""

import math


def calcula_delta(a, b, c):
    return b ** 2 - 4 * a * c


def calcula_raizes(delta, a, b):
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    if x1 == x2:
        return x1
    else:
        return x1, x2


if __name__ == '__main__':
    a = float(input("Informe o valor de A: "))
    b = float(input("Informe o valor de B: "))
    c = float(input("Informe o valor de C: "))

    if a == 0:
        print("A equação não é do segundo grau!")
    elif calcula_delta(a, b, c) < 0:
        print("A equação não possui raízes reais!")
    elif calcula_delta(a, b, c) == 0:
        print(f"A equação possui apenas uma raiz real: {calcula_raizes(calcula_delta(a, b, c), a, b)}")
    else:
        print(f'''Raízes:
x1 = {calcula_raizes(calcula_delta(a, b, c), a, b)[0]}
x2 = {calcula_raizes(calcula_delta(a, b, c), a, b)[1]}''')
