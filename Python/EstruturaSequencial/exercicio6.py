"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""


def calcula_area_circulo(tamanho_raio):
    return tamanho_raio * 2 * 3.14


raio = float(input("Informe o raio da circunferência: "))
print(f"Área: {calcula_area_circulo(raio):.2f}")
