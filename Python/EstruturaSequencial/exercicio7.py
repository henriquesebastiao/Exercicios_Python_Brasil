"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""


def calcula_area_quadrado(tamanho_lado):
    return tamanho_lado ** 2


lado = float(input("Informe o tamanho do lado do quadrado: "))
print(f"Resultado: {calcula_area_quadrado(lado) * 2}")
