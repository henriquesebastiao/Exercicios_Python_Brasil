"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""


def calcula_media(*notas):
    divisor = notas.__len__()
    soma = 0
    for nota in notas:
        soma += nota
    return soma / divisor


nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
nota4 = float(input("Informe a quarta nota: "))

print(f"Média: {calcula_media(nota1, nota2, nota3, nota4)}")
