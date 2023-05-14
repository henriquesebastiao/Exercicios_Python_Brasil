"""
Faça um Programa que converta metros para centímetros.
"""


def converte_met_para_cent(metros):
    return metros * 100


metragem = float(input("Informe a metragem: "))
print(f"{metragem} metros equivalem à {converte_met_para_cent(metragem)} centímetros.")
