"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?"

    O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
    Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
    entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""


def verifica_participacao(resultado):
    sim = 0
    for x in resultado:
        if x == 'sim':
            sim += 1
    if sim < 2:
        return 'INOCENTE'
    elif sim == 2:
        return 'SUSPEITA'
    elif 3 <= sim <= 4:
        return 'CÚMPLICE'
    else:
        return 'ASSASSINA'


if __name__ == '__main__':
    resultados = [
        input('Telefonou para a vítima? ').lower(),
        input('Esteve no local do crime? ').lower(),
        input('Mora perto da vítima? ').lower(),
        input('Devia para a vítima? ').lower(),
        input('Já trabalhou com a vítima? ').lower()
    ]

print(f"\nVeredito = {verifica_participacao(resultados)}")

