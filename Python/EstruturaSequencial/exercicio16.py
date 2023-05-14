"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

from math import ceil


def calcula_quantidade_latas(area):
    """Função que calcula a quantidade de latas de tinta necessárias para pintar uma área."""
    return ceil(area / 54)


area_pintura = float(input("Informe o tamanho da área a ser pintada: "))
quantidade_latas = calcula_quantidade_latas(area_pintura)
print(f"Quantidade de latas: {quantidade_latas}")
print(f"Preço total: R$ {quantidade_latas * 80:.2f}")
