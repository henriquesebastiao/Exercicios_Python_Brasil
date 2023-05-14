"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

    A) Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    B) comprar apenas latas de 18 litros;
    C) comprar apenas galões de 3,6 litros;
    D) misturar latas e galões, de forma que o desperdício de tinta seja menor.
    Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

from math import ceil


def calcula_quantidade_latas(area):
    return ceil(area / 108)


def calcula_quantidade_galoes(area):
    return ceil(area / 21.6)


def calcula_economia_tinta(area):
    latas = calcula_quantidade_latas(area)
    area_restante = area - latas * 108
    galoes = calcula_quantidade_galoes(area_restante)
    latas = latas + latas
    galoes = galoes + galoes
    return latas, galoes


area_pintar = float(input("Informe a área a ser pintada: "))
print(f"Apenas latas: {calcula_quantidade_latas(area_pintar)} ==> Valor: R$ {calcula_quantidade_latas(area_pintar) * 80}.")
print(f"Apenas galões: {calcula_quantidade_galoes(area_pintar)} ==> Valor: R$ {calcula_quantidade_galoes(area_pintar) * 25}")
economia = calcula_economia_tinta(area_pintar)
print(f"Economizando tinta: Latas: {economia[0]}, Galões: {economia[1]} ==> Valor: R$ {economia[0] * 80 + economia[1] * 25}")
